from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#定义请求格式：要求传入的JSON必须包含text字段
class TextItem(BaseModel):
    text:str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze_text(item:TextItem):
    text = item.text
    if not text.strip():
        return{"error":"Text cannot be empty"}
    
    return{
        "original_text":text,
        "char_count":len(text)
    }

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat_with_ai(request: ChatRequest):
    user_text = request.prompt
    mock_ai_reply = f"【来自AI的回复】我收到了你的提问：'{user_text}'。这是一条通过 Mock 技术模拟的回复！"
    
    return{
        "status": "success",
        "reply": mock_ai_reply,
        "model": "mock-gpt-3.5"
    }

