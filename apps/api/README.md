# @nomitr/api

后端服务，为 `web` 与 `admin` 提供数据接口。

## 职责

- 文章、标签、评论、站点配置的读取与写入接口。
- 认证与鉴权：后台写操作必须经过身份校验。
- 内容同步：把 `content/posts/` 的源文件导入数据库，或反向导出。
- 提供给 `web` 构建期使用的稳定数据契约。

不负责：页面渲染、后台界面。

## 建议的 src 结构

```text
src/
├─ modules/       # 按业务域划分：articles/、comments/、auth/
│                 # 每个模块内部再分 controller / service / repository
├─ common/        # 跨模块的基础设施：异常、拦截器、校验管道
├─ jobs/          # 定时或一次性任务：内容同步、索引重建
└─ config/        # 配置读取与环境变量校验
```

## 依赖

- 可以引用：`@nomitr/shared`（类型、校验规则、常量）、`@nomitr/config`。
- 一般不需要引用 `@nomitr/ui`；服务端不应依赖浏览器组件。
- 不可以引用：`@nomitr/web`、`@nomitr/admin` 的源码。

接口的请求/响应类型放 `packages/shared/src/types/`，让前后端共用同一份定义。
