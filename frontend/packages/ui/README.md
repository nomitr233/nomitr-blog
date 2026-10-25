# @nomitr/ui

`web` 与 `admin` 共用的 UI 组件库。两个前端的视觉规范在这里收敛，避免各写一套按钮和弹窗。

## 放什么

- 基础组件：按钮、输入框、弹窗、分页、骨架屏、提示。
- 布局组件：页头页脚（游客站用）、侧边栏与内容容器（后台用）。
- 主题层：颜色、字号、间距等设计变量，暗色模式切换。
- 与 DOM 交互相关的 hooks：`use-media-query`、`use-click-outside`。

## 不放什么

- 业务组件（`PostCard`、`ArticleTable`）：它们依赖具体数据模型，放各自的 `features/`。
- 页面路由与数据请求逻辑：属于应用层。
- 任何对 `frontend/web`、`frontend/admin` 的引用。

## 建议的 src 结构

```text
src/
├─ components/    # form/、feedback/、layout/、navigation/
├─ hooks/         # 可复用交互逻辑
├─ styles/        # 设计变量、全局基线样式
└─ index.ts       # 唯一对外入口
```

外部只允许 `import { Button } from "@nomitr/ui"`，不要走 `@nomitr/ui/src/components/Button` 这类深路径。
