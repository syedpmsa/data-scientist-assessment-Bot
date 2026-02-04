from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from rag.retriever import retrieve
from prompts import build_prompt
from llm import call_llm

BOT_TOKEN = "8248102492:AAGSfpssOacfHR0FyTtxvfdgdfsgs65ny12Dk_UBUSM"

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("Usage: /ask <your question>")
        return

    chunks = retrieve(query)
    context_text = "\n".join(chunks)
    prompt = build_prompt(context_text, query)

    answer = call_llm(prompt)
    await update.message.reply_text(answer)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/ask <question> - Ask from knowledge base\n"
        "/help - Show this help message"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("help", help_command))

print("🤖 Bot is running...")
app.run_polling()

