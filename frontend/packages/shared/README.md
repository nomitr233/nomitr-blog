# @nomitr/shared

与 UI 无关的共享逻辑，供 `web` 与 `admin` 引用。**仅限 TypeScript**：Python 后端 `backend/` 不引用本包，跨语言对齐靠 `contracts/`。

## 放什么

- 接口类型：由 `contracts/openapi.json` 生成到 `src/types/api/`，两个前端共用（生成物，勿手改）。
- 领域类型：文章、标签、分页等前端内部使用的类型。
- 工具函数：日期格式化、slug 生成、摘要截断、URL 处理。
- 常量：站点信息、分页大小、文章状态枚举（与后端枚举保持一致，见契约）。
- 前端校验：表单必填、长度、格式规则；后端入参校验以 Python 侧模型为准。

## 不放什么

- 组件、样式、DOM 操作（属于 `@nomitr/ui`）。
- 后端逻辑：数据库、服务端 HTTP 处理都在 `backend/`，Python 侧自有一套。
- 与具体接口绑定的请求封装：放各应用的 `services/`，便于 mock 和替换。
- 环境相关的配置读取。

## 建议的 src 结构

```text
src/
├─ types/         # 领域类型；types/api/ 为契约生成物
├─ utils/         # 纯函数工具，保持无副作用
├─ constants/     # 常量与枚举
├─ validation/    # 前端校验规则
└─ index.ts       # 唯一对外入口
```

## 依赖

- 允许引用：`@nomitr/config`。
- 不允许引用：`@nomitr/ui`（避免 `ui ↔ shared` 环）、`frontend/web`、`frontend/admin`。
