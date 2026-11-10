"""校园 if 启动入口，并保留原文件的类和数据导入接口。"""

from character import Character
from game import Game
from story import DIALOGUES, GIFT_EFFECTS


if __name__ == "__main__":
    game = Game()
    game.start()
