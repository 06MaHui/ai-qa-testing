import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# 1. 参数化测试：正常情况
@pytest.mark.parametrize("input_text, expected_count", [
    ("Hello World", 11),
    ("测试开发", 4),
    ("FastAPI", 7),
])
def test_analyze_normal(input_text, expected_count):
    response = client.post("/analyze", json={"text": input_text})
    assert response.status_code == 200
    assert response.json()["char_count"] == expected_count

# 2. 异常测试：空字符串
def test_analyze_empty():
    response = client.post("/analyze", json={"text": "   "})
    assert response.status_code == 200
    assert response.json() == {"error": "Text cannot be empty"}

# 3. 极端异常测试：缺少必填字段
def test_analyze_missing_field():
    # 故意不传 text，测试 FastAPI 的内置校验
    response = client.post("/analyze", json={}) 
    assert response.status_code == 422  # 422 是 FastAPI 默认的请求体校验错误码