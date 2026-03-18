from fastapi import FastAPI, Request
from chatbot import ricardo_ai_response
from fidelity import add_points

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    data = await request.json()
    user_message = data.get("Body", "")
    user_id = data.get("From", "")

    reply = ricardo_ai_response(user_message, user_id)
    add_points(user_id, action="chat")

    return {"reply": reply}
