"""校园 if 角色的数据与交互方法。"""

from story import DIALOGUES, GIFT_EFFECTS


class Character:
    def __init__(self, name: str, role: str, affinity: int = 0) -> None:
        self.name = name
        self.role = role
        self.affinity = affinity

    def talk(self) -> None:
        print(f"你正在和{self.name}对话...")
        dialogues = DIALOGUES.get(self.name, [])
        if not dialogues:
            print("暂时没有可用对话。")
            return

        dialogue = dialogues[0]
        print(f"{self.name}：{dialogue['text']}")
        print("1.", dialogue["optionA"])
        print("2.", dialogue["optionB"])
        choice = input("请选择：")

        if choice == "1":
            self.change_affinity(5)
        elif choice == "2":
            self.change_affinity(-5)
        else:
            print("无效选择")

    def give_gift(self, gift: str) -> None:
        print(f"你送给 {self.name} 一份 {gift}。")
        gift_data = GIFT_EFFECTS.get(gift, {})
        default_value = gift_data.get("default", 0)
        value = gift_data.get(self.name, default_value)
        self.change_affinity(value)

    def change_affinity(self, value: int) -> None:
        self.affinity += value
        print(f"{self.name} 的好感度变化 {value} -> 当前好感度：{self.affinity}")

    def check_ending(self) -> bool:
        if self.affinity >= 100:
            print(f"恭喜！你和 {self.name} 的故事进入了结局线！")
            return True
        return False
