
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from credits import bot_token
import sqlite3

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""Hello! You're welcome to the best Movie-Chat-Bot🎥!
Here you can find 1000 movies 🔥
Click /random to get random movie
Or write the title of movie and I will try to find it! 🎬 """)

async def send_info(update, context, row):
        info = f"""
📍Title of movie:   {row[2]}
📍Year:                   {row[3]}
📍Genres:              {row[4]}
📍Rating IMDB:      {row[5]}


🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻
{row[6]}
"""
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=row[1], caption=info)

async def random_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = sqlite3.connect("movie_database.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM movies ORDER BY RANDOM() LIMIT 1")
        row = cur.fetchall()[0]
        cur.close()
    await send_info(update, context, row)


app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("random", random_movie))

app.run_polling()
