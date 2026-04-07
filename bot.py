import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Correct way to get token
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing! Add it in Render.")

WELCOME_MESSAGE = """מדויקת לפי הצרכים שלך 🌿

👇🏽👇🏽להזמנות וקישקושים לחצו על הקישורים מחכים לכם 👇🏽👇🏽

https://t.me/m/lreqLDxBYjA0
https://t.me/m/lreqLDxBYjA0
https://t.me/m/lreqLDxBYjA0

👆👆להזמנות וקישקושים לחצו על הקישורים מחכים לכם 👆👆
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
