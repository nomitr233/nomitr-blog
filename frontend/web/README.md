# @nomitr/web（游客站）

面向读者的公开站点，只读。博客对外的门面。

## 职责

- 公开页面：首页 / 文章列表、文章详情、归档、标签、关于、RSS。
- 数据来源：调用 `backend` 的读接口；若采用构建期生成，则在构建时拉取一次。
- SEO：页面级 meta、站点地图、静态 HTML 输出。

**不做什么**：不提供任何写操作（发文、改文、删评论都不在这里），也不直连数据库。

## 建议的 src 结构

```text
src/
├─ pages/         # 路由级页面：index、posts/[slug]、tags/[tag]、about
├─ components/    # 仅游客站使用的组件（例如文章卡片）
├─ features/      # 按业务域聚合：posts/、search/、comments/（若开放评论）
├─ services/      # 接口调用封装，统一出口，便于替换 mock
├─ styles/        # 全局样式与主题变量
└─ assets/        # 本站专用图片、字体
```

## 依赖边界

- 可以引用：`@nomitr/ui`、`@nomitr/shared`、`@nomitr/config`。
- 接口类型只从 `@nomitr/shared` 的 `types/api/` 取（由契约生成），不手写。
- 不可以引用：`@nomitr/admin` 的任何文件，以及 `backend/` 的源码。
- 与后台共用组件时，提升到 `@nomitr/ui`，不要在 web 里做"顺便也给 admin 用"的导出。
