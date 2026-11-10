# Day 1 一页速查

> 2026-11-09，根据今天实际练习整理，供本人核对和复习。
> 娜比娅个人理解验收安排在 Day 4，今天不追加。

## 赋值与索引

- 字符串拼接使用当时的值；之后给原变量重新赋值，不会重算已经拼好的字符串。
- 列表索引从 0 开始，题目编号从 1 开始：学长 `u` 对应 `names[u - 1]`。
- 学长改名只更新当前记录，使用目标人物当时的名字，不建立自动跟随关系。

## Lambda 与排序

- `lambda 参数: 表达式` 创建小函数，表达式的值就是返回值。
- 例：`add_ten = lambda x: x + 10`。
- `key` 接收排序规则函数。`sorted()` 逐个传入元素，用规则的返回值排序，返回完整元素组成的新列表。
- 学生成绩排序：`sorted(students, key=lambda student: student[1])`。
- `students[1]` 是第二条学生记录；函数中的 `student[1]` 是当前这条记录的成绩。

## 函数调用与返回

- 形参接收调用时的实参；例如 `total(4, 6)` 中，4、6 分别交给形参 `a`、`b`。
- 函数名可以作为值传递；加括号才是调用，例如 `func` 与 `func()`。
- `print()` 将内容显示到屏幕；`return` 将结果交给调用者。
- 没有执行 `return` 的函数默认返回 `None`，不能把打印内容当成返回值。
- 执行 `return` 后当前函数立即结束，后面的语句不再执行。

## 装饰器基础

装饰器接收原函数，返回包装函数。`@with_log` 等价于定义后执行 `study = with_log(study)`。
定义时包装一次；之后调用 `study()`，执行包装函数，它再调用保存的原函数。

```python
def with_log(func):
    def wrapper():
        print("开始执行")
        func()
        print("执行结束")
    return wrapper

@with_log
def study():
    print("学习 Python")

study()
```

`return wrapper` 与 `def wrapper()` 对齐，属于外层函数。放错层级会让外层默认返回 `None`。

## 运行环境

解释器决定由哪个 Python 执行代码；工作目录决定相对路径从哪里开始找。
本项目使用已安装的 Python 3.12.3；终端默认 `python` 目前指向 Anaconda 3.13.9，未修改全局配置。

```powershell
Set-Location -LiteralPath "C:\Users\Allen\Desktop\learn-AI-me"
& "C:\Users\Allen\AppData\Local\Programs\Python\Python312\python.exe" `
    "Task0\作业4\name_updates.py"
```

## 今天的真实易错点

- 学长编号没有减 1：已修正，并通过两个官方样例与六组边界自测。
- `return wrapper` 放进了内部函数：已讲解修正，完整例子辅助运行通过。
- 把 `print` 的输出当成函数返回值：讲解后补对 `return a + b`。
- 最后一道变式正确判断输出为 `10`，没有执行 `return` 后的打印。
