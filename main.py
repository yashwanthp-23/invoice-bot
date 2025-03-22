# app/main.py
from fastapi import FastAPI
from app.routes import whatsapp, telegram
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

# Database Setup
client = AsyncIOMotorClient(os.getenv('MONGO_URI'))
db = client.invoice_bot_db

# Register routes
app.include_router(whatsapp.router, prefix="/whatsapp")
app.include_router(telegram.router, prefix="/telegram")

# Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Invoice Bot is running!"}
