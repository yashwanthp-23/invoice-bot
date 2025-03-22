# app/routes/telegram.py
from fastapi import APIRouter, Request
from app.services.invoice import generate_invoice
from app.services.utils import send_telegram_message
import os

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    
    try:
        message = data['message']['text']
        sender_id = data['message']['from']['id']
        
        # Parse order and generate invoice
        invoice_path = await generate_invoice(message)
        
        # Send PDF back to user
        await send_telegram_message(sender_id, invoice_path)

    except Exception as e:
        print("Error:", e)

    return {"status": "success"}
