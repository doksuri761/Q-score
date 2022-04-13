# Developed by dgm
from dotenv import load_dotenv
from os import getenv
from nextcord.ext.commands import Bot
import sqlite3

env = load_dotenv(".env")
token = getenv("token")
db = sqlite3.connect("image.db")
cur = db.cursor()
bot = Bot(command_prefix="!")


@bot.command()
async def 등록(ctx):
    sql = f"select * from user where(nick=\"{ctx.author.display_name}\")"
    cur.execute(sql)
    fetch = cur.fetchone()
    if fetch is None:
        sql = f"insert into user values(0, \"{ctx.author.display_name}\")"
        cur.execute(sql)
        db.commit()
        await ctx.channel.send(ctx.author.mention + "님의 이미지 컬럼이 생성되었어요.")
    else:
        await ctx.channel.send("이미 등록 되어 있는데요?")


@bot.command()
async def 떡락(ctx):
    sql = f"select * from user where(nick=\"{ctx.author.display_name}\")"
    cur.execute(sql)
    query = cur.fetchone()
    if query is None:
        await ctx.channel.send("일단 \!등록부터 하고 오셔~")
    else:
        nick = ctx.message.content.replace("!떡락 ", "")
        sql = f"select * from user where(nick=\"{nick}\")"
        cur.execute(sql)
        query = cur.fetchone()
        sql = f"update user set image={query[0] - 1} where(nick=\"{nick}\")"
        cur.execute(sql)
        db.commit()
        print(query)
        await ctx.channel.send(nick + "님의 이미지가 1 떡락했어요.")


@bot.command()
async def 떡상(ctx):
    sql = f"select * from user where(nick=\"{ctx.author.display_name}\")"
    cur.execute(sql)
    query = cur.fetchone()
    if query is None:
        await ctx.channel.send("일단 \!등록부터 하고 오셔~")
    else:
        nick = ctx.message.content.replace("!떡상 ", "")
        sql = f"select * from user where(nick=\"{nick}\")"
        cur.execute(sql)
        query = cur.fetchone()
        sql = f"update user set image={query[0] + 1} where(nick=\"{nick}\")"
        cur.execute(sql)
        db.commit()
        print(query)
        await ctx.channel.send(nick + "님의 이미지가 1 떡상했어요.")


@bot.command()
async def 이미지(ctx):
    nick = ctx.message.content.replace("!이미지", "")
    if nick == "":
        sql = f"select * from user where(nick=\"{ctx.author.display_name}\")"
        cur.execute(sql)
        query = cur.fetchone()
        await ctx.channel.send(ctx.author.mention + f"님의 이미지는 {query[0]}입니다.")
    else:
        sql = f"select * from user where(nick=\"{nick[1:]}\")"
        cur.execute(sql)
        query = cur.fetchone()
        await ctx.channel.send(nick.capitalize() + f"님의 이미지는 {query[0]}입니다.")


bot.run(token)
