# 约定速查

写代码时拿不准放哪，看这一页。不超过两分钟。

## 放哪

| 东西 | 位置 |
| --- | --- |
| 游客站页面、组件 | `frontend/web/src/` |
| 后台页面、组件 | `frontend/admin/src/` |
| 两个前端都要用的代码 | `frontend/packages/`（**先别抽**，重复第三次再说） |
| 后端接口、业务逻辑 | `backend/src/nomitr_api/modules/<域>/` |
| OSS 读写 | `backend/src/nomitr_api/modules/storage/`，业务模块不直接调 SDK |
| 数据库迁移 | `backend/migrations/` |
| 测试 | `backend/tests/`、前端各应用自己的 `*.test.*` |
| 部署 | `deploy/docker/`、`deploy/nginx/` |
| 一次性脚本 | `scripts/` |

## 五条边界

1. **前端不 import 后端**，只走 HTTP；后端也不 import 前端。
2. **`web` 和 `admin` 互不 import**。共用代码放 `frontend/packages/`，从包名导入，不写相对路径跨应用。
3. **写接口必须服务端鉴权**。`/api/admin/*` 统一校验，前端隐藏入口不算防护。
4. **游客站只读**，不调任何写接口。
5. **OSS key 必须带环境前缀**：`{OSS_PREFIX}/articles/...`、`{OSS_PREFIX}/assets/...`，代码里不出现裸 key。

## OSS 约定

```text
{prefix}/articles/YYYY-MM-DD-<slug>.md    # 文章正文
{prefix}/assets/YYYY/MM/<uuid>.<ext>      # 图片
```

`OSS_PREFIX` 开发填 `test`，生产填 `prod`。数据库只存元数据和 OSS key，正文以 OSS 为准。

## 什么时候该写文档

- 改了目录结构：更新这份文件和根 `README.md`。
- 做了有代价的取舍（换框架、换存储、拆包）：在 `docs/adr/` 补一页，说清背景和备选。没做过取舍就不用写。
