# 面试资料索引

适用定位：**5 年前端 + AI 应用工程化 + AI Agent + RAG + Go/Python**。

这套文档服务两类场景：

1. **面试准备**：自我介绍、项目讲法、RAG/Agent 深挖、工程化追问。
2. **RAG 知识注入**：`local_rag.py` 默认不加载全文；需要时可设 `BOSS_RAG_LOAD_DOCS=1` 把 `docs/*.md` 切分进 Prompt。

## 阅读顺序

| 顺序 | 文档 | 用途 |
|------|------|------|
| 0 | [business-flow.md](./business-flow.md) | **业务小白必读**：投递/聊天/AI 全流程人话版 |
| 1 | [ai-interview-learning-roadmap.md](./ai-interview-learning-roadmap.md) | 总路线：学什么、怎么讲、七天突击 |
| 2 | [ai-interview-playbook.md](./ai-interview-playbook.md) | 作战手册：主线话术 + 场景题模板 |
| 3 | [ai-interview-questions-detailed.md](./ai-interview-questions-detailed.md) | 题库：短答 → 展开 → 项目结合 → 防守 |
| 4 | [ai-interview-review-and-study.md](./ai-interview-review-and-study.md) | 复盘：易错表达、必背模板、模拟题 |

## 一句话定位（所有文档统一口径）

> 我不是算法训练方向。我的定位是 **前端出身 + AI 应用工程化**：能把 RAG、Agent、LLM 调用做成可上线的产品和链路，重点解决检索准确、流式体验、工具安全、结果可解释、成本可控和线上可观测。

## 技术栈地图

```text
前端（主战场）
  TypeScript / React(Vue) · 聊天与质检后台 · SSE/WebSocket 流式 · 状态管理 · 表单/表格/权限 UI

AI 应用工程
  RAG 全链路 · Agent 工具编排 · Prompt 版本 · 结构化输出 · 评测与 badcase · MCP

后端/脚本（Go / Python）
  Python：FastAPI · Celery/队列 · LangChain/LangGraph · embedding/rerank 脚本
  Go：高并发 API · 任务调度 · 网关/鉴权 · 观测与限流

基础设施
  Redis · Kafka/RabbitMQ · PostgreSQL/MySQL · ES/PGVector/Milvus · 对象存储
```

## 不要说的话

- 「我训练了大模型」—— 除非真的做过训练/微调。
- 「RAG 就是 AI 长期知识库」—— 应说：**RAG 是检索增强链路，知识库只是数据源之一**。
- 「Agent 可以自动操作系统」—— 应说：**受控工具调用 + 权限 + 审计 + 人工兜底**。
- 「我只会调 ChatGPT API」—— 应讲：RAG、Agent、评测、降级、前端体验、可观测性。

## 2 分钟项目标准结构

```text
业务背景（为什么需要 AI）
→ 用户/运营在前端看到什么（对话、质检结果、复核台）
→ 后端链路（ASR / RAG / LLM / 任务状态）
→ 我负责什么（前端 + 工程化 + 部分 RAG/Agent）
→ 难点（召回、流式、JSON 稳定、可解释、成本）
→ 指标（准确率、复核率、延迟、token 成本）
```
