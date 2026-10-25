# Nomitr Blog

一个以**单仓库（monorepo）**方式组织的博客项目：前台站点、内容管理后台、后端服务与共享库放在同一个仓库里，通过工作区（workspace）互相引用；文章内容与代码分离存放。

> 本仓库只约定**目录结构与分层规则**。各模块具体用什么框架、语言与构建工具，由对应模块自行决定，不影响本文档的约定。

## 目录总览

```text
nomitr-blog/
├─ apps/                     # 可独立运行、可独立部署的应用
│  ├─ web/                   # 博客前台：读者访问的站点
│  ├─ admin/                 # 内容管理后台：写文章、管评论、看数据
│  └─ api/                   # 后端服务：对外提供数据接口
├─ packages/                 # 被应用复用的内部共享库（不单独部署）
│  ├─ ui/                    # 通用 UI 组件
│  ├─ shared/                # 通用工具、类型、常量、校验逻辑
│  └─ config/                # 共享工程配置（lint / 构建 / 规范化）
├─ content/                  # 内容源与素材，与代码分离
│  ├─ posts/                 # 文章正文（Markdown 源文件）
│  ├─ assets/                # 文章配图等静态素材
│  └─ drafts/                # 本地草稿（默认不入库）
├─ docs/                     # 项目文档
│  └─ adr/                   # Architecture Decision Record
├─ scripts/                  # 工程化脚本（新建文章、生成索引、发布等）
├─ deploy/                   # 部署编排
│  ├─ docker/                # 镜像构建与编排文件
│  └─ nginx/                 # 反向代理 / 静态站点配置
├─ .github/workflows/        # CI 流水线
├─ .githooks/                # 本地 Git 钩子（拦截误推 main）
├─ package.json              # 工作区根清单：只放脚本与公共元信息
├─ pnpm-workspace.yaml       # 工作区成员声明
├─ .editorconfig             # 跨编辑器的基础格式约定
├─ .gitattributes            # 统一换行符（LF），避免跨平台 diff 噪音
├─ .gitignore
└─ README.md
```

## 分层规则

| 层级 | 目录 | 放什么 | 不放什么 |
| --- | --- | --- | --- |
| 应用层 | `apps/*` | 可独立启动、独立部署的完整应用 | 供别人复用的抽象、跨应用共享代码 |
| 共享层 | `packages/*` | 被多个应用引用的组件、工具、类型、配置 | 具体页面、具体业务路由、部署产物 |
| 内容层 | `content/*` | 文章正文、配图、草稿 | 任何可执行代码 |
| 支撑层 | `docs/`、`scripts/`、`deploy/` | 文档、工程脚本、部署配置 | 业务运行时逻辑 |

依赖方向只能自上而下，不允许反向或横向：

```text
apps/web   apps/admin   apps/api
      \         |         /
       ▼        ▼        ▼
        packages/*
        （ui / shared / config）

packages/ui ──▶ packages/shared     ✔ 允许
packages/shared ──▶ packages/ui     ✘ 禁止（会形成环形依赖）
 apps/a ──▶ apps/b                  ✘ 禁止（共享逻辑下沉到 packages/）
 packages/* ──▶ apps/*              ✘ 禁止
```

## 命名约定

- 目录与文件名：`kebab-case`，例如 `post-list`、`use-pagination`。
- 工作区包名：`@nomitr/<目录名>`，例如 `apps/web` → `@nomitr/web`。
- 文章文件：`YYYY-MM-DD-<slug>.md`，slug 全仓库唯一，例如 `2026-10-25-hello-nomitr.md`。
- 一个目录一个职责；目录下若只有 README 而没有代码，说明该模块尚未实现，不要往里塞无关文件。

## 常用命令

```bash
pnpm install          # 安装全部工作区依赖
pnpm dev              # 并行启动各应用的 dev 任务（需各 app 自行提供 dev 脚本）
pnpm build            # 构建全部应用
pnpm lint             # 校验全部工作区
```

脚本统一通过 `pnpm -r --if-present <task>` 转发，因此某个模块还没实现该任务时不会报错，补齐后再接入即可。

## 分支约定

| 分支 | 用途 | 是否直接推送 |
| --- | --- | --- |
| `main` | 稳定分支，保持随时可发布 | 否，只接受 PR 合并 |
| `devloop` | 日常开发，所有改动先落这里 | 是 |
| `hotfix/<主题>` | 线上紧急修复，从 `main` 切出 | 是，修完同时合回 `main` 与 `devloop` |

- 改动路径：`devloop` 本地提交 → `git push origin devloop` → 开 PR 合入 `main`。
- 提交信息用 `<type>: <summary>`，`type` 取 `feat` / `fix` / `docs` / `chore` / `refactor` / `test`。
- 可选：启用仓库内的推送守卫，拦截误推 `main`（`git push --no-verify` 可临时绕过）：

```bash
git config core.hooksPath .githooks
```

## 首次提交

仓库已初始化，远端 `origin` 指向 `github.com/nomitr233/nomitr-blog`，但还没有任何提交。HEAD 已切到 `devloop`，首个提交会落在这条分支上，`main` 留空等 PR：

```bash
git branch --show-current   # 应输出 devloop；若不在该分支：git switch -c devloop
pnpm install                # 生成 pnpm-lock.yaml，CI 的 --frozen-lockfile 依赖它
git add -A
git commit -m "chore: init monorepo layout"
git push -u origin devloop
```

`git add -A` 使用 `-A` 而不是点名文件：结构里包含 `apps/*/src/`、`content/posts/` 等新目录，只 add `README.md` 会漏掉它们。

尚未安装 pnpm 时，先执行 `corepack enable`（Node 16.13+ 自带）或 `npm i -g pnpm`。

更多细节见 [docs/architecture.md](docs/architecture.md) 与 [docs/adr/0001-monorepo-layout.md](docs/adr/0001-monorepo-layout.md)。
