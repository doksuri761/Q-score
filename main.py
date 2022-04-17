# Developed by dgm
import os
import socket
import sqlite3
from os import getenv

from dotenv import load_dotenv
from nextcord.ext.commands import Bot

from funcs import image, leaderboard, register, updater

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
env = load_dotenv(".env")
is_test = getenv("is_test", default=None)

if is_test is None:
    token = getenv("token")
else:
    token = getenv("test_token")
db = sqlite3.connect("image.db")
cur = db.cursor()
bot = Bot(command_prefix="!")


@bot.event
async def on_ready():
    sock.sendto(str(os.getpid()).encode(), ('127.0.0.1', 8080))
    print("ready!")


@bot.command()
async def 떡상랭킹(ctx):
    await leaderboard.uprank(ctx, cur)


@bot.command()
async def 떡락랭킹(ctx):
    await leaderboard.downrank(ctx, cur)


@bot.command()
async def 등록(ctx):
    await register.register(ctx, cur, db)


@bot.command()
async def 떡락(ctx):
    await image.down(ctx, cur, db)


@bot.command()
async def 떡상(ctx):
    await image.up(ctx, cur, db)


@bot.command()
async def 이미지(ctx):
    await image.get_image(ctx, cur)


@bot.command()
async def update(ctx):
    await updater.update(ctx, sock, bot)


@bot.command()
async def sql(ctx):
    if ctx.author.id == 720435385703858297:
        sql = ctx.message.content.replace("!sql ", "")
        cur.execute(sql)
        db.commit()
        await ctx.channel.send("committed.")
    else:
        await ctx.send("동건맨 아니잖슴 ㅡㅡ")


@bot.command()
async def sqlc(ctx):
    if ctx.author.id == 720435385703858297:
        sql = ctx.message.content.replace("!sqlc ", "")
        cur.execute(sql)
        await ctx.channel.send(cur.fetchall())
    else:
        await ctx.send("동건맨 아니잖슴 ㅡㅡ")


@bot.command()
async def 깃허브(ctx):
    embed = nextcord.Embed(title="깃헙 링크는 여기.")
    embed.add_field(name="99덕 파티 공식 깃헙", value="https://github.com/99duck-discord/99duck-bot", inline=False)
    embed.add_field(name="ㄷㄱㅁ 개인 깃헙", value="https://github.com/doksuri761/Q-score", inline=True)
    await ctx.send(embed=embed)


bot.run(token)
