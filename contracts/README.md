# contracts/

语言无关的接口契约，是 `frontend/`（TypeScript）与 `backend/`（Python）之间**唯一的事实来源**。两个世界不共享代码，只共享这份文件。

## 内容

| 文件 | 来源 | 消费方 |
| --- | --- | --- |
| `openapi.json` | `backend` 导出 | `frontend/packages/shared/src/types/api/`（生成 TS 类型）、接口调试工具 |

## 流程

```text
backend 的请求/响应模型（Python）
        │ 导出
        ▼
contracts/openapi.json   ← 随 PR 提交，可在 diff 里审查
        │ 代码生成
        ▼
frontend/packages/shared/src/types/api/   ← 生成物，web 与 admin 都从这里取类型
```

## 规则

1. **由后端生成，不手写**。契约只能来自 `backend` 的模型定义，避免两端各写一份再对不上。
2. **生成物不手改**。`frontend/packages/shared/src/types/api/` 下是生成代码，改动会随下次生成被覆盖；要改字段就去改后端模型。
3. **契约变更是接口变更**，PR 里必须说明：新增字段通常兼容，重命名/删除字段要同步改两个前端的调用点。
4. **提交生成结果**。`openapi.json` 与生成的 TS 类型都要入库，保证克隆后不装 Python 也能编译前端。

生成脚本的位置与命令随技术选型确定，实现后补到这里；在那之前，本目录只承载约定。
