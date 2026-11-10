# Foundation 1 学习与作业入口

## 教学顺序

先教够用的基础知识，再回到官方模板对应的函数与 TODO，一步一步填写和验证。
仅在题目没有模板时另写程序；基础讲解中的小例子不替代模板作业。
每次练习给齐题目、文件位置、变量来源和上下文，不默认存在未说明的变量。

| 官方任务 | 当前对应文件 | 使用方式 |
| --- | --- | --- |
| 文档 1：Python 笔记 | [note.md](note.md) | 沿用本人已有笔记，补入已学内容；没有固定代码模板 |
| 作业 1：娜比娅 | [正式实现][battle] | 原模板的 12 个函数；修复在此文件内完成 |
| 作业 2：校园 | [官方框架][campus] | 基础知识学够后，按原类、方法、字典和 TODO 完成 |
| 文档 2：终端复盘 | 待所选代码作业完成后撰写 | 不提前编造问题与复盘 |

[battle]: ../docs/work-2026/foundation/Nabia_Snack_Incident/longmen_vs_nabiya.py
[campus]: ../docs/work-2026/foundation/Campus_IF_Love/Campus_IF_Love.py

`Task1/作业1.py` 是迁移前的早期草稿，正式娜比娅作业以表中路径为准。
`day1-cheatsheet.md` 是复习资料，不替代正式笔记。

## 娜比娅与原模板的对应关系

已通过 AST 核对：12 个函数的名字、参数、返回注释与原模板一致，13 个数值常量一致。
官方检查器、运行入口和参考答案未修改。函数体是填入模板任务的实现，不是重新定义题目。

| 原模板函数 | 任务 |
| --- | --- |
| `display_status` | 检查最大 HP 并按检查器格式输出 |
| `roll_dice` | 校验数量，用 while 掷骰并累加 |
| `choose_nagato_action` | 根据双方 HP 选择行动 |
| `calculate_attack_damage` | 使用指定骰子数计算攻击 |
| `calculate_defense_value` | 使用指定骰子数计算防御 |
| `check_critical_hit` | 比较暴击阈值并返回布尔值 |
| `nabiya_ai_action` | 根据 HP 选择娜比娅行动 |
| `calculate_final_damage` | 校验伤害、防御并计算非负结果 |
| `apply_damage` | 正确扣除 HP，最低为零 |
| `is_battle_over` | 判断是否一方 HP 归零 |
| `get_battle_result` | 返回胜者或平局 |
| `main_battle_loop` | 按模板顺序执行双方行动、防御消耗、结束判断和回合推进 |

本地验证：官方检查 11/11、回归测试 14/14 通过。个人理解验收仍留 Day 4。

## 校园模板的学习前置与落点

1. 先学 Class、实例、属性和 `self` 的够用基础，再读 `Character.__init__`。
2. 先学嵌套字典与 `.get()`，再使用原有 `GIFT_EFFECTS`，不另造礼物表替代正式数据。
3. 在 `Character.give_gift(self, gift)` 的 TODO 中查询角色对应效果，
   调用已有 `self.change_affinity(value)` 更新角色状态。
4. 在 `Character.talk(self)` 的 TODO 中使用原有 `DIALOGUES` 或允许的自拟对话。
5. 先学条件、循环和退出，再完善 `Game.story_loop` 已有菜单；
   按原选项处理聊天、送礼、查看好感度与退出。
6. 后两条路线回到 `scene_xiaobai`、`scene_jiejie` 的 TODO，随后完成拆文件与 Type Hint。

今天只开始第一条路线；未完成的模板任务不能因为基础练习通过就标为完成。

## 文件与 Git 同步

每完成一部分，先落到对应笔记或模板文件，验证并展示摘要，再按本人确认提交和推送。
唯一目标是 `Pineapple-Papaya/learn-AI-me`；官方与旧仓库只读取，不推送。
“本地已保存”和“GitHub 已同步”分开说明，以实际提交与远端核对结果为准。
