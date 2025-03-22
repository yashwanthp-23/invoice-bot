# app/services/utils.py
import requests
import os

async def send_whatsapp_message(user_id, file_path):
    # Upload media to WhatsApp Cloud API
    media_url = f"https://graph.facebook.com/v13.0/{os.getenv('WHATSAPP_PHONE_ID')}/media"
    headers = {
        'Authorization': f'Bearer {os.getenv("WHATSAPP_TOKEN")}',
        'Content-Type': 'application/json',
    }
    
    files = {'file': open(file_path, 'rb')}
    response = requests.post(media_url, headers=headers, files=files)
    media_id = response.json().get('id')
    
    # Send document message
    message_url = f"https://graph.facebook.com/v13.0/{os.getenv('WHATSAPP_PHONE_ID')}/messages"
    data = {
        "messaging_product": "whatsapp",
        "to": user_id,
        "type": "document",
        "document": {
            "id": media_id,
            "filename": "invoice.pdf"
        }
    }
    
    requests.post(message_url, headers=headers, json=data)
