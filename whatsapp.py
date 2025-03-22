# app/routes/whatsapp.py
from fastapi import APIRouter, Request
from app.services.invoice import generate_invoice
from app.services.utils import send_whatsapp_message
import os

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.json()

    try:
        message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        sender_id = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        
        # Parse order and generate invoice
        invoice_path = await generate_invoice(message)
        
        # Send PDF back to user
        await send_whatsapp_message(sender_id, invoice_path)

    except Exception as e:
        print("Error:", e)

    return {"status": "success"}
