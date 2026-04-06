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

# Reply to ANY message
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Message received")
    await update.message.reply_text(WELCOME_MESSAGE)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
