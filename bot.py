import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import instaloader

TOKEN = os.getenv("BOT_TOKEN")

L = instaloader.Instaloader()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    try:
        if "instagram.com" in url:
            shortcode = url.split("/")[-2]
            post = instaloader.Post.from_shortcode(L.context, shortcode)

            L.download_post(post, target="downloads")

            await update.message.reply_text("Download feito ✅")
        else:
            await update.message.reply_text("Envie um link válido")

    except Exception:
        await update.message.reply_text("Erro ao baixar")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
