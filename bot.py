import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("8497214557:AAHPXpdcquwy8NCWllBpvgRY1nzj5fWEpKg")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN missing!")

WELCOME_MESSAGE = """מדויקת לפי הצרכים שלך 🌿

👇🏽👇🏽להזמנות וקישקושים לחצו על הקישורים מחכים לכם 👇🏽👇🏽

https://t.me/m/lreqLDxBYjA0
https://t.me/m/lreqLDxBYjA0
https://t.me/m/lreqLDxBYjA0

👆👆להזמנות וקישקושים לחצו על הקישורים מחכים לכם 👆👆
"""
