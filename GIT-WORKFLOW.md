# 个人 fork 与上游同步

## 仓库分工

| 名称 | 地址或位置 | 用途 |
| --- | --- | --- |
| origin | https://github.com/Pineapple-Papaya/learn-AI-me.git | 个人 fork，默认推送目标 |
| upstream | https://github.com/west2-online/learn-AI.git | 官方任务与框架，只拉取；本地 push URL 设为 `DISABLED` |
| legacy | C:/Users/Allen/Desktop/西二在线 | 本机旧作业历史，只读取；本地 push URL 设为 `DISABLED` |

旧作业远端仍为 https://github.com/Pineapple-Papaya/learn-ai-Pineapple-Papaya.git ，此次不向它推送。上述远端设置仅在本机 Git 配置中生效，不随文件提交传播到其他克隆。

## 本次整合

- 在独立目录准备，原旧目录未改动。
- 本地审查分支：`codex/integrate-homework`，以个人 fork 的 `main` 为起点。
- 保留 fork 的个人作业提交，合入上游 `main`，再添加旧目录当前作业和计划。
- 上游已将任务迁入 `docs/work-2026/`，原路径的迁移、删除和官方文档变更均来自此次上游更新。
- 本次已审查摘要并获得明确确认，创建合并提交 `d222417`，再将本地 `main` 快进到该提交。
- 2026-11-09 已仅推送 `origin main`，远端与本地提交一致；没有强推，也未向官方发 PR。后续每次 commit 与 push 仍需按用户规则获得确认。
- 2026-11-09 再次获取上游后，`upstream/main` 仍为 `a3379b1`，已是当前 `main` 的祖先，无需重复合并。
- 2026-11-10 娜比娅修复与学习资料已获本人发布确认，按原路径更新个人 fork 中的文件，保留 Git 历史。

## 日常作业

先看 `git status` 和 diff，小步修改，运行对应检查器；展示变更摘要和结果，经本人确认再 commit。个人媒体、Cookie、密钥、数据集、模型和虚拟环境均不提交。

正式个人娜比娅作业为 `Task1/作业1.py`，使用 `python Task1/check_nabiya.py` 验证。
`docs/work-2026/foundation/Nabia_Snack_Incident/` 用于来源对照和检查资料；
入口说明见 [MY-PROGRESS.md](MY-PROGRESS.md)。

## 后续获取官方更新

下面是操作说明，不表示已经执行未来的同步：

```powershell
Set-Location -LiteralPath 'C:\Users\Allen\Desktop\learn-AI-me'
git switch main
git status --short
git fetch upstream
git log --oneline main..upstream/main
git diff --stat main upstream/main
```

先审查更新及可能的文件删除，工作区干净后再准备合并：

```powershell
git merge --no-commit --no-ff upstream/main
```

有冲突先检查差异，保留个人作业意图并运行验证；不得使用 `reset --hard` 或 force push 代替处理。审查并确认后才执行 commit；再次确认推送目标为自己的 fork 后，执行：

```powershell
git push origin main
```

`fetch upstream` 只读官方更新；`push origin main` 发布到自己的 fork。它们是两个方向不同的动作。无需创建指向官方仓库的 Pull Request。

## 注意事项

- 当前若仍在未完成的合并中，不再运行新的 merge/pull/switch；先完成本次审查。
- 作业保留为根目录 Task0/Task1，避免无必要地搬动旧文件。新增作业的实际入口及时写进进度说明。
- 旧任务清单和历史计划含过时路径，以最新 README 与 `docs/work-2026/foundation/` 的任务原文为准。
