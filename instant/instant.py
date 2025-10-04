from fastapi import FastAPI
from openai import OpenAI
from fastapi.responses import HTMLResponse
import os 

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    client = OpenAI()
    message = """
    You are on a website that has just been deployed to production for the first time.
    Please reply with an enthusiastic message to welcome visitors to the site, 
    explaining that it is live on production. 
    """
    messages = [{
        "role": "user",
        "content": message
    }]
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = (
        f"<html><head><title>Welcome to the site!</title></head><body><p>{reply}</p></html>"
    )
    return html

@app.get("/check")
def check():
    return {"has_key": bool(os.getenv("OPENAI_API_KEY"))}