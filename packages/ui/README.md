# @nomitr/ui

跨应用复用的 UI 组件库，被 `web` 与 `admin` 共同依赖。

## 放什么

- 基础组件：按钮、输入框、弹窗、分页、骨架屏、提示。
- 布局组件：页头页脚、侧边栏、内容容器。
- 主题层：颜色、字号、间距等设计变量，以及暗色模式切换。
- 与 DOM 交互相关的 hooks：`use-media-query`、`use-click-outside`。

## 不放什么

- 业务组件（`PostCard`、`CommentList`）：它们依赖具体数据模型，放各自的 `features/`。
- 页面路由与数据请求逻辑：属于应用层。
- 任何对 `apps/*` 的引用。

## 建议的 src 结构

```text
src/
├─ components/    # 组件按功能分组：form/、feedback/、layout/、navigation/
├─ hooks/         # 可复用交互逻辑
├─ styles/        # 设计变量、全局基线样式
└─ index.ts       # 唯一对外入口
```

外部使用时只允许 `import { Button } from "@nomitr/ui"`，不要走 `@nomitr/ui/src/components/Button` 这类深路径。
