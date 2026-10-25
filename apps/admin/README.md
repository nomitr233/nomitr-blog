# @nomitr/admin

内容管理后台，面向作者本人的写作与运营界面。

## 职责

- 文章的增删改查、草稿管理、发布与撤回。
- 评论审核、标签与分类维护。
- 调用 `apps/api` 的接口完成写操作，不在前端直接读 `content/` 目录。

不负责：公开页面的渲染（属于 `apps/web`）、接口实现（属于 `apps/api`）。

## 建议的 src 结构

```text
src/
├─ pages/         # 路由级页面：登录、文章列表、编辑器等
├─ components/    # 后台专用组件（表格、表单、编辑器外壳）
├─ features/      # 按业务域聚合：articles/、comments/、settings/
├─ services/      # 与后端接口交互的封装，统一出口
└─ styles/        # 后台主题样式
```

## 依赖

- 可以引用：`@nomitr/ui`、`@nomitr/shared`、`@nomitr/config`。
- 不可以引用：`@nomitr/web`、`@nomitr/api` 的源码。

后台与前台共用的表单控件、编辑器壳等，放 `packages/ui`，两边都从包里取。
