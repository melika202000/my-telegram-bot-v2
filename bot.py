import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔹 توکن ربات (حتماً جایگزین کن!)
TOKEN = "8166526926:AAGxhbUNoYvZ4_AUWRoqlK_qbuQ3BI6CITo"

# 🔹 تنظیمات لاگ برای خطایابی
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /start"""
    await update.message.reply_text("سلام داپینویی عزیز💖، من دستیار تو هستم. چطور میتونم کمکت کنم؟ 🥰")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """پاسخ به پیام‌های کاربر"""
    await update.message.reply_text("پیام زیبات به دستمون رسید، به زودی پاسخ برات ارسال میشه🥰✨")

def main():
    """اجرای ربات"""
    app = Application.builder().token(TOKEN).build()

    # ثبت دستورات ربات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # اجرای مداوم بات
    app.run_polling()

if __name__ == "__main__":
    main()
