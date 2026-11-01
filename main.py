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
