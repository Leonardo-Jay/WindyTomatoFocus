# 自行发布到 GitHub

这个目录已经初始化为本地 Git 仓库，分支名为 `main`；目前没有提交，也没有设置远程仓库。公开版采用 **GPL-3.0-only 代码 + 独立保留品牌素材权利** 的方案。发布操作由项目作者本人完成。

## 本地文件边界

**会上传**：`zhuchengxu.py`、`jianku.py`、`keshihua.py`、`demo.py`、`assets/public/`、`tools/generate_public_assets.py`、`README.md`、`LICENSE`、`RIGHTS.md`、`requirements.txt`、`docs/`、`shujuku/` 下的版本日志和程序内版权说明、`.gitignore`。

**不会上传**：作者原创品牌图标与音乐所在的 `path/self/`、`shujuku/schedule.db`、`shujuku/defaultdata.json`、`installfiles/` 中的旧安装包、旧 `WindyTomatoFocus.spec`、缓存和编辑器状态。`houduan.py` 也被排除，因为它依赖缺失的 `operations` 模块且主程序没有使用它。

公开版的图标由 `assets/public/` 提供，专注完成时使用 Windows 系统提示音。不要把旧安装包直接作为首个 GitHub Release：旧打包脚本会整体收集私有素材和本地数据。

## 1. 发布前最后核对

在 PowerShell 中执行：

```powershell
cd D:\project\new_app
git status --short --ignored
git add --dry-run .
```

检查候选列表里**没有** `path/self/`、`schedule.db`、`defaultdata.json`、`installfiles/`。不要使用 `git add -f` 绕过忽略规则。如果你在本地改动过文件，先重新核对。

## 2. 在 GitHub 创建空仓库

登录 [GitHub 新建仓库页面](https://github.com/new)，Owner 选 `Leonardo-Jay`，仓库名建议 `WindyTomatoFocus`，Visibility 选 **Public**。不要在网页上勾选初始化 README、`.gitignore` 或 License；这些文件已经在本地，建立空仓库能避免首次推送时合并冲突。[GitHub 官方步骤](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

## 3. 本地提交并推送

仍在 `D:\project\new_app` 执行：

```powershell
git add .
git diff --cached --stat
git status --short
git commit -m "Initial GPLv3 source release"
git remote add origin https://github.com/Leonardo-Jay/WindyTomatoFocus.git
git push -u origin main
```

如果 Git 提示没有配置作者身份，先设置 `git config user.name "Leonardo-Jay"` 和 `git config user.email "你用于 Git 提交的邮箱"`，再重新运行 `git commit`。若你给仓库取了别的名字，替换 `git remote add origin` 中的 URL。推送时按 Git 的提示完成 GitHub 登录；不要把密码或访问令牌写进命令、代码或 README。

## 4. 网页复核

打开公开仓库，确认首页显示 README 和 GPLv3 许可；在文件列表中确认没有个人数据库、设置、原始图标与音频、旧安装包。若日后重新打包，请从干净目录制作，只包含公开版通用图标和适当的第三方许可说明，再考虑通过 GitHub Releases 发布。
