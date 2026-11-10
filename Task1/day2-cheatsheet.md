# Day 2 一页速查：对象、状态与循环

## 从对象找到操作

| 写法 | 含义 |
| --- | --- |
| `Character(...)` | 根据类创建角色对象 |
| `target = senpai` | 两个变量指向同一个对象，不复制角色 |
| `target.talk()` | 调用角色方法；Python 自动传入角色作为 `self` |
| `self.current_target` | 在 `Game` 的方法里，取得当前角色 |
| `self.current_target.affinity` | 读取当前角色的好感度 |
| `self.current_target.change_affinity(10)` | 把当前角色好感度增加 10 |

**`self` 指向调用当前实例方法的对象，不是类本身。**
在 `Game` 方法里是游戏对象；在 `Character` 方法里，是调用该方法的角色对象。
**`self.current_target` 是游戏保存的角色对象；游戏主菜单用 `self.story_loop()` 调用。**
接受角色后 `return True` 表示已选中；`check_ending()` 判断好感度是否达到 100，含义不同。

模块导入：`from character import Character` 导入类，`Character(...)` 才创建对象。
类型注释：`value: int` 表示整数参数；`-> None` 表示执行操作但没有返回业务结果。

## 字典和列表取数据

| 写法 | 含义 |
| --- | --- |
| `data.get(key, fallback)` | 找到键就返回对应值，否则返回默认值 |
| `gift_data.get("default", 0)` | 显式取通用效果；`"default"` 只是普通键 |
| `gift_data.get(self.name, default_value)` | 优先取角色专属效果 |
| `dialogues[0]` | 取对话列表的第一条，先检查列表非空 |
| `dialogue["text"]` | 从这条对话字典取台词 |

## 输入与流程控制

`input()` 返回字符串，用 `choice == "1"` 判断；多分支写为同一组 `if / elif / else`。
`choice not in ("1", "2")` 检查无效选项；无效输入不改变角色状态。

| 语句 | 动作 |
| --- | --- |
| `continue` | 跳过本轮剩余代码，下一轮重新询问 |
| `break` | 退出当前循环 |
| `return` | 结束整个函数或方法 |
| `sys.exit(0)` | 正常运行本作业时结束程序 |

## 今日易错点与验证办法

- 角色操作要从 `self.current_target` 开始；不要对 `Game` 直接调用角色方法。
- `change_affinity` 直接修改状态，没有返回新分数；不要把它的返回值赋给 `value`。
- 输错后重问使用 `continue`；本人首次误选 `break`，经讲解纠正。
- 跟踪“初始值 → 操作增减 → 最终值”，检查正常、无效、零值、负值和结局边界。
- 运行测试：在个人校园目录执行 `python -m unittest -v`，使用 Python 3.12.3。

原定 Day 2 完成学姐路线；本人追加继续后，三条基础路线均已接通。
姐姐接受分支三行本人写对；其余指导完成的部分仍需巩固，不据此认定 OOP 全部掌握。
