# content/

博客的内容源，和代码分开存放：改文章不需要动代码，改代码也不会误伤文章。`content/` 不参与工作区依赖安装，由 `apps/api` 或构建脚本读取。

## 目录

| 目录 | 内容 | 是否入库 |
| --- | --- | --- |
| `posts/` | 已发布与待发布文章（Markdown 源文件） | 是 |
| `assets/` | 文章配图、附件等静态素材 | 是 |
| `drafts/` | 本地草稿 | 否（已在 `.gitignore` 中忽略） |

## 文章文件约定

- 命名：`YYYY-MM-DD-<slug>.md`，slug 全仓库唯一。
- 目录平铺，不做多级分类；分类靠 frontmatter 的 `tags` / `categories` 表达。
- frontmatter 字段：

```yaml
---
title: 文章标题            # 必填
date: 2026-10-25           # 必填，发布日期
updated: 2026-10-26        # 可选，最后修改日期
summary: 列表页摘要        # 可选，缺省时截取正文开头
tags: [meta]               # 可选，用于标签页聚合
draft: false               # 可选，true 时构建期跳过
cover: /assets/cover.png   # 可选，封面图，相对 content/assets
---
```

字段的校验规则与解析逻辑放 `packages/shared`，不要在读取方各写一份。

## 素材约定

- 图片按用途分目录：`assets/covers/`、`assets/inline/`，避免根目录堆满文件。
- 文件名用 `kebab-case`，不加空格与中文，便于 URL 引用。
- 大文件（视频）不入库，放对象存储，文章里引外链。

## 内容流水线

```text
content/posts/*.md
      │  解析 + 校验（packages/shared）
      ▼
  apps/api 导入数据库  ──▶  web 构建时读取 / 运行时请求
      ▲
      └── apps/admin 编辑文章（写接口回库，必要时导出回 Markdown）
```
