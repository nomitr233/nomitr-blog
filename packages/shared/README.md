# @nomitr/shared

与 UI 无关的共享逻辑，前后端都可以引用。

## 放什么

- 类型定义：文章、标签、评论、分页等数据结构（前后端共用一份）。
- 工具函数：日期格式化、slug 生成、摘要截断、URL 处理。
- 常量：站点信息、分页大小、文章状态枚举。
- 校验规则：文章 frontmatter 的字段校验、接口入参校验。
- 内容解析：把 Markdown 源文件解析成统一数据结构（不含渲染）。

## 不放什么

- 组件、样式、DOM 操作（属于 `@nomitr/ui`）。
- 数据库访问、HTTP 客户端实例等有运行时依赖的东西（属于 `apps/api` 或应用层的 `services/`）。
- 环境相关的配置读取。

## 建议的 src 结构

```text
src/
├─ types/         # 数据结构定义
├─ utils/         # 纯函数工具，保持无副作用
├─ constants/     # 常量与枚举
├─ validation/    # 校验规则
└─ index.ts       # 唯一对外入口
```

## 依赖

- 允许引用：`@nomitr/config`。
- 不允许引用：`@nomitr/ui`（避免形成 `ui ↔ shared` 环）、任何 `apps/*`。
