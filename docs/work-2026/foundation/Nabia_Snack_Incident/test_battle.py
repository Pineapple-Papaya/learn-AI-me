"""当前作业的语法和边界回归测试；运行 python -m unittest -v。"""

from contextlib import redirect_stdout
import io
from pathlib import Path
import random
import re
import unittest
from unittest.mock import patch

import longmen_vs_nabiya as battle


class BattleSyntaxTests(unittest.TestCase):
    def test_assignment_can_be_compiled(self):
        path = Path(__file__).with_name("longmen_vs_nabiya.py")
        try:
            compile(path.read_text(encoding="utf-8-sig"), str(path), "exec")
        except SyntaxError as error:
            self.fail(f"作业存在语法错误：第 {error.lineno} 行，{error.msg}")


class BattleRegressionTests(unittest.TestCase):
    def run_battle(self, **kwargs):
        output = io.StringIO()
        with redirect_stdout(output):
            result = battle.main_battle_loop(**kwargs)
        return result, output.getvalue()

    def test_display_clamps_hp_to_valid_range(self):
        for hp, expected in [(-5, 0), (80, 80), (200, 115)]:
            with self.subTest(hp=hp):
                output = io.StringIO()
                with redirect_stdout(output):
                    battle.display_status("长门", hp, 115)
                self.assertEqual(output.getvalue(), f"[长门]HP: {expected} / 115\n")

    def test_display_rejects_nonpositive_max_hp(self):
        for maximum in [0, -1]:
            with self.subTest(maximum=maximum), self.assertRaises(ValueError):
                battle.display_status("长门", 10, maximum)

    def test_zero_dice_returns_zero_without_random_draw(self):
        with patch.object(battle.random, "randint", side_effect=AssertionError("零骰子不应产生随机点数")):
            self.assertEqual(battle.roll_dice(0), 0)

    def test_both_alive_is_a_draw(self):
        self.assertEqual(battle.get_battle_result(115, 105), "draw")

    def test_loop_rejects_invalid_parameters(self):
        for kwargs in [{"pause_seconds": -0.1}, {"max_turns": 0}, {"max_turns": -1}]:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.run_battle(**kwargs)

    def test_nagato_critical_hit_can_end_first_turn(self):
        with patch.object(battle, "NABIYA_MAX_HP", 36), patch.object(battle.random, "randint", return_value=6):
            result, _ = self.run_battle(max_turns=1)
        self.assertEqual(result, "nagato")

    def test_nabiya_does_not_receive_nagato_critical_bonus(self):
        # 长门 HP=20 时防御 12 点；娜比娅攻击 18 点，长门应存活。
        with patch.object(battle, "NAGATO_MAX_HP", 20), patch.object(battle.random, "randint", return_value=6):
            result, _ = self.run_battle(max_turns=1)
        self.assertEqual(result, "draw")

    def test_special_success_probability_boundary(self):
        for chance, expected in [(0.449, "nagato"), (0.45, "draw"), (1.0, "draw")]:
            with self.subTest(chance=chance), patch.object(battle, "NABIYA_MAX_HP", 1), patch.object(
                battle.random, "random", return_value=chance
            ), patch.object(battle.random, "randint", return_value=6):
                result, _ = self.run_battle(max_turns=1)
                self.assertEqual(result, expected)

    def test_special_damage_respects_previous_enemy_defense(self):
        # 第 1 回合特殊攻击失败，娜比娅防御 12；第 2 回合 24-12=12，剩 6 HP。
        with patch.object(battle, "NABIYA_MAX_HP", 18), patch.object(
            battle.random, "random", side_effect=[1.0, 0.0, 1.0]
        ), patch.object(battle.random, "randint", return_value=6):
            result, output = self.run_battle(max_turns=3)
        self.assertEqual(result, "draw")
        self.assertIn("[娜比娅]HP: 6 / 18", output)

    def test_enemy_does_not_act_after_being_defeated(self):
        with patch.object(battle, "NABIYA_MAX_HP", 1), patch.object(
            battle.random, "random", return_value=0.0
        ), patch.object(battle.random, "randint", side_effect=AssertionError("战斗结束后敌人不应掷骰")):
            result, _ = self.run_battle(max_turns=1)
        self.assertEqual(result, "nagato")

    def test_zero_pause_does_not_sleep(self):
        with patch("time.sleep", side_effect=AssertionError("无暂停战斗不应休眠")), patch.object(
            battle.random, "randint", return_value=1
        ):
            result, output = self.run_battle(max_turns=2)
        self.assertEqual(result, "draw")
        self.assertIn("第 2 回合", output)
        self.assertNotIn("第 3 回合", output)

    def test_positive_pause_uses_requested_duration(self):
        durations = []
        with patch("time.sleep", side_effect=durations.append), patch.object(
            battle.random, "randint", return_value=1
        ):
            self.run_battle(pause_seconds=0.25, max_turns=2)
        self.assertTrue(durations)
        self.assertTrue(all(duration == 0.25 for duration in durations))

    def test_seeded_games_finish_with_valid_hp_and_turn_limit(self):
        state = random.getstate()
        self.addCleanup(random.setstate, state)
        for seed in range(20):
            with self.subTest(seed=seed):
                random.seed(seed)
                result, output = self.run_battle(max_turns=50)
                self.assertIn(result, {"nagato", "nabiya", "draw"})
                turns = re.findall(r"第 (\d+) 回合", output)
                self.assertTrue(turns)
                self.assertLessEqual(int(turns[-1]), 50)
                for hp, maximum in re.findall(r"HP: (-?\d+) / (\d+)", output):
                    self.assertGreaterEqual(int(hp), 0)
                    self.assertLessEqual(int(hp), int(maximum))


if __name__ == "__main__":
    unittest.main()
