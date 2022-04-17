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
    await updater.update(ctx, sock)


bot.run(token)
