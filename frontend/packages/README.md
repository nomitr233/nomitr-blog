# frontend/packages/

被 `web` 与 `admin` 复用的内部共享库，全部是 TypeScript。每个子目录是一个 pnpm 工作区包（`@nomitr/<目录名>`），`private: true`，不单独部署。

## 成员

| 目录 | 包名 | 职责 |
| --- | --- | --- |
| `ui/` | `@nomitr/ui` | 跨应用复用的 UI 组件、样式变量、hooks |
| `shared/` | `@nomitr/shared` | 工具函数、类型定义、常量、前端校验 |
| `config/` | `@nomitr/config` | lint 规则、构建基础配置、格式化约定 |

## 规则

1. **只放"已经被两个前端都需要"的东西**。只给某个站点用的组件留在 `web/src` 或 `admin/src`。
2. **不引用 `frontend/web`、`frontend/admin`**，共享库必须能脱离应用独立编译。
3. **不放 Python 代码**：`backend/` 与本层零代码依赖，跨语言只走 `contracts/`。
4. **包之间保持单向**：`ui → shared`，`config` 被所有包引用，`shared` 不反向依赖 `ui`。
5. 每个包必须有唯一入口（`src/index.ts`），外部只能从包入口 import，禁止深路径引用内部文件。
6. 不发布到公共 registry；确需发布时，单独在该包 README 里说明版本策略。
