from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random
import os

TOKEN = os.getenv("7905966141:AAEdp0j4BOWBMo4IUc6ELokQ_MvvtxBLvK0")

quotes = ["Ты не обязан быть лучше всех. Но ты обязан быть лучше себя вчерашнего."]
challenges = ["Сделай 10 отжиманий сразу после этой цитаты 💪"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup([["/done"]], resize_keyboard=True)
    quote = random.choice(quotes)
    challenge = random.choice(challenges)
    msg = f"🔥 *Утренняя цитата:*\n_{quote}_\n\n🎯 *Челлендж дня:*\n{challenge}"
    await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=reply_markup)

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    responses = ["Молодец! Ты сделал это 💥", "Уважение! Так держать 💪", "Огонь, брат! 🔥"]
    await update.message.reply_text(random.choice(responses))

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("done", done))
    app.run_polling()
