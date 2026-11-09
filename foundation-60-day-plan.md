# Foundation 60 天学习计划

> 起始日期：2026-09-30  
> 结束日期：2026-11-28  
> 上游基准：`west2-online/learn-AI` `main` 分支，提交 `da32e4329a2c7204182b5eb206a65dae44cc48ff`  
> 目标：完成 2026 Foundation 的可验收交付物，同时建立能独立读题、调试、测试和解释代码的能力。

## 先说结论

仓库给 Foundation Task 0–3 的标注总时长是 115 天。压缩到 60 天不是轻松路线，按每天 1 小时基本不现实。建议每周投入至少 20 小时：普通日 2.5–3 小时，项目整合日 4 小时；每 7 天允许 1 天只做复盘和补欠账。

本计划优先保证必做内容可验收，再做对录取最有帮助的 Bonus。Task 1 选择“校园·if 恋 + 宝可梦对战”，因为二者组合能覆盖多文件拆分、Type Hint、文件读写、状态管理、继承、组合和 OOP 设计。Task 3 官方允许自由选择完成程度，本计划完成作业 1、2，并把作业 4 做成加分项。

## 你的当前起点

### 已具备

- Python 3.12.3、Git、uv、VS Code 已安装。
- `Hello, World!` 已完成。
- 旧版要求中的 4 道 OJ 已有代码。
- 已完成 Task 0 Bonus 1、2。
- 已开始整理 Python 笔记，并写出了 Task 1 作业 1 的前两个函数雏形。

### 现在必须修正

- 上游 Task 0 已新增第 5 道 OI 题：学长改名模拟题，当前尚未完成。
- `Task0/作业2/crazy-day.md` 中存在占位图片、错误链接语法和未闭合括号，不能视为通过 Markdown 验收。
- `Task0/作业4/Bonus/1.3.py` 是空文件。
- Task 1 作业 1 当前官方要求在 `longmen_vs_nabia.py` 中完成 12 个函数，并运行 `check_my_code.py`；现有 `Task1/作业1.py` 不能替代官方框架。
- Task 1 笔记仍缺 Lambda、Decorator、Class、Magic Methods、OOP、`re`、列表推导式、Type Hint、generator 与 `yield`。
- Git 当前有一个已删除的根目录 `crazy-day.md` 和未跟踪的 `Task1/`。这是你的现有改动，本计划不替你提交或清理。

## 每天固定学习方式

每次学习按下面四段进行：

1. 15 分钟：不看笔记，口述昨天学了什么，并写一个最小例子。
2. 40–50 分钟：只看当天对应的官方文档或任务文档。
3. 90–120 分钟：独立编码。先写伪代码，再写实现，不先向 AI 索取完整答案。
4. 20–30 分钟：运行测试、记录错误、更新笔记和当天完成证据。

卡住时执行“20 分钟规则”：先读完整报错，定位第一个属于自己代码的栈帧，构造最小复现，查官方文档；仍未解决再提问。提问时必须附上目标、代码、完整报错、已尝试方案和预期结果。

使用 AI 时遵守三条：先让 AI 给思路或测试用例；拿到代码后逐行解释；关闭对话后能从空文件重新写出核心逻辑。答辩不能解释的代码等同于没完成。

## 60 天日程

| Day | 日期 | 当天主题 | 必须留下的成果 |
| ---: | :---: | --- | --- |
| 1 | 09-30 | 对照最新版 Task 0，检查环境、目录和 Git 状态；修复 `crazy-day.md` 的链接、图片和格式 | Markdown 预览正常；列出 Task 0 未完成项 |
| 2 | 10-01 | 完成最新版新增的第 5 道 OI 题；先手算两个样例再编码 | 程序通过题目样例；写出时间复杂度 |
| 3 | 10-02 | 给已有 5 道 OI 题补边界测试并统一代码风格 | 每题至少 3 组自测；能解释每个循环边界 |
| 4 | 10-03 | 完成 Bonus 1.3、1.4，并运行 Markdown lint；整理 Task 0 README | Task 0 达到可验收状态 |
| 5 | 10-04 | List、Dict、Set、Tuple：增删改查、切片、排序、复制与可变性 | 20 个小例子；补笔记中的对比表 |
| 6 | 10-05 | 函数：参数、返回值、作用域、异常、Lambda、列表推导式 | 完成 Bonus 1.6；为函数写类型注释 |
| 7 | 10-06 | 文件读写、`pathlib`、JSON、异常处理 | 写一个读写 JSON 的小程序；记录 3 类异常 |
| 8 | 10-07 | Class：实例、类属性、封装、继承、组合 | 完成 Bonus 商品类；画出对象关系 |
| 9 | 10-08 | Magic Methods 与 OOP 设计 | 完成 `MyZoo`；解释 `__init__`、`__str__`、`__eq__`、`__len__` |
| 10 | 10-09 | Decorator、闭包、generator、`yield` | 各写 2 个可运行例子并补入笔记 |
| 11 | 10-10 | `re` 正则、Type Hint、Pylance；完成密码正则 Bonus | Pylance 无明显类型错误；写出正则测试表 |
| 12 | 10-11 | 获取官方娜比娅作业框架，阅读 README 与检查器，不急着写 | 列出 12 个函数的输入、输出、异常和边界 |
| 13 | 10-12 | 完成纯计算函数：骰子、攻击、防御、暴击、最终伤害 | 对每个函数做正常值、边界值、非法值测试 |
| 14 | 10-13 | 完成状态函数：行动选择、扣血、结束判断、结果判断 | `check_my_code.py` 对应检查通过 |
| 15 | 10-14 | 完成主战斗循环；控制随机调用次数与最大回合数 | 全部自动检查通过；游戏可完整结束 |
| 16 | 10-15 | 复盘娜比娅作业；重构命名和重复逻辑 | 能脱稿讲清调用链；记录 3 个 bug 的根因 |
| 17 | 10-16 | 阅读“校园·if 恋”剧情、README 和现有代码 | 状态字段、角色、操作和结局流程图 |
| 18 | 10-17 | 设计多文件结构和 Type Hint；实现 `talk()` | 程序能展示第一段完整对话 |
| 19 | 10-18 | 实现 `give_gift()`、输入校验和第一角色分支 | 第一角色从开始到结局可玩 |
| 20 | 10-19 | 实现第二、第三角色和好感度边界 | 三条分支可玩；好感度不会非法越界 |
| 21 | 10-20 | 增加 JSON 存档/读档 Bonus | 关闭程序后能恢复进度；坏存档有清晰提示 |
| 22 | 10-21 | 校园项目测试、README、类型检查和重构 | 全流程测试表；Pylance 通过；README 可复现 |
| 23 | 10-22 | 宝可梦需求拆解；区分“宝可梦、属性、技能、状态、队伍、战斗” | 类图和战斗时序图；确定模块边界 |
| 24 | 10-23 | 实现 `Pokemon` 基类、属性克制与伤害计算 | 用固定随机种子验证克制、抗性和闪避 |
| 25 | 10-24 | 实现技能抽象和状态效果基类 | 至少完成中毒、烧伤、麻痹、护盾 |
| 26 | 10-25 | 实现 4 只指定宝可梦 | 每只两个技能；基础单元测试通过 |
| 27 | 10-26 | 自行设计第 5 只宝可梦；实现草、火、水、电被动 | 被动效果有独立测试，避免写成大段 `if` |
| 28 | 10-27 | 实现队伍选择、换人、电脑随机选择与战斗循环 | 3v3 命令行完整跑通一次 |
| 29 | 10-28 | 宝可梦边界测试和重构 | 昏厥、蓄力、连续状态、全队失败均正确 |
| 30 | 10-29 | 完成 Task 1 两份文档、项目 README、类型检查与模拟答辩 | Task 1 可验收；10 个答辩问题及答案 |
| 31 | 10-30 | HTTP 基础：URL、GET、状态码、请求头、Cookie、HTML、JSON | 用 DevTools 找到一个页面请求并解释各字段 |
| 32 | 10-31 | `requests`、超时、`raise_for_status()`、编码、Beautiful Soup/XPath | 抓一个练习页并输出 3 个字段 |
| 33 | 11-01 | CSV、日志、重试、限速、去重、断点续爬设计 | 可复用的请求与增量保存函数；异常测试 |
| 34 | 11-02 | 教务通知：分析列表页、分页规律和详情页结构 | 抓取 10 条通知的最小原型 |
| 35 | 11-03 | 教务通知：抓通知人、标题、日期、详情链接和正文 | 抓取 50 条并抽查 10 条准确性 |
| 36 | 11-04 | 教务通知：用 Network 找附件 Ajax 请求 | 抓到附件名、下载次数和链接码 |
| 37 | 11-05 | 教务通知：加入断点、失败重试、去重和文本清洗 | 中断后重启不会丢失或重复数据 |
| 38 | 11-06 | 教务通知：完成至少 500 条；字段与质量检查 | CSV、数据字典、错误日志、运行 README |
| 39 | 11-07 | Pandas：读取、筛选、缺失值、重复值、`groupby` | 对教务 CSV 输出基础质量报告 |
| 40 | 11-08 | 教务分析 Notebook：通知人、课程调整、下载关系、时间高峰 | Notebook 有代码、图表、文字结论和导出 CSV |
| 41 | 11-09 | Open-Meteo：读 API 文档，先在纸上设计一次请求 | 一次请求取回全年全部小时/日变量并保存 CSV |
| 42 | 11-10 | 开源之夏：用 Network 找 JSON 接口并解析 | 项目名、难度、标签、简述、产出要求 CSV |
| 43 | 11-11 | Selenium：定位器、显式等待、滚动、页面结构 | 在练习页完成打开、定位、滚动、取文本 |
| 44 | 11-12 | 知乎：人工登录与 Cookie 本地保存；设计数据结构 | Cookie 加入 `.gitignore`；抓 1 个问题原型 |
| 45 | 11-13 | 知乎：抓问题名、正文和回答纯文本 | 抓 5 个问题，每题 10 个回答 |
| 46 | 11-14 | 知乎：扩展到 20 个问题并增强等待、重试和断点 | 最终 CSV；随机抽查 20 条文本 |
| 47 | 11-15 | NumPy：shape、dtype、切片、布尔索引、原地操作 | 完成作业 3.1，不使用多余循环 |
| 48 | 11-16 | NumPy 广播、`axis` 和向量化距离 | 完成作业 3.2；手算验证一个距离 |
| 49 | 11-17 | Matplotlib 与 Logistic 函数 | 标准曲线和参数对比图；图例、单位、结论齐全 |
| 50 | 11-18 | Task 2 总验收：从空环境按 README 运行 | 4 个爬虫、3 个数据作业可复现；隐私文件未跟踪 |
| 51 | 11-19 | 模型压力测试：5 个指定问题分别新对话 | 保存回答，标注逻辑、幻觉、角色与常识问题 |
| 52 | 11-20 | Colab、Transformers Pipeline；零样本分类实验 | 自选文本和 3–4 个标签，保存概率并评价准确性 |
| 53 | 11-21 | BERT 填空实验：改变上下文对概率的影响 | 两组以上对照；解释概率变化而非只贴截图 |
| 54 | 11-22 | Qwen2.5-0.5B-Instruct：修改 system/user 消息 | 代码、输出、对照实验和 system prompt 解释 |
| 55 | 11-23 | Vibe Coding TODO：先让 AI 产出需求表、数据表与 API 清单 | 审核后的方案、完整对话记录、隔离项目环境 |
| 56 | 11-24 | TODO：生成并跑通 FastAPI、逻辑删除和 Vue3 前端 | 增改查删可用；被删除数据不再被操作 |
| 57 | 11-25 | TODO：运行 API 测试，修复幻觉，完成反思文档 | 测试全过；README 能部署；记录错误与修正提示词 |
| 58 | 11-26 | 全仓库干净环境验证：依赖、命令、路径、README、敏感信息 | 从空虚拟环境复现；所有入口命令有记录 |
| 59 | 11-27 | 模拟答辩：随机抽 3 个项目，口述后现场改一个需求 | 30 个问答；列出仍不理解的代码并补齐 |
| 60 | 11-28 | 缓冲与最终整理；只修阻塞问题，不临时扩功能 | Foundation 交付清单、演示顺序、后续分流决定 |

## 每阶段验收门槛

### Task 0

- Markdown 预览正确并通过基础 lint。
- 当前上游要求的 5 道 OI 题都有 Accepted 或等价验证。
- 能解释 PATH、解释器、终端工作目录、全局环境与虚拟环境。
- 至少完成 4 个真正能解释的 Bonus，而不是只留下代码。

### Task 1

- 娜比娅官方检查器全部通过，游戏能稳定结束。
- “校园·if 恋”和“宝可梦对战”均能从 README 启动。
- 两个项目有合理多文件结构、Type Hint 和输入错误处理。
- 笔记覆盖官方要求全部主题，每个主题都有自己的最小例子。
- 终端复盘能解释 IDE 运行按钮实际调用了什么命令、解释器和工作目录。

### Task 2

- 爬虫 1–4 和数据分析 1–3 全部完成；若负责人确认有选做规则，再缩减。
- 教务数据至少 500 条，支持断点续爬，附件动态字段来自 Ajax 接口。
- 知乎达到 20 个问题 × 每题 10 个回答；Cookie 不进入 Git。
- Open-Meteo 只发一次业务请求，单位、时区和缺失值处理有说明。
- Notebook 不只是代码截图，必须包含结论、图表和数据质量说明。

### Task 3

- 至少完整完成作业 1、2，能解释“概率生成、幻觉、上下文、system prompt”。
- 作业 4 作为加分项，但只有实际跑通、测试通过、对话记录完整才算完成。
- 能指出 AI 生成代码中至少 3 个真实问题，并说明自己如何验证与修复。

## 精选资料

只选主线资料，不同时刷多个教程。

### 任务原文

- [Foundation Task 0](https://github.com/west2-online/learn-AI/blob/main/tasks%282026%29/foundation/task0.md)
- [Foundation Task 1](https://github.com/west2-online/learn-AI/blob/main/tasks%282026%29/foundation/task1.md)
- [Foundation Task 2](https://github.com/west2-online/learn-AI/blob/main/tasks%282026%29/foundation/task2.md)
- [Foundation Task 3](https://github.com/west2-online/learn-AI/blob/main/tasks%282026%29/foundation/task3.md)

### Python 与工程习惯

- [Python 官方中文教程](https://docs.python.org/zh-cn/3.12/tutorial/)
- [Python 类与生成器](https://docs.python.org/zh-cn/3.12/tutorial/classes.html)
- [Python `typing` 文档](https://docs.python.org/zh-cn/3.12/library/typing.html)
- [Python `re` 文档](https://docs.python.org/zh-cn/3.12/library/re.html)
- [PEP 8](https://peps.python.org/pep-0008/)
- [CS61A](https://www.cs61a.org/)：属于长期 Bonus，不挤占前 50 天主线；进度领先时每周做 1 个 Lab。

### 爬虫与数据

- [Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Beautiful Soup 文档](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Chrome DevTools Network](https://developer.chrome.com/docs/devtools/network/overview)
- [Selenium 等待策略](https://www.selenium.dev/documentation/webdriver/waits/)
- [Pandas 入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [NumPy 初学者指南](https://numpy.org/doc/stable/user/absolute_beginners)
- [Matplotlib 教程](https://matplotlib.org/stable/tutorials/index)
- [Open-Meteo 历史天气 API](https://open-meteo.com/en/docs/historical-weather-api)

### AI 入门实验

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)
- [Transformers Pipeline 教程](https://huggingface.co/docs/transformers/main/pipeline_tutorial)
- [Google Colab](https://colab.research.google.com/)

## 每日汇报模板

每天结束时只记录下面五项，控制在 10 分钟内：

```markdown
## Day N - YYYY-MM-DD

- 今日完成：
- 今日产物：文件路径 / 测试结果 / 截图
- 最难的问题：
- 我如何定位并解决：
- 明日第一步：
```

向我请求帮助时，直接发送当天编号、当前文件和完整报错。我会优先做三件事：先确认题意与验收口径，再给最小知识补充，最后用测试和追问帮助你自己完成；不会直接替你生成一份你无法答辩的作业。

## 进度失速时怎么处理

- 落后 1–2 天：使用下一次复盘日补，不增加新 Bonus。
- 落后 3–5 天：保留所有必做；暂停 Task 0 额外 Bonus 和 CS61A。
- 落后超过 5 天：校园项目只做要求内功能，不做存档 Bonus；Task 3 作业 4 移到 Foundation 验收之后。
- 不通过删除测试、压缩文档或复制 AI 代码来“追进度”。这些做法会在答辩时集中暴露。

