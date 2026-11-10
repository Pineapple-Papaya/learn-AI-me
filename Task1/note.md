# python

> 本文件对应 Foundation 1“文档 1”，是正式学习笔记；速查表只是辅助资料。
> 新增部分根据本人在对话中的回答与错误，由 Codex 辅助整理，供本人复核。
> 模板位置和未完成项见 [Task1 任务入口](README.md)，未学内容不预填为已掌握。

## 字符编码

Unicode 是字符标准，不是某一种固定字节数的存储方式；实际字节数取决于所用编码。
现代 UTF-8 使用 1–4 个字节编码一个 Unicode 标量值；ASCII 范围字符用 1 个字节，
常见汉字通常用 3 个字节。不能笼统地说 Unicode 存英文一定比 ASCII 多一倍。

## List列表

[]
可变有序表
append()加末尾
insert()加特定位置
pop()删特定位置
元素数据类型可不同

## tuple

()
初始化后不能修改  更安全

## 模式匹配

match case  case _表示其他所有情况

## dict

 d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
 字典的 key 必须可哈希。字符串、整数通常可作为 key；list 不能直接作为 key。

## set

无序性
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
通过remove(key)方法可以删除元素

## 函数

定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
定义函数：要可变参数就必须写`*`
调用函数：传零散数字不用`*`；传列表元组要拆开，才加`*`

### 关键字参数 `**kw`

- 定义：`**kw`，函数内部 `kw` 是一个 **dict 字典**
- 作用：接收任意多个 `key=value` 形式的关键字实参
- 和`*numbers`区别：`*`打包成 tuple；`**`打包成 dict

```python
def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
```

输出：

```text
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
`*` 之后，Python **不再接收无名的位置实参**  必须写key=value
`*args` 解包元组
`**kw` 解包字典
要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

## 递归函数

在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数.

## 函数输入、打印与返回

- 调用 `total(4, 6)` 时，实参 4、6 分别交给函数的形参。
- `print()` 显示内容，`return` 把结果交给调用者；显示内容不等于返回值。
- 没有执行 `return` 的函数默认返回 `None`。
- 执行 `return` 后当前函数立即结束，后面的语句不再执行。

本人的实际错误：曾把只打印结果的函数也判断为返回 `5`；讲解后补对 `return a + b`，
并正确判断 `return` 后的打印不执行。

## Lambda 与排序规则

Lambda 的写法是 `lambda 参数: 返回表达式`，适合只有一个返回表达式的小函数。

本人已写出的例子：

```python
add_ten = lambda x: x + 10
print(add_ten(5))  # 15
```

排序规则的完整例子：

```python
students = [("Tom", 80), ("Jerry", 95), ("Alice", 70)]
result = sorted(students, key=lambda student: student[1])
print(result)
```

`sorted()` 逐个取出列表元素，传给 `key` 指定的函数，用它的返回值作为排序依据，
返回排好序的完整记录。`student` 是当前一条记录；`student[1]` 取得这条记录的成绩。

## Decorator 装饰器基础

装饰器接收原函数，返回包装函数。定义时完成包装，之后调用装饰后的函数，
执行包装函数，再由它调用保存的原函数。

```python
def with_log(func):
    def first():
        print("开始执行")
        func()
        print("执行结束")
    return first

@with_log
def study():
    print("学习 Python")

study()
```

此处 `@with_log` 等价于定义之后执行 `study = with_log(study)`。
`return first` 属于外层 `with_log`，与 `def first()` 对齐。
本人曾把它写进内部函数，导致外层没有返回包装函数；这部分已针对性讲解，示例辅助运行通过。

## Day 2 已做的基础练习

- `.get(键, 默认值)` 查询一个键，找不到时返回默认值；不是一次传入多个候选键。
- 完整上下文是先定义礼物字典，再用 `gift = input(...)` 保存输入，最后查询 `effects.get(gift, 0)`。
- 本人正确判断：礼物“巧克力”不在示例字典时，默认结果为 `0`。
- 本人已写对 `affinity += change` 与 `affinity >= 100`。
- 已回填个人校园模板的 `give_gift`、首条对话及主交互循环。

## Class、实例、属性与 self

`class Character` 定义角色对象的数据和操作。调用类创建实例时，Python 会调用 `__init__` 初始化。
`self` 是当前对象，由 Python 自动传入；`self.name`、`self.affinity` 是对象自己的属性。

以下结构来自校园模板，底部是课堂使用的完整调用：

```python
class Character:
    def __init__(self, name, role, affinity=0):
        self.name = name
        self.role = role
        self.affinity = affinity

    def change_affinity(self, value):
        self.affinity += value

xiaobai = Character("小白", "课堂上的元气同学", 10)
xiaobai.change_affinity(20)
xiaobai.change_affinity(-10)
print(xiaobai.affinity)  # 20
```

本人正确判断：省略初始好感度时使用默认值 `0`；连续修改时使用当前状态，最终为 `20`。

## 嵌套字典与通用效果

原模板的 `GIFT_EFFECTS` 是两层字典：外层按礼物查询，内层按角色查询。
`"default"` 只是普通字符串键，不会自动生效，必须先读取再传给角色查询作为默认值。

```python
GIFT_EFFECTS = {
    "鲜花": {"学姐": 10, "小白": 10, "姐姐": 15},
    "奇怪的石头": {"default": -10},
}
gift = "奇怪的石头"
character_name = "学姐"
gift_data = GIFT_EFFECTS.get(gift, {})
default_value = gift_data.get("default", 0)
value = gift_data.get(character_name, default_value)
print(value)  # -10
```

本人正确判断鲜花对姐姐为 `15`、石头对学姐使用通用值 `-10`。

## 调用当前对象的方法

在 `give_gift` 内部，应写 `self.change_affinity(value)`。
Python 会把当前对象作为第一个参数 `self`，把 `value` 作为第二个参数。
不能把类中的方法当成未定义的全局函数，直接写 `change_affinity(self, value)`。

模板中的 `change_affinity` 用于修改对象状态，没有 `return`，默认返回 `None`。
因此不需要 `value = self.change_affinity(value)`，否则局部变量 `value` 会变成 `None`。
本人礼物查询这一行写对；方法调用这一行经讲解修正，本轮不计为独立完成。

## 对话列表与条件分支

原模板 `DIALOGUES` 的外层字典按角色查询，得到对话列表；`dialogues[0]` 取第一条对话字典，
再用 `dialogue["text"]`、`dialogue["optionA"]`、`dialogue["optionB"]` 取台词和选项。
`if not dialogues` 判断列表为空；此时提前 `return`，避免访问不存在的第一条。

`input()` 返回字符串，因此使用 `choice == "1"` 判断。
`if / elif / else` 从上到下判断，执行第一个匹配的分支；都不匹配时执行 `else`。
本轮约定选 1 加 5、选 2 减 5、其他输入只提示，不改好感度；这是个人实现选择。

本人独立写对上述三个分支，评分 10/10；取对话、空列表保护和显示部分由讲解提供。
当前每次使用角色的第一条对话，不声称已完成按次数切换剧情。

## 游戏对象、角色对象与菜单调用

### 重点：类、对象与 self 的关系

> **`self` 指向当前调用这个实例方法的对象，不是类本身，也不是所有方法共享的固定对象。**

`Game`、`Character` 是类；`game = Game()` 创建游戏对象，`Character(...)` 创建角色对象。
类定义有哪些数据和操作，对象保存自己的具体数据。两个角色来自同一个类，也有各自的名字和好感度。

| 所在方法 | 本次调用中 `self` 指向谁 |
| --- | --- |
| `game.story_loop()` 所进入的方法 | 游戏对象 `game` |
| 小白对象调用的 `talk()` | 小白对象 |
| 姐姐对象调用的 `talk()` | 姐姐对象 |

> **`self.current_target` 是游戏对象的普通属性，其中保存着当前角色对象。**

```text
游戏对象 game（Game 创建）
    └── current_target → 姐姐对象（Character 创建）
                            ├── name = "姐姐"
                            └── affinity = 0
```

在游戏的 `story_loop` 中，`self.current_target.talk()` 的读取顺序是：
找到当前游戏 → 找到游戏保存的角色 → 调用该角色的聊天方法。
进入角色的 `talk` 后，它自己的 `self` 就指向这个角色；方法间同名的参数互不影响。

> **先找方法定义在哪个类，再找持有该方法的对象，最后用“对象.方法()”调用。**

| 在 `Game` 方法内要做的事 | 调用写法 |
| --- | --- |
| 打开游戏主菜单 | `self.story_loop()` |
| 让当前角色聊天 | `self.current_target.talk()` |
| 给当前角色送礼 | `self.current_target.give_gift(gift)` |
| 检查当前角色结局 | `self.current_target.check_ending()` |

本人曾把 `self` 说成“类本身”，后经讲解正确回答：`game.story_loop()` 中的 `self` 是 `game` 对象。
姐姐分支的三行本人全部写对，10/10；这是当前具体场景的正确应用，不等于整个 OOP 已独立掌握。

姐姐接受分支内的代码如下，依赖已有 `Game` 方法上下文，不是独立脚本：

```text
self.current_target = self.characters["姐姐"]
self.story_loop()
return True
```

三行分别表示：选中姐姐对象 → 运行游戏主菜单 → 主菜单正常返回后，告诉调用方已选择角色。
**`return True` 表示已选择角色；`check_ending()` 判断是否达到结局，两者含义不同。**

### 菜单调用与当时的易错记录

在 `Game.story_loop()` 中，`self` 是游戏对象；`self.current_target` 是选中的角色对象。
因此分别用 `self.current_target.talk()`、`self.current_target.give_gift(gift)` 调用角色方法，
用 `self.current_target.affinity` 读取角色属性。

变量不需要变成类；它保存某个类创建的对象，就可以通过该对象调用实例方法。
`target = self.current_target` 让两个位置指向同一个角色，不复制角色，也不会丢失角色的方法。
调用 `target.talk()` 时，Python 自动把 `target` 对应的角色传给 `talk` 的 `self`。

本人首次把游戏对象当成角色，三处接收对象均需修正，评分 4/10。
经对象与类、变量引用的讲解后表示理解；主菜单由讲解后回填，尚不计独立掌握。

`while True` 重复显示菜单；`break` 结束当前循环，原模板 `sys.exit(0)` 直接结束程序。
所有菜单选项应放在同一组 `if / elif / else` 中，避免有效操作后又被独立的 `else` 提示无效。
菜单每轮读取一次输入；送礼或聊天时，进入对应方法或分支后还会读取一次具体选择。

## 无效输入与循环控制

学姐入口使用 `while True` 反复询问，用 `choice not in ("1", "2")` 检查输入不在允许选项中。
输错时提示并执行 `continue`，跳过本轮后面的角色选择，回到下一轮 `input()`。
若误用 `break`，会退出循环；这个方法循环后没有其他代码，会结束方法并默认返回 `None`。

| 语句 | 作用范围与效果 |
| --- | --- |
| `continue` | 跳过当前这一轮剩余代码，进入下一轮循环 |
| `break` | 结束当前这一层循环，继续执行循环后面的代码 |
| `return True` / `return False` | 结束整个方法，把选择结果返回给调用方 |
| `sys.exit(0)` | 在本作业正常运行时结束程序，状态码为 0 |

本人首次选择 `break`，该题 0/1；讲解后改为 `continue`，属于纠正后完成，不算独立迁移通过。
下一次先复测对象接收者与循环跳转，不因为代码通过测试就宣称已经独立掌握。

## 选择路线的返回值与结局判断

小白路线本人写对 `self.current_target = self.characters["小白"]`，
但将菜单误写为 `self.current_target.story_loop()`，将选择结果误写为 `self.current_target.check_ending()`。
本题评分 4/10；后两行经讲解修正，属于指导完成。

`story_loop` 定义在 `Game` 中，游戏方法内应调用 `self.story_loop()`。
`talk`、`give_gift` 和 `check_ending` 定义在 `Character` 中，
在游戏方法内使用 `self.current_target` 调用它们。

`scene_xiaobai` 返回 `True` 表示玩家已经选中小白；好感度为 0 也可以选择她。
`check_ending()` 判断好感度是否达到 100，其返回值含义不同。
仅调用它不会代替当前方法的 `return`。
菜单结束后应使用 `return True`，让 `start` 跳过姐姐入口；明确拒绝时用 `return False`。

## 模块与 import：拆文件第一步

**一个 `.py` 文件通常就是一个模块。导入时使用模块名，不加 `.py`。**
`from story import GIFT_EFFECTS` 表示从同目录 `story.py` 中导入礼物效果表。
本人正确写出这一行，10/10；随后正确写出 `from character import Character`，导入类练习也是 10/10。

原模板的两张完整数据表已移入 `Task1/Campus_IF_Love/story.py`。
角色模块顶部使用以下语句，逗号分隔表示一次导入两个名字：

```text
from story import DIALOGUES, GIFT_EFFECTS
```

**导入类只是让当前文件可以使用这个类；调用 `Character(...)` 才会创建角色对象。**
`character.py` 保存角色类，`game.py` 使用 `from character import Character` 导入后创建角色。
原 `Campus_IF_Love.py` 保留启动入口，以及之前使用过的类和数据导入名字。

| 文件 | 职责 |
| --- | --- |
| `story.py` | 完整对话与礼物数据 |
| `character.py` | `Character`，角色数据与操作 |
| `game.py` | `Game`，角色选择与主菜单 |
| `Campus_IF_Love.py` | 启动游戏，并保留已有导入接口 |

已分两次移动角色类和游戏类，每次移动后 30/30 回归通过，方法体核对不变。
实际启动也覆盖三条路线和全部拒绝；单独导入各模块不启动游戏、不询问输入。
文件结构要求已完成；类型注释与检查随后完成，见下节。结构验收和行为验收分别核对。

## Type Hint：参数与返回值的类型

**`参数名: 类型` 说明参数类型，`-> 类型` 说明返回值类型。**
类型注释用于阅读和静态检查，不会自动把传入的字符串转换为整数。

| 类型 | 本作业中的含义 |
| --- | --- |
| `str` | 角色名、角色介绍、礼物名称 |
| `int` | 好感度与本次增减值 |
| `bool` | 是否选择角色、是否达到结局 |
| `None` | 方法执行操作，没有返回业务结果 |

本人正确填出 `int`、`None`，10/10。对应的实际方法签名是：

```text
def change_affinity(self, value: int) -> None:
```

**修改好感度是修改对象状态；没有返回新分数，因此返回类型是 `None`，不是 `int`。**
`affinity: int = 0` 表示参数为整数，默认值为 0。通常不需要额外标注实例方法的 `self`。
`give_gift(self, gift: str) -> None` 接收礼物名；`check_ending(self) -> bool` 返回判断结果。

两个类的全部 11 个方法已补注释，助手检查其余签名，不把这部分全部记成本人独立完成。
mypy 2.4.1 的严格检查覆盖 4 个业务文件，结果为无问题；30/30 功能回归继续通过。
另用错误调用验证：传字符串给 `change_affinity(value: int)` 时，检查工具能指出参数类型错误。

## 后续必做待补

Class、`self`、对象属性已讲基本用法，继续通过模板实作巩固。
Magic Methods、完整 OOP、`re`、列表推导式、generator/`yield` 仍待补齐。
Type Hint 的本次基础应用已讲，后续仍需练习容器类型和独立迁移，不能认为全部进阶类型知识已掌握。
学会对应基础后再回填实际模板；完整笔记最终由本人复核、补充自己的理解。
