# deploy/

部署编排，按平台分目录。原则：**一个部署单元一个目录**，配置里不出现跨单元隐式依赖。

## 部署单元

| 单元 | 源码 | 命名（Dockerfile / nginx.conf） | 运行形态 |
| --- | --- | --- | --- |
| 游客站 | `frontend/web` | `web` | 静态产物或 SSR 进程 |
| 管理后台 | `frontend/admin` | `admin` | 静态产物，可独立域名 |
| 接口服务 | `backend` | `api` | Python 常驻进程 |

## 目录

| 目录 | 内容 |
| --- | --- |
| `docker/` | 各单元的镜像构建文件与本地编排（compose），一单元一 `Dockerfile` |
| `nginx/` | 反向代理与静态站点配置：域名、证书、缓存头、动静分离、`/api` 转发 |

## 约定

- **前后端基础镜像不同**：`web`、`admin` 用 Node 起构建、产物交给 nginx；`api` 用 Python 基础镜像，构建上下文是 `backend/`，安装依赖用 `pip install -e .`（或 `uv sync --frozen`）。
- `api` 的镜像里不装 Node，`web`/`admin` 的镜像里不装 Python——两个语言世界的产物互不夹带。
- 后台与游客站分开时，nginx 必须把 `/api` 反代到 `api`，并把 CORS 白名单收紧到这两个域名。
- 密钥、证书、数据库密码不入库，通过环境变量或部署平台的 secret 注入；仓库里只放 `.env.example`。
- 每个环境（dev / staging / prod）的差异用覆盖文件表达，不要复制整份配置。
- 新增部署单元时，在这里补对应的构建文件与代理配置，并更新本表。
