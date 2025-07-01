import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOXIC_PHRASES = [
    "Ты — ошибка синтаксиса в человеческом виде.",
    "Даже captcha умнее тебя.",
    "Ты как баг, который не фиксится.",
    "С тобой даже ИИ отказывается говорить.",
    "Ты мог бы быть полезен… в режиме 'не беспокоить'.",
    "Твоя логика — как null, вроде есть, но толку ноль.",
    "С тобой спорить — всё равно что дебажить NaN.",
    "Ты как while(true), только бессмысленнее.",
    "Если бы у глупости был интерфейс — ты бы его имплементировал.",
    "Ты — как зависимость без документации: никто не знает, зачем ты тут.",
    "Твоя харизма — как 404 Not Found.",
    "С тобой даже try/catch не справится.",
    "Ты — пример того, как не надо коммитить в реальность.",
    "Когда ты говоришь, даже console.log выдает undefined.",
    "Твоя самооценка — единственное, что у тебя в overload.",
    "Если бы интеллект был библиотекой — у тебя бы был missing import.",
    "Ты — как merge конфликт: от тебя все страдают.",
    "С тобой даже баг-репорты отказываются работать.",
    "Твоя речь — как плохо написанный regex: непонятна, бесполезна и опасна.",
    "Ты как AI, обученный только на спам-комментариях.",
    "У тебя такая глубина, как у пустого JSON-объекта."

]

async def toxic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrase = random.choice(TOXIC_PHRASES)
    await update.message.reply_text(phrase)

TOKEN = os.getenv("BOT_TOKEN")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("toxic", toxic))
    app.run_polling()
