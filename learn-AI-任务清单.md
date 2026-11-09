# west2-online learn-AI 2026 任务清单

> 整理基准：仓库 `main` 分支，提交 `df3040bbf2c4e8f5f61c2573fbc3f6e15244f331`，提交时间 2026-08-29 15:43 +08:00。
>
> 当前有效路线以 `README.md` 和 `tasks(2026)` 为准。`pre-tasks/tasks(2023-2025)` 是历史归档，不应当作为 2026 必做清单。

## 一、先看结论

你需要先完成共同基础阶段 Foundation，然后在两条主线中二选一：

```text
Foundation Task 0 -> Task 1 -> Task 2 -> Task 3 -> Task 4 分流
                                                  |
                         +------------------------+------------------------+
                         |                                                 |
                 Scientific Research                                Application
                 Research 1 -> 2 -> 3                Application 0 -> 1 -> 2 -> 3 -> 4
```

- 想保研、进实验室、复现论文：选 Scientific Research。
- 想做工程、产品、Agent：选 Application，但 Application 0 是工程能力门槛。
- 仓库明确提醒：纯 AI 应用对本科就业并不稳妥，建议同时学习 Go/Java 后端、运维，并了解前端。
- 如果已有基础，可面谈申请跳过 Foundation Task 0、1、3；Task 2 与分流任务原则上仍要完成。
- 如果往年已通过部分考核，从尚未通过的阶段继续。
- 只完成最低要求通常不够稳。README 明确说，想进入工作室还需要适量 Bonus，答辩也会检查知识储备。

文档标注的预计耗时按顺序相加：

| 路线 | 标注耗时 | 说明 |
| --- | ---: | --- |
| Foundation | 115 天 | Task 0/1/2/3 分别为 10/45/45/15 天；Task 4 是导引 |
| Application | 150 天 | 30 + 15 + 15 + 30 + 60 天 |
| Research | 至少 150 天 | Research 1 为 90 天，Research 2 标 60 天但尚无任务，Research 3 待补充 |
| Foundation + Application | 约 265 天 | 不含 Bonus、返工、答辩准备 |
| Foundation + Research | 至少约 265 天 | Research 2/3 尚未写完整，真实耗时不可确定 |

## 二、开始前必须做好

### 1. 账号与工具

- GitHub 账号。
- Edge 或 Chrome。
- Python 3.12.3。仓库不建议直接用 3.13/3.14，以免 AI 框架兼容性不足。
- VS Code + Python/Pylance，或 PyCharm。
- Git、终端、Markdown 预览和 markdownlint。
- 建议安装 `uv` 管理虚拟环境；早期可用 `venv`。
- 能使用 Google、Colab、Hugging Face 等站点；需要自行处理网络访问。
- 没有 NVIDIA GPU 不影响 Foundation，可用 Colab/云 GPU。Research 和 Application 3 的训练任务再考虑算力。

### 2. 建立自己的作业仓库

建议建一个 `learn-ai-<github-username>` 仓库，按阶段组织：

```text
learn-ai-username/
├─ foundation/
│  ├─ task0/
│  ├─ task1/
│  ├─ task2/
│  └─ task3/
├─ application/              # 或 research/
├─ docs/
├─ .gitignore
└─ README.md
```

每个独立作业至少包含：

- `README.md`：功能、环境、运行方法、目录树、已知限制。
- 源码和必要配置。
- 依赖声明，如 `pyproject.toml`/`uv.lock` 或 `requirements.txt`。
- 测试或最小可复现脚本。
- 对应笔记、实验报告、截图、图表。
- `.gitignore`，忽略 `.env`、密钥、Cookie、数据库、数据集、模型权重、虚拟环境、缓存和 IDE 配置。

### 3. Git 与提交约束

- 自己的仓库用于代码审查。
- 还要向 `west2-online-reserve/collection-ai` 提 PR，仅用于留档。
- 每个作业按“最小可运行子集”提交，不要最后一次性塞进一个巨大 commit。
- 推荐英文 commit 前缀：`feat:`、`fix:`、`docs:`、`style:`、`refactor:`、`test:`、`chore:`。
- GitHub 建议单文件不超过 50MB，100MB 以上无法普通上传。数据集、模型、爬虫结果等大文件应忽略，并用网盘/数据源链接说明。
- 禁止抄袭。允许使用 AI，但必须理解、能复现、能解释每一行关键代码；引用 AI 生成部分时建议注明来源。

## 三、Foundation 共同基础阶段

## Task 0：环境搭建与 Python 入门（预计 10 天）

### 必做交付物

1. 完成开发环境：Python、IDE、终端、Git、GitHub、Markdown。
2. 创建个人 GitHub 作业仓库。
3. 提交 `crazy-day.md`，内容自拟，但必须含：
   - 多级标题；
   - 图片；
   - 链接；
   - 代码块；
   - 表格。
4. Markdown 通过基本 markdownlint，并满足：
   - 中文与英文之间加空格；
   - 中文与数字之间加空格；
   - 数字与单位之间不加空格，如 `8GB`；
   - 中文语境使用全角标点，英文/代码使用半角标点。
5. `Hello, World!` 程序，输出必须精确匹配。
6. 用 Python 完成 4 道 OJ：
   - 洛谷 P1001；
   - 洛谷 P1046；
   - 洛谷 P5737；
   - AtCoder ARC017A。

### Bonus

基础题 8 项：三数排序、九九乘法表、字符串替换倒序、列表过滤排序、字典删偶数学号、数字频次统计、商品类、斗地主发牌写入 4 个文件。

进阶题 5 项：计时装饰器、有序斗地主发牌、矩阵转置列表推导式、实现含多个魔术方法的 `MyZoo`、密码正则校验。

### 验收标准

- 能从终端执行 `python your_script.py`，理解 IDE 运行按钮实际执行的命令、工作目录和解释器。
- 能解释 PATH、全局环境、虚拟环境、依赖安装位置。
- 不用手机拍屏；提问时能提供源码、完整报错、截图和复现步骤。

## Task 1：语法基础与简单面向对象（预计 45 天）

### 总体规则

- 文档 1、文档 2 都要完成。
- 作业 1 必做。
- 作业 2、3、4 至少选择两个。
- 作业 2–4 必须使用 Type Hint，并通过 Pylance 或同等静态检查。
- 作业 1–3 可以 clone 官方仓库取得框架，不需要 fork。

### 文档 1：Python 学习笔记

用 Markdown 或 Jupyter Notebook，以自己的理解覆盖：

- List、Dict；
- Lambda、Decorator；
- Class、Magic Methods、OOP 思想；
- `re` 正则表达式；
- 列表推导式、Type Hint；
- generator 与 `yield`。

禁止整篇交给 AI 代写。答辩时必须能举例解释。

### 文档 2：终端复盘

在完成所选代码作业后再写，内容包括：

- 作业中碰到的终端问题；
- 如何定位并解决；
- VS Code/PyCharm 右上角运行三角形究竟做了什么。

### 作业 1：娜比娅偷吃事件（必做）

按配套 README、starter 和 `check_my_code.py` 完成 12 个函数：

1. `display_status`
2. `roll_dice`
3. `choose_nagato_action`
4. `calculate_attack_damage`
5. `calculate_defense_value`
6. `check_critical_hit`
7. `nabiya_ai_action`
8. `calculate_final_damage`
9. `apply_damage`
10. `is_battle_over`
11. `get_battle_result`
12. `main_battle_loop`

运行：

```powershell
python check_my_code.py
python start_the_battle.py
```

验收重点：边界值、非法参数抛 `ValueError`、骰子随机调用次数、暴击、防御仅消费一回合、HP 不低于 0、最大回合数、确定性测试可结束。

### 作业 2：校园 if 恋（择做）

- 阅读剧情文件。
- 完成 `talk()`、`give_gift()`、第二/第三角色分支、玩家交互循环。
- 好感度达到 100 解锁结局。
- 合理拆分为至少 3 个 `.py` 文件。
- 全面补 Type Hint。
- 完成后写问题与解决过程文档；如果确实没有问题，可不写。
- Bonus：存档、读档、即时存档；建议 JSON 化状态并设计剧情索引。

### 作业 3：宝可梦命令行对战（择做）

- 玩家选 3 只，电脑随机选 3 只；对战中选择出战宝可梦和技能。
- 实现草/火/水/电克制、抗性及各自被动。
- 实现指定 4 只：皮卡丘、妙蛙种子、杰尼龟、小火龙。
- 至少再自行设计 1 只。
- 实现每只宝可梦的两个技能及中毒、烧伤、麻痹、护盾、蓄力等效果。
- 避免重复：建议 `Pokemon` 基类 -> 属性类 -> 具体宝可梦类；技能和状态效果单独模块。
- 提交玩法 `README.md`，使用 Type Hint，并确保命令行完整可玩。
- 官方示例只实现妙蛙种子，且代码中的 `GlassPokemon` 实际意图是 `GrassPokemon`；它是参考框架，不是完整答案。

### 作业 4：自拟 OOP 小项目（择做）

- 自己设计结构完整、功能清晰、可运行的小项目。
- 必须使用 Class、Magic Methods 等 OOP 思想。
- 合理拆分多文件。
- 可参考三国杀 Demo、视频转文字工具、Galgame 引擎，但不要只做空壳。

### 长期 Bonus：CS61A

- 完成 CS61A 课程、作业和 lab。
- 不要求在 Task 1 当轮完成，但仓库建议在整个 Foundation 结束前完成。

## Task 2：网络爬虫与数据分析（预计 45 天）

文档没有写“任选”规则。按字面，除明确标为 Bonus 的内容外，爬虫 1–4 和数据分析 1–3 都应视为必做；正式开工前最好向当年负责人确认工作量口径。

### 爬虫作业 1：福大教务通知

- 至少爬 500 条通知，越多越好。
- 字段：通知人、标题、日期、详情链接、正文、附件名、附件下载次数、附件链接码。
- 清洗回车、括号等无用符号。
- 保存 CSV。
- 附件下载次数属于动态数据，必须抓 Ajax 接口，不能用 Selenium 代替。
- 设计断点/增量保存，避免网络中断后全部重爬。
- Bonus：下载附件。

交付建议：`crawler.py`、原始/清洗 CSV 字段说明、失败重试与断点策略、运行 README。

### 爬虫作业 2：Selenium 爬知乎话题

- 选 1 个话题。
- 爬 20 个问题，每题 10 个回答。
- CSV 字段至少含问题名、问题正文、回答纯文本。
- Bonus：从话题广场扩展、保存评论。
- 可扫码登录并把 Cookie 保存为 JSON，但 Cookie 必须加入 `.gitignore`，不得提交。

### 爬虫作业 3：抓接口爬开源之夏 2025

- 用 DevTools Network 找到项目列表接口。
- 用 `requests`/同类库请求 JSON，不能只解析页面 HTML。
- 提取项目名、难度、技术领域标签、项目简述、项目产出要求。
- Bonus：下载项目申请书 PDF。

### 爬虫作业 4：Open-Meteo

- 只允许发起一次请求。
- 地点：福州大学旗山校区，经纬度 `119.198, 26.05942`。
- 时间：2024-01 至 2024-12。
- 保存逐小时 10 个变量：温度、相对湿度、体感温度、降水、天气代码、总云量、10m 风速、10m 风向、即时短波辐射、昼夜标记。
- 保存逐日 5 个变量：平均/最高/最低温、总降水、日照时长。
- 输出 CSV，并说明单位、时区和缺失值处理。

### 爬虫 Bonus：B-Wiki API

- 用 MediaWiki API 获取“方案舰娘”分类下全部页面，保留原始数据即可。
- 每次请求间隔至少 1 秒，`maxlag=5`，服务器繁忙最长等待 5 秒后放弃。
- 禁止并发请求，避免封 IP。

### 数据分析作业 1：教务通知分析（Jupyter）

- 必须使用 Jupyter Notebook 同时呈现代码、结果和文字分析。
- 统计通知人及各自占比。
- 筛出“课程调整”通知，统计数量与内容并另存 CSV。
- 分析附件下载次数与通知人的关系。
- 按日统计发布量，识别学期高峰期。
- 自拟 1 个探索问题。
- 至少把课程调整和附件下载关系相关结果可视化。

### 数据分析作业 2：Logistic 函数

- 绘制 `L=1, k=1, x0=0` 的标准 Logistic 曲线。
- 对比多个 `L`、`k`、`x0`，用图例/文字说明参数如何改变曲线。

### 数据分析作业 3：NumPy

基础矩阵：

- 创建 `0..99` 的 `(10, 10)` 数组。
- 提取中心 `(4, 4)` 子矩阵。
- 用布尔索引把大于 75 的值置零，禁止显式循环。
- 原地乘 `0.8`。
- 求最大值及其二维索引。

广播距离：

- 随机生成 `(5, 2)` 的 `points_A` 与 `(8, 2)` 的 `points_B`。
- 无显式循环计算 `(5, 8)` 欧氏距离矩阵。
- 求 A 中每个点到 B 的最小距离。
- 找出与任一 A 点距离小于 20 的 B 点索引。

Bonus 图像数组：灰度转 RGB、矩阵乘法 Sepia、向量化过饱和、左右 20px 渐变边框、Matplotlib 对比展示。

## Task 3：简单 AI 认识（预计 15 天）

此阶段被仓库定义为科普，并写明“可自由选择完成至什么程度”。它不是严格的全做任务，但答辩会检查你是否真正理解 AI 的局限、概率生成、提示词与 Vibe Coding 风险。

### 作业 1：模型压力测试

- 注册 DeepSeek，开深度思考、关闭联网。
- 5 个指定问题分别新建对话：对象位置、角色扮演、虚假演唱会信息、50 米洗车、竹竿过门。
- 记录推理、角色风格、幻觉和常识错误。
- 可横向对比其他模型。

### 作业 2：3 个 Hugging Face 实验 + 理解文档

- Colab 安装 `transformers torch accelerate`。
- 零样本分类：替换成自己的句子和 3–4 个标签，记录概率和准确性判断。
- BERT 填空：改变上下文，比较前 5 个 token 概率变化并解释原因。
- Qwen2.5-0.5B-Instruct：改 system/user 消息，记录代码、输出并解释 system prompt 的作用。
- 最终提交一篇自己的理解文档和必要截图。

### 作业 3：女娲 Skill

- 使用 `nuwa-skill` 思路蒸馏一个人物人格；人物可自行选择。
- 不应只交生成结果，还应能说明资料来源、人格规则和验证方法。

### 作业 4：Vibe Coding TODO LIST

- 只使用 AI/提示词完成 FastAPI + 数据表 + Vue3。
- 增：新增事项。
- 改：单条/全部完成、单条/全部恢复待办、按 id 修改标签。
- 查：全部/待办/完成分页，关键词分页，id 查询，标签分页。
- 删：单条/全部完成/全部待办/全部事项，全部使用逻辑删除。
- 已逻辑删除数据不能被查到或被后续改、删影响。
- API 路径语义清晰，尽量 RESTful，统一 JSON 返回。
- 所有生成物只能存在项目目录，不能污染全局环境。
- 提交 README、接口文档、AI 完整对话链接/Markdown、API 测试脚本，并亲自跑通。
- 再写反思文档，回答 AI/使用形式、幻觉与提示词修正、可维护性、与官方 `Memo-Codex5.5` 对比、能否按 README 部署、弱模型 API 能否完成。

官方 `Memo-Codex5.5` 是用于对比的示例，不是让你直接提交。它包含 FastAPI + SQLModel + SQLite、Vue3 CDN 页面、接口测试和部署 README。

## Task 4：选择方向

Task 4 没有代码作业，核心任务是做职业/学习方向决策：

- Research：理论、模型、论文复现，依赖数学基础、导师和实验室资源。
- Application：工程化调用模型、RAG、Agent/Harness；同时补后端、运维、前端。
- 附属目录 Backend/Frontend/Statistic 不是 2026 主线必做考核。

## 四、Scientific Research 路线

## Research 1：从机器学习到深度学习（预计 90 天）

### 前置知识

- 多元函数求导、偏导、矩阵求导。
- 线性代数。
- NumPy 向量化。
- Python。
- 环境优先 Colab 或 Linux/WSL2；大量 I/O 时不要把 WSL 项目放在 `/mnt/c`/`/mnt/d`。

### 必做内容

仓库写的是“5 篇文档 + 作业 1–3”。5 篇实际组成是两篇专题文档，加上每个作业各一篇复盘报告。

1. 文档：用自己的话说明生成式 AI 的 Pre-training、SFT、RLHF。
2. 文档：解释 k-NN、SVM、Softmax、XGBoost、Random Forest 的原理、场景，以及它们与神经网络的区别。
3. CS231n Assignment 1：从零实现线性分类器/两层神经网络，理解损失、梯度下降、反向传播，并写复盘。
4. CS231n Assignment 2：CNN、现代深度学习框架/PyTorch，并写复盘。
5. 第三阶段方向作业并写复盘：
   - CV：CS231n Assignment 3；
   - NLP/LLM：CS224n，文档建议先做前三个 assignment。

仓库同一段先写“完成 CS231n A3、完成 CS224n”，后文又说二选一；建议按“方向二选一”为最低口径，但在开始前向负责人确认。本科生被建议两个方向都体验，福大实验室侧更偏 CV。

传统树模型只要求理解并会用 scikit-learn；k-NN/SVM/Softmax 是理解损失与梯度的基础，需要在 CS231n 作业中实现。

## Research 2：Idea（标注 60 天）

当前文件只有标题、预计耗时和“后续调整”说明，没有学习内容、作业或验收标准。现在无法形成可靠任务清单，等仓库更新或直接询问负责人。

## Research 3：进实验室介绍

当前只有“待补充”，没有可执行任务。

## 五、Application 路线

## Application 0：TikTok Demo 工程门槛（预计 30 天）

如果已完成后端/客户端考核，或已有符合工程规范的项目，可申请面谈免做。否则必须先完成它才能继续 Application。

### 最低接口

| 模块 | 接口 |
| --- | --- |
| 用户 | 注册、登录、用户信息 |
| 视频 | 投稿、发布列表、搜索视频 |
| 互动 | 视频点赞、点赞列表、视频评论、评论列表、删除评论 |
| 社交 | 关注操作、关注列表、粉丝列表 |

### 硬要求

- Python + FastAPI 或 Flask，采用三层架构。
- 数据库 CRUD 与合理表设计，提交 SQL 建表语句。
- 分页参数 `page_num`/`page_size` 正确生效。
- 视频搜索的全部条件都要满足。
- 只能删除自己的评论。
- 双 Token（通常是 access/refresh）机制。
- 投稿接收文件并保存本地即可，无需分片和分布式存储。
- 点赞只要求视频，不要求评论点赞；关注不要求 WebSocket。
- 提供目录树、README 和 API 文档。
- 严禁 Vibe Coding；允许适量 AI 辅助，但你必须主导架构与实现。

## Application 1：AI 应用认知（预计 15 天）

### 文档 1：底层认知

阅读 Karpathy 从零构建 GPT、nanoGPT、Illustrated Transformer、指定科普博客；Bonus 阅读 Attention Is All You Need。写理解文档。

### 作业 1：机器学习/深度学习对比

- 完成 2025 电工杯第 2 题。
- 使用 `uv`。
- 处理原始数据。
- 在 SVM、XGBoost、Random Forest、CNN、RNN、Transformer、LSTM 中至少选 3 个，其中必须含你认定的最优解，做对比分析。
- 文档还要概述上述所有方法的原理，并说明对比结论和问题。

### 作业 2：YOLO 项目

- 自拟一个基于 YOLO 的单机游戏自动化项目，例如自动通关 PVZ 1-10。
- 不能只调用 YOLO 已有类别做一个识别 Demo；需要形成自动化闭环或训练/适配自己的检测能力。

### 作业 3：现代 LLM 思想

- 阅读 PyTorch 入门、Hugging Face LLM Course、Transformers 文档。
- 理解 Pipeline、Transformer 与基本推理参数。
- 写理解文档，并能独立完成类似 Foundation Task 3 的本地模型 Pipeline 实验。

## Application 2：大语言模型简单应用（预计 15 天）

### 作业 1：QQ 情绪表情包

- 调用智谱 GLM 4.0，仅通过 API + Prompt 分析最近 x 条文本/图片/表情。
- 使用有视觉能力的模型。
- 输出严格限制为“开心/难过/愤怒/中性”之一。
- 按标签随机发送对应表情包。
- 使用 `openai` SDK、`uv`、`.gitignore` 保护密钥。

### 作业 2：调课通知解析器

- 输入 Foundation Task 2 筛出的调课通知 CSV。
- 调用合适模型转成 `from_date`/`to_date` JSON 规则。
- 设计 Prompt 并做严格格式校验。
- 用真实通知验证正确性。
- 使用 `openai` SDK 和 `uv`。

### 作业 3：实时会议转写、总结、思维导图

- Whisper small 实时转写，保留原始文本。
- 配置 Chat Model 做实时总结。
- 前处理加入降噪；后处理修复 Whisper 错字漏字。
- 输出原文、实时总结、Mermaid 思维导图三块内容。
- 最终结果必须渲染，不接受只生成未展示的文本。
- 可先做离线版验证，但最终提交必须实时。

## Application 3：进阶应用（预计 30 天）

### 作业 1：MiniMind LoRA 微调

- 准备本地 NVIDIA GPU 或 AutoDL/Colab/OpenDL；远程训练建议 VS Code Remote。
- 阅读 MiniMind README 和 LoRA 部分。
- 获得医疗 LoRA 适配器和身份 LoRA 适配器。
- 组合两个适配器，得到兼具身份与医疗知识的模型。
- 本地测试身份、创造者、医疗知识、医疗建议、组合问题、非医疗边界能力。
- 写训练/微调过程、挑战、最终测试报告。
- Bonus：从 0 训练、用 SwanLab/W&B 展示 Loss、用 PEFT 重写 LoRA 脚本。

### 作业 2：番茄助手 RAG

本地阶段：

- 爬笔趣阁总榜 10 页，至少含标题、简介、作者、标签，尽量保留正文。
- 建立向量数据库和 naiveRAG。
- 本地部署约 1B 模型，用 LangChain 构建工作流。
- 增加并比较 LightRAG、ReActRAG、GraphRAG。
- 设计更合理的 chunking 和 Prompt 策略。

云测试阶段：

- 部署到含 RTX 3090 的云服务器。
- 模型升级到 7B–10B，例如 Qwen 3.5-9B。
- 使用恶意 Prompt 数据集做攻击测试，并确保输出合法。

交付：能运行的推荐助手、无检索结果时不编造、技术说明文档。Bonus 为 LangChain/Dify 双实现和完整前后端。

### 作业 3：生产化扩展（明确不要求）

可继续研究量化/蒸馏、vLLM/TGI、Tracing/Prometheus/Grafana/ELK、安全过滤、无感升级、Nginx/Kong、Docker/Kubernetes。

## Application 4：Agent/Harness（预计 60 天）

### 作业 1：Agent Learning

- 学完 `learn-claude-code` s01–s20。
- 理解从基础循环、工具调用到更完整 Harness 的演进。
- 教程为教学使用单脚本；你要思考真实项目如何拆分模块，而不是照抄一个单文件 Demo。

### 作业 2：Agent 大作品

- 自己设计 Agent 架构并落地，语言/框架不限，推荐 Python + LangChain/LangGraph。
- 必须是结构化、可维护、可运行的项目。
- 答辩重点是架构选择、遇到的问题、验证方法和解决过程。

参考题：

- 多 Agent 长篇小说：多个 Agent 真正协作，并约束设定一致性。
- 游戏陪玩：多模态实时获取游戏信息，实时聊天、操作反馈和赛后评价。
- 多 Agent 狼人杀：语音；预言家 1、女巫 1、狼人 2、平民 2；支持 `x` 个人 + `y` 个 Agent 且 `x+y=6`；实现完整胜负规则。

Bonus 阅读：ReAct、CAMEL、AutoGen、MemGPT、mem0。

## 六、附属路线，不是主线强制作业

### Backend Routine

- Python 后端用于快速原型，不建议作为主要就业技术栈。
- 可自测 To-Do、TikTok、微服务、部署监控，但“不要求提交”。
- 推荐真正想做后端的人学习 Go/Java，并掌握 REST、JWT、ORM、路由拆分、异常处理、文件上传、日志、Redis、pytest、Docker 和部署。

### Frontend Routine

- Gradio/Streamlit 用于 AI 原型演示。
- 可用它们完成前端相关练习，但“不强制提交”。
- 专业前端仍建议学习 JavaScript/TypeScript 主流技术栈。

### Statistic Routine

- 数学建模速成路线：爬虫、Pandas/Matplotlib、数据挖掘、评价/规划/预测模型、蒙特卡罗/粒子群、传统 ML/DL。
- 两项均不强制：参加一次电工杯/国赛/美赛；参加一次非 Titanic 示例的 Kaggle 比赛。
- 文档后半是比赛经验：组队、选题、审题、论文结构、误差/敏感性、摘要、数据、图表、排版、AI 使用。可作为参赛手册，不是额外考核任务。

## 七、答辩与时间节点

仓库只写月份，没有写具体年份和硬 DDL；应以当年群通知为准。

| 阶段 | 仓库预计时间 | 形式 |
| --- | --- | --- |
| Foundation Task 0–3 | 1 月初至 1 月中 | 直接问源码，不用 PPT |
| Research 1 | 5 月初 | PPT/文档讲 10–15 分钟 + 提问 |
| Research 2 | 6 月中下旬 | PPT/文档讲 10–15 分钟 + 提问 |
| Application 0–1 | 3 月中旬 | PPT/文档讲 10–15 分钟 + 提问 |
| Application 2–3 | 5 月初 | PPT/文档讲 10–15 分钟 + 提问 |
| Application 4 | 6 月中下旬 | PPT/文档讲 10–15 分钟 + 提问 |

- 可提前申请单独答辩，公开到考核群，至少 3 人提问。
- 错过阶段可顺延到下一轮或申请单独答辩。
- 8 月有兜底答辩；再错过需等下一年纳新。

## 八、推荐执行顺序

### 第一阶段：7–10 天内把仓库和环境立住

1. 建 GitHub 仓库、README、`.gitignore`、目录。
2. 安装 Python 3.12.3、Git、VS Code/Pylance、`uv`。
3. 完成 `crazy-day.md`、Hello World、4 道 OJ。
4. 每完成一个最小功能就 commit。

### 第二阶段：Task 1 不要一上来做大项目

1. 先写 Python 语法笔记。
2. 完成娜比娅 12 函数，每个函数写完立即跑检查器。
3. 从校园 if 恋/宝可梦/自拟项目中选两个；时间紧时建议校园 if 恋 + 自拟小项目，想练 OOP 深度则选宝可梦。
4. 最后补终端复盘文档。

### 第三阶段：Task 2 让数据链条贯通

1. 先做教务爬虫，直接为后续分析和 Application 2 调课解析生产数据。
2. 再做 Open-Meteo，快速掌握 API 和 JSON/CSV。
3. 再做开源之夏抓包；最后做知乎 Selenium。
4. 用教务 CSV 完成 Jupyter 分析。
5. 再完成 Logistic 与 NumPy 向量化。

### 第四阶段：Task 3 重点做理解和复盘

1. 完成模型压力测试与 3 个 Pipeline 实验。
2. 至少挑 Vibe Coding TODO 或人物 Skill 中一个做完整。
3. 不要把官方 Memo 示例当答案；对比架构和维护性。

### 第五阶段：尽早分流

- Research：先补数学，再按 CS231n A1 -> A2 -> CV/NLP 分流推进。
- Application：先证明自己能独立完成 Application 0，再进入 AI 任务；不要反过来先堆 LangChain。

## 九、仓库中的歧义与坑

1. Foundation Task 1 总文档说娜比娅“8 个函数”，但 2026 配套 README、starter 和检查器已升级为 12 个。应以 12 个和检查器为准。
2. Foundation Task 2 没写作业选择数量。除 Bonus 外应先按全做规划，再向负责人确认。
3. Foundation Task 3 明确说可自由选择完成程度，因此不能把 4 个作业武断认定为全部强制。
4. Research 1 同时出现“CS231n A3 和 CS224n 都完成”与“可选择 CV 或 NLP”。最低口径需负责人确认。
5. Research 2/3 尚未编写完成，无法提前做完整计划。
6. Application 4 的说明把 LangChain/RAG 称为“作业 3”，实际应指 Application 3，是文字引用错误。
7. 官方 `Memo-Codex5.5/AI_CONVERSATION.md` 称 TODO 为“作业 3”，但 2026 `task3.md` 中它实际是作业 4。
8. Statistic 文档中的部分交叉引用沿用旧编号；数据工具当前主要在 Foundation Task 2。
9. 文档和任务可能随 AI 发展动态更新。每开始一个大阶段前，应同步上游并查看该阶段文件的 Git diff。

## 十、历史归档怎么处理

- 2023：Python 基础、爬虫、MNIST，随后分 CV/NLP，包含 YOLO、模型训练和云服务器资料。
- 2024：合并为环境/Python/OOP、爬虫/Pandas，再转 CS231n/CS224n。
- 2025：Task 1–3 为 Python/爬虫/数据分析，Task 4–6 为机器学习/深度学习/CV 或 LLM，Task 7–10 再细分现代工具、应用/科研、部署运维和前沿主题。
- 2026：重构为 Foundation + Research/Application，Application 更偏 Agent/Harness，Research 任务目前只完整写到 Research 1。

历史目录可用于找旧题、示例和扩展方向，但 2026 作业要求发生过改动，不能直接复制旧答案。维护规范也明确将 `pre-tasks` 排除在当前默认检查范围之外。

## 十一、每次提交前自查

- [ ] 项目能在一个全新虚拟环境按 README 跑起来。
- [ ] 没有提交 `.env`、API Key、Token、Cookie、数据库、数据集、权重、缓存、IDE 配置。
- [ ] 代码已格式化，Type Hint 和静态检查符合该任务要求。
- [ ] 核心逻辑有测试或最小复现脚本。
- [ ] README 写清目录、依赖、运行、输入输出、已知限制。
- [ ] 文档是自己的理解，能在答辩中解释公式、API、架构和每个关键选择。
- [ ] 图表有标题、坐标轴、单位、图例和结论，不只是截图。
- [ ] 数据来源、采集时间、字段和清洗规则可追溯。
- [ ] AI 参与部分保留对话/提示词和修正过程，自己已审查生成内容。
- [ ] Git 历史按最小可运行子集组织，没有一个超大提交。
- [ ] 开始新阶段前已检查上游任务是否更新。
