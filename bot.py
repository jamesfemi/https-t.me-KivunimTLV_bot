from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your bot token from BotFather
BOT_TOKEN = "8497214557:AAHPXpdcquwy8NCWllBpvgRY1nzj5fWEpKg"

WELCOME_MESSAGE = """מדויקת לפי הצרכים שלך 🌿

👇🏽👇🏽להזמנות וקישקושים לחצו על הקישורים מחכים לכם 👇🏽👇🏽

https://t.me/m/lreqLDxBYjA0
https://t.me/m/lreqLDxBYjA0
https://t.me/m/lreqLDxBYjA0

👆👆להזמנות וקישקושים לחצו על הקישורים מחכים לכם 👆👆
"""

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
