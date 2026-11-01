# AI QA Testing Project

一个用于测试开发实习准备的综合实战项目，包含 FastAPI 后端接口开发、完整的 Pytest 自动化测试体系、以及针对 AI 接口的 Mock 测试实践。

## 🛠 技术栈 (Tech Stack)
*   **语言**: Python 3.13
*   **Web 框架**: FastAPI, Uvicorn
*   **数据校验**: Pydantic
*   **自动化测试**: Pytest, Requests
*   **测试报告**: pytest-html
*   **版本控制**: Git, GitHub

## ✨ 核心功能 (Features)
1.  **基础接口**：提供 `/health` 健康检查接口。
2.  **业务接口**：提供 `/analyze` 接口，实现文本字数统计及参数校验（拦截空文本）。
3.  **AI 接口 (Mock)**：提供 `/chat` 接口，利用 Mock 技术模拟大模型返回，为测试 AI 业务逻辑提供基础。

## 🧪 自动化测试亮点 (Testing Highlights)
*   **数据驱动测试**：使用 `@pytest.mark.parametrize` 覆盖中英文、特殊字符等多种文本输入场景。
*   **异常与边界测试**：覆盖空字符串校验、缺少必填字段（422 状态码）等极端情况。
*   **Mock 测试**：针对收费/不稳定的真实大模型 API，采用 Mock 技术拦截请求，实现**断网环境下的快速回归测试**。
*   **可视化报告**：集成 `pytest-html`，一键生成包含环境信息、用例耗时、执行状态的 HTML 测试报告。

## 🚀 快速开始 (Quick Start)

### 1. 安装依赖
```bash
pip install -r requirements.txt