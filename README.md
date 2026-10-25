# Nomitr Blog

一个用来练手的博客项目：Python 后端 + 两个前端（游客站、文章管理后台）。文章和图片放 OSS，仓库里只有代码。

## 结构

```text
nomitr-blog/
├─ frontend/              # 所有 TypeScript（pnpm 工作区根）
│  ├─ package.json
│  ├─ pnpm-workspace.yaml
│  ├─ web/                # 游客站：列表、详情、标签
│  ├─ admin/              # 文章管理后台：写作、发布
│  └─ packages/           # 共享库：现在是空壳，等真的重复了再抽
├─ backend/               # 所有 Python
│  ├─ pyproject.toml      # 依赖 + ruff/mypy/pytest 配置
│  ├─ src/nomitr_api/     # 代码
│  └─ tests/              # 测试
├─ contracts/             # 接口契约，暂时可以不管
├─ deploy/                # docker / nginx，最后阶段再碰
├─ docs/                  # 只有一页约定
├─ scripts/
└─ README.md
```

三条规则够用了：

1. TypeScript 进 `frontend/`，Python 进 `backend/`，不要混。
2. `web` 与 `admin` 互不 import；真需要共用代码时放 `frontend/packages/`。
3. 文章和图片在 OSS，仓库里不存内容；开发用 `test/` 前缀，生产用 `prod/`。

## 跑起来

```bash
# 后端
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
pytest

# 前端
cd frontend
pnpm install
pnpm dev
```

现在两个 `src/` 都是空的，所以上面只能装依赖、跑不了服务——这正是要你写的第一件事。

## 学习路线

按顺序做，每步都有验收标准。卡住了再问我，我不代写。

**① 后端起得来**

- 写 `backend/src/nomitr_api/main.py`，先不接框架也行：一个模块级 `app` 或一个 `main()`。
- 加一个 `GET /api/health` 返回 `{"ok": true}`。
- `backend/tests/` 里写第一个用例。
- ✅ 验收：`pytest` 通过，且能用一条命令启动服务、浏览器/curl 访问到健康检查。

**② 文章读接口**

- `modules/articles/` 里先写死三条假数据，返回列表和详情。
- 想清楚 slug、标题、发布时间、标签这几个字段怎么组织。
- ✅ 验收：`GET /api/articles` 和 `GET /api/articles/{slug}` 有稳定响应。

**③ 游客站**

- `frontend/web/src` 里做列表页和详情页，先用假数据或直连 ② 的接口。
- 路由、数据请求、加载态、404 各自怎么处理，自己想一遍。
- ✅ 验收：浏览器里能点进文章详情，刷新不 404。

**④ 接真数据**

- 后端把 ② 的假数据换成 OSS 读写（`modules/storage/` 里封一个适配层）。
- 图片上传接口、返回 CDN 地址。
- ✅ 验收：后台发一篇文章，游客站能看到。

**⑤ 后台**

- 登录（先做一个写死的账号也行），文章列表、编辑、发布。
- ✅ 验收：能写能改能下架，未登录访问后台页面会被拦住。

**⑥ 部署**

- `deploy/` 里补 Dockerfile 和 nginx 配置，把三个单元跑起来。
- ✅ 验收：一条命令起全站，`/api` 反代正常。

做到哪一步都可以停。中途想回头改结构也行，改完把这份 README 和 `docs/architecture.md` 一起改掉。

## 说明

- `docs/architecture.md` 是约定速查，写作时翻一眼就够，不用背。
- 每个目录里的 README 是备忘（"这里放什么"），不是任务书。
- ADR（架构决策记录）这类东西等你真的做过几个取舍再补，现在没有必要。
