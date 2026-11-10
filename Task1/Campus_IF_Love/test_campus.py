"""验证校园模板的送礼、对话和主菜单。"""

from contextlib import redirect_stdout
import io
import unittest
from unittest.mock import patch

import Campus_IF_Love as campus
from Campus_IF_Love import Character


class GiftTests(unittest.TestCase):
    def give(self, character, gift):
        with redirect_stdout(io.StringIO()):
            character.give_gift(gift)

    def test_role_specific_effect(self):
        for name, gift, expected in [
            ("学姐", "鲜花", 95),
            ("姐姐", "鲜花", 100),
            ("小白", "编程笔记", 100),
        ]:
            with self.subTest(name=name, gift=gift):
                character = Character(name, "测试角色", 85)
                self.give(character, gift)
                self.assertEqual(character.affinity, expected)
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(character.check_ending(), expected >= 100)

    def test_shared_default_effect(self):
        character = Character("学姐", "测试角色", 85)
        self.give(character, "奇怪的石头")
        self.assertEqual(character.affinity, 75)

    def test_unknown_gift_keeps_affinity(self):
        character = Character("学姐", "测试角色", 85)
        self.give(character, "巧克力")
        self.assertEqual(character.affinity, 85)

    def test_explicit_zero_effect(self):
        character = Character("学姐", "测试角色", 85)
        self.give(character, "夜宵外卖")
        self.assertEqual(character.affinity, 85)

    def test_repeated_gifts_keep_current_state(self):
        character = Character("学姐", "测试角色", 85)
        self.give(character, "鲜花")
        self.assertEqual(character.affinity, 95)
        self.give(character, "奇怪的石头")
        self.assertEqual(character.affinity, 85)

    def test_negative_affinity_is_preserved_as_in_template(self):
        character = Character("学姐", "测试角色", 0)
        self.give(character, "奇怪的石头")
        self.assertEqual(character.affinity, -10)


class TalkTests(unittest.TestCase):
    def talk(self, character, choice):
        output = io.StringIO()
        with patch("builtins.input", return_value=choice), redirect_stdout(output):
            character.talk()
        return output.getvalue()

    def test_each_role_displays_its_first_dialogue_and_options(self):
        for name in ("学姐", "小白", "姐姐"):
            with self.subTest(name=name):
                character = Character(name, "测试角色", 10)
                output = self.talk(character, "1")
                dialogue = campus.DIALOGUES[name][0]
                for field in ("text", "optionA", "optionB"):
                    self.assertIn(dialogue[field], output)
                self.assertEqual(character.affinity, 15)

    def test_second_choice_decreases_affinity(self):
        character = Character("学姐", "测试角色", 10)
        self.talk(character, "2")
        self.assertEqual(character.affinity, 5)

    def test_invalid_choices_keep_affinity(self):
        for choice in ("", "3", "hello"):
            with self.subTest(choice=choice):
                character = Character("学姐", "测试角色", 10)
                output = self.talk(character, choice)
                self.assertIn("无效选择", output)
                self.assertEqual(character.affinity, 10)

    def test_unknown_role_has_no_dialogue_or_affinity_change(self):
        character = Character("未知角色", "测试角色", 10)
        output = self.talk(character, "1")
        self.assertIn("暂时没有可用对话", output)
        self.assertEqual(character.affinity, 10)

    def test_empty_dialogue_list_keeps_affinity(self):
        character = Character("学姐", "测试角色", 10)
        with patch.dict(campus.DIALOGUES, {"学姐": []}):
            output = self.talk(character, "1")
        self.assertIn("暂时没有可用对话", output)
        self.assertEqual(character.affinity, 10)

    def test_repeated_talk_updates_current_state(self):
        character = Character("学姐", "测试角色", 0)
        for choice, expected in (("1", 5), ("1", 10), ("2", 5), ("x", 5)):
            self.talk(character, choice)
            self.assertEqual(character.affinity, expected)


class MenuTests(unittest.TestCase):
    def play(self, game, inputs, start=False):
        output = io.StringIO()
        exited = False
        with patch("builtins.input", side_effect=inputs), redirect_stdout(output):
            try:
                if start:
                    game.start()
                else:
                    game.story_loop()
            except SystemExit as exc:
                self.assertEqual(exc.code, 0)
                exited = True
        return output.getvalue(), exited

    def selected_game(self, affinity=0):
        game = campus.Game()
        game.current_target = game.characters["学姐"]
        game.current_target.affinity = affinity
        return game

    def test_view_current_affinity_and_quit(self):
        game = self.selected_game(12)
        output, exited = self.play(game, ["3", "4"])
        self.assertTrue(exited)
        self.assertIn("当前好感度：12", output)
        self.assertNotIn("无效输入", output)
        self.assertEqual(game.current_target.affinity, 12)

    def test_first_route_selection_chat_gift_view_and_quit(self):
        game = campus.Game()
        output, exited = self.play(game, ["1", "1", "1", "2", "奶茶", "3", "4"], start=True)
        self.assertTrue(exited)
        self.assertIs(game.current_target, game.characters["学姐"])
        self.assertEqual(game.current_target.affinity, 25)
        self.assertIn(campus.DIALOGUES["学姐"][0]["text"], output)
        self.assertIn("当前好感度：25", output)
        self.assertNotIn("无效输入", output)
        self.assertNotIn("【场景二", output)
        self.assertEqual(game.characters["小白"].affinity, 0)

    def test_invalid_menu_input_keeps_state_and_returns_to_menu(self):
        game = self.selected_game(12)
        output, exited = self.play(game, ["x", "3", "4"])
        self.assertTrue(exited)
        self.assertEqual(output.count("无效输入"), 1)
        self.assertIn("当前好感度：12", output)
        self.assertEqual(game.current_target.affinity, 12)

    def test_second_chat_option_and_unknown_gift_through_menu(self):
        game = self.selected_game()
        output, exited = self.play(game, ["1", "2", "2", "巧克力", "3", "4"])
        self.assertTrue(exited)
        self.assertEqual(game.current_target.affinity, -5)
        self.assertIn("当前好感度：-5", output)
        self.assertNotIn("无效输入", output)

    def test_gift_at_or_above_threshold_ends_route(self):
        for initial, gift, expected in ((90, "鲜花", 100), (95, "奶茶", 115)):
            with self.subTest(initial=initial, gift=gift):
                game = self.selected_game(initial)
                output, exited = self.play(game, ["2", gift, "4"])
                self.assertFalse(exited)
                self.assertEqual(game.current_target.affinity, expected)
                self.assertIn("进入了结局线", output)

    def test_below_threshold_continues_menu(self):
        game = self.selected_game(85)
        output, exited = self.play(game, ["2", "鲜花", "3", "4"])
        self.assertTrue(exited)
        self.assertEqual(game.current_target.affinity, 95)
        self.assertIn("当前好感度：95", output)
        self.assertNotIn("进入了结局线", output)

    def test_invalid_scene_input_retries_before_accepting(self):
        for invalid in ("9", "", "hello"):
            with self.subTest(invalid=invalid):
                game = campus.Game()
                output, exited = self.play(game, [invalid, "1", "3", "4"], start=True)
                self.assertTrue(exited)
                self.assertIs(game.current_target, game.characters["学姐"])
                self.assertEqual(game.current_target.affinity, 0)
                self.assertEqual(output.count("无效输入，请输入 1 或 2。"), 1)
                self.assertNotIn("【场景二", output)

    def test_invalid_scene_input_then_rejection_returns_false(self):
        game = campus.Game()
        output = io.StringIO()
        with patch("builtins.input", side_effect=["9", "2"]), redirect_stdout(output):
            selected = game.scene_senpai()
        self.assertIs(selected, False)
        self.assertIs(game.current_target, game.characters["None"])
        self.assertIn("无效输入，请输入 1 或 2。", output.getvalue())

    def test_repeated_invalid_scene_inputs_then_full_route(self):
        game = campus.Game()
        output, exited = self.play(game, ["9", "x", "1", "2", "奶茶", "3", "4"], start=True)
        self.assertTrue(exited)
        self.assertEqual(output.count("无效输入，请输入 1 或 2。"), 2)
        self.assertEqual(game.current_target.affinity, 20)
        self.assertIn("当前好感度：20", output)
        self.assertNotIn("【场景二", output)


    def test_xiaobai_selection_chat_gift_view_and_quit(self):
        game = campus.Game()
        output, exited = self.play(game, ["2", "1", "1", "1", "2", "编程笔记", "3", "4"], start=True)
        self.assertTrue(exited)
        self.assertIs(game.current_target, game.characters["小白"])
        self.assertEqual(game.current_target.affinity, 20)
        self.assertEqual(game.characters["学姐"].affinity, 0)
        self.assertIn(campus.DIALOGUES["小白"][0]["text"], output)
        self.assertIn("当前好感度：20", output)
        self.assertNotIn("【场景三", output)

    def test_invalid_xiaobai_input_retries_before_selection(self):
        for invalid in ("9", "", "hello"):
            with self.subTest(invalid=invalid):
                game = campus.Game()
                output, exited = self.play(game, ["2", invalid, "1", "3", "4"], start=True)
                self.assertTrue(exited)
                self.assertIs(game.current_target, game.characters["小白"])
                self.assertEqual(output.count("无效输入，请输入 1 或 2。"), 1)
                self.assertNotIn("【场景三", output)

    def test_xiaobai_invalid_input_then_rejection_returns_false(self):
        game = campus.Game()
        output = io.StringIO()
        with patch("builtins.input", side_effect=["9", "2"]), redirect_stdout(output):
            selected = game.scene_xiaobai()
        self.assertIs(selected, False)
        self.assertIs(game.current_target, game.characters["None"])
        self.assertIn("无效输入，请输入 1 或 2。", output.getvalue())

    def test_xiaobai_ending_does_not_offer_jiejie(self):
        game = campus.Game()
        game.characters["小白"].affinity = 85
        output, exited = self.play(game, ["2", "1", "2", "编程笔记"], start=True)
        self.assertFalse(exited)
        self.assertIs(game.current_target, game.characters["小白"])
        self.assertEqual(game.current_target.affinity, 100)
        self.assertIn("进入了结局线", output)
        self.assertNotIn("【场景三", output)


    def test_jiejie_selection_chat_gift_view_and_quit(self):
        game = campus.Game()
        output, exited = self.play(game, ["2", "2", "1", "1", "1", "2", "鲜花", "3", "4"], start=True)
        self.assertTrue(exited)
        self.assertIs(game.current_target, game.characters["姐姐"])
        self.assertEqual(game.current_target.affinity, 20)
        self.assertEqual(game.characters["学姐"].affinity, 0)
        self.assertEqual(game.characters["小白"].affinity, 0)
        self.assertIn(campus.DIALOGUES["姐姐"][0]["text"], output)
        self.assertIn("当前好感度：20", output)

    def test_invalid_jiejie_input_retries_before_selection(self):
        for invalid in ("9", "", "hello"):
            with self.subTest(invalid=invalid):
                game = campus.Game()
                output, exited = self.play(game, ["2", "2", invalid, "1", "3", "4"], start=True)
                self.assertTrue(exited)
                self.assertIs(game.current_target, game.characters["姐姐"])
                self.assertEqual(output.count("无效输入，请输入 1 或 2。"), 1)
                self.assertNotIn("眼前三妹子都不要", output)

    def test_all_three_rejections_end_without_selecting_a_role(self):
        game = campus.Game()
        output, exited = self.play(game, ["2", "2", "2"], start=True)
        self.assertFalse(exited)
        self.assertIs(game.current_target, game.characters["None"])
        self.assertIn("眼前三妹子都不要", output)
        self.assertNotIn("你要做什么", output)

    def test_jiejie_invalid_input_then_rejection_returns_false(self):
        game = campus.Game()
        output = io.StringIO()
        with patch("builtins.input", side_effect=["9", "2"]), redirect_stdout(output):
            selected = game.scene_jiejie()
        self.assertIs(selected, False)
        self.assertIs(game.current_target, game.characters["None"])
        self.assertIn("无效输入，请输入 1 或 2。", output.getvalue())

    def test_jiejie_ending_returns_to_start_without_rejection_message(self):
        game = campus.Game()
        game.characters["姐姐"].affinity = 85
        output, exited = self.play(game, ["2", "2", "1", "2", "鲜花"], start=True)
        self.assertFalse(exited)
        self.assertIs(game.current_target, game.characters["姐姐"])
        self.assertEqual(game.current_target.affinity, 100)
        self.assertIn("进入了结局线", output)
        self.assertNotIn("眼前三妹子都不要", output)


if __name__ == "__main__":
    unittest.main()
