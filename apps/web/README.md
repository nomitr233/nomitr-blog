# @nomitr/web

博客前台，读者直接访问的站点。

## 职责

- 渲染公开页面：首页 / 文章列表、文章详情、归档、标签、关于、RSS。
- 读取文章数据：构建期直接消费 `content/posts/`，或运行时调用 `apps/api` 的接口。
- 承载 SEO 相关产出：页面级 meta、站点地图、静态生成的 HTML。

不负责：内容编辑（属于 `apps/admin`）、数据持久化（属于 `apps/api`）。

## 建议的 src 结构

```text
src/
├─ pages/         # 路由级页面，一个文件对应一个可访问路径
├─ components/    # 仅本站点使用的组件
├─ features/      # 按业务域聚合：posts/、search/、comments/
├─ styles/        # 全局样式与主题变量
└─ assets/        # 本站点专用的图片、字体
```

组件若被 `admin` 也需要，就提升到 `packages/ui`，而不是从 web 里 import。

## 依赖

- 可以引用：`@nomitr/ui`、`@nomitr/shared`、`@nomitr/config`。
- 不可以引用：`@nomitr/admin`、`@nomitr/api` 的源码。
