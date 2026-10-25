# scripts/

工程化脚本，与业务代码隔离：不进 `apps/*` 的产物，也不被运行时引用，只在开发、构建、发布阶段执行。

## 放什么

| 脚本 | 用途 |
| --- | --- |
| `new-post` | 按模板在 `content/posts/` 生成新文章文件，自动填日期与 slug |
| `build-index` | 扫描文章生成列表索引（归档、标签、RSS） |
| `sync-content` | 把 `content/posts/` 同步进数据库，供 `apps/api` 读取 |
| `check-structure` | 校验目录是否符合约定（如共享包缺失入口、app 之间互相引用） |

## 约定

- 一个脚本一个文件，命名 `kebab-case`，不带扩展名歧义（`.mjs` / `.sh` 由实现决定）。
- 必须有 `--help`，说明参数与默认值。
- 脚本只依赖根 `package.json` 的 devDependencies，不引用具体应用的源码。
- 破坏性操作（删文件、写数据库）默认 `--dry-run`，需显式确认才执行。

## 与根脚本的关系

根 `package.json` 中的命令只做转发；复杂流程写在这里，通过 `scripts/` 下的条目调用，便于单独调试与在 CI 中复用。
