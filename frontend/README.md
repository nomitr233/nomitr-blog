# frontend/

全部 TypeScript 代码，同时是 pnpm 工作区的根：`package.json`、`pnpm-workspace.yaml`、`pnpm-lock.yaml` 都在这一层。

## 成员

| 目录 | 包名 | 用途 | 使用者 |
| --- | --- | --- | --- |
| `web/` | `@nomitr/web` | 游客站：文章列表、详情、归档、标签、关于 | 公开访问 |
| `admin/` | `@nomitr/admin` | 文章管理后台：写作、发布、下架、标签维护 | 只有你 |
| `packages/ui/` | `@nomitr/ui` | 两个前端共用的组件与设计变量 | web、admin |
| `packages/shared/` | `@nomitr/shared` | 工具、类型、常量、前端校验 | web、admin |
| `packages/config/` | `@nomitr/config` | lint / 构建 / 格式的共享配置 | 所有成员 |

## 规则

1. **`web` 与 `admin` 互不引用**。两边都要用的东西放 `packages/`，并且只从包名导入（`@nomitr/ui`），不写 `../../admin/...` 这类相对路径。
2. **只有 `web`、`admin` 是部署单元**，`packages/*` 不单独部署，`private: true`。
3. **数据靠接口拿**：两个前端都不直连数据库、不读 `backend/` 的源码，统一走 HTTP + `contracts/openapi.json`。
4. **游客站只读**：`web` 不调用任何写接口；写操作全部在 `admin` 里，接口侧再做鉴权兜底。
5. **共享类型不手写两遍**：接口类型由契约生成到 `packages/shared/src/types/api/`，两个前端都从那里取。
6. 新增前端应用要手动加进 `pnpm-workspace.yaml`（没用通配），并在本表补一行。

## 命令

```bash
cd frontend
pnpm install
pnpm dev            # 并行启动 web 与 admin
pnpm build
pnpm --filter @nomitr/web dev      # 只启游客站
pnpm --filter @nomitr/admin dev    # 只启后台
```
