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
- 这些是基础知识练习，尚未回填校园模板，不代表模板送礼功能已经完成。

## 后续必做待补

Class、`self`、对象属性、Magic Methods、OOP、`re`、列表推导式、Type Hint、generator/`yield`。
学会对应基础后再回填实际模板；完整笔记最终由本人复核、补充自己的理解。
