# scripts/

工程化脚本，与业务代码隔离：不进 `frontend/*` 的产物，也不被运行时引用，只在开发、构建、发布阶段执行。

## 放什么

| 脚本 | 用途 |
| --- | --- |
| `new-post` | 按模板在 `content/posts/` 生成新文章文件，自动填日期与 slug |
| `build-index` | 扫描文章生成列表索引（归档、标签、RSS） |
| `sync-content` | 把 `content/posts/` 同步进数据库，供 `backend` 读取 |
| `export-openapi` | 从 `backend` 导出 `contracts/openapi.json`，再生成 `frontend/packages/shared/src/types/api/` |
| `check-structure` | 校验目录是否符合约定（如前端应用互相引用、`web` 调用写接口、契约被手改） |

## 约定

- 一个脚本一个文件，命名 `kebab-case`，落语言按实现选（`.mjs` / `.sh` / `.py`），但必须能独立运行。
- 必须有 `--help`，说明参数与默认值。
- 脚本只依赖自己语言的工具链，不引用具体应用的源码。
- 破坏性操作（删文件、写数据库）默认 `--dry-run`，需显式确认才执行。

## 与工程的关系

`frontend/` 与 `backend/` 里的命令只做转发；跨目录、跨语言的流程写在这里，便于单独调试与在 CI 中复用。
