# Developed by dgm
import asyncio
import os
import nextcord
import sys
from dotenv import load_dotenv
from os import getenv
from nextcord.ext.commands import Bot
import sqlite3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
env = load_dotenv(".env")
is_test = False

if not is_test:
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
    sql = "select * from user"
    cur.execute(sql)
    data = cur.fetchall()
    data.sort(reverse=True)
    result = {}
    prize = {}
    for rank, people in data:
        if rank in result:
            result[rank].append(people)
        else:
            result[rank] = [people]
    print(result)
    index = 1
    embed = nextcord.Embed(title=f"{ctx.guild.name}의 이미지 리더보드", description="누가누가 더 높을까??", color=0xff0000)
    for i in list(result.keys()):
        users = result.get(i)
        temp = ""
        for k in users:
            temp += k + ", "
        embed.add_field(name=f"{index}등{'!' * (5 - index)}", value=f"{temp[:-2]}\n{i}점!", inline=False)
        prize[index] = users
        next_index = index + 1 if len(users) == 1 else index + 2
        if next_index > 5:
            break
        else:
            index = next_index
    await ctx.send(embed=embed)


@bot.command()
async def 떡락랭킹(ctx):
    sql = "select * from user"
    cur.execute(sql)
    data = cur.fetchall()
    data.sort(reverse=False)
    result = {}
    prize = {}
    for rank, people in data:
        if rank in result:
            result[rank].append(people)
        else:
            result[rank] = [people]
    index = 1
    embed = nextcord.Embed(title=f"{ctx.guild.name}의 이미지 리더보드", description="누가누가 더 낮을까??", color=0xff0000)
    for i in list(result.keys()):
        users = result.get(i)
        temp = ""
        for k in users:
            temp += k + ", "
        embed.add_field(name=f"{index}등{'!' * (5 - index)}", value=f"{temp[:-2]}\n{i}점!", inline=False)
        prize[index] = users
        next_index = index + 1 if len(users) == 1 else index + 2
        if next_index > 5:
            break
        else:
            index = next_index
    await ctx.send(embed=embed)


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
        await ctx.channel.send(nick + "님의 이미지가 1 떡락했어요.")


@bot.command()
async def 떡상(ctx):
    nick = ctx.message.content.replace("!떡상 ", "")
    if ctx.author.display_name == nick:
        await ctx.channel.send("으디서 스스로 이미지를 올려!")
    else:
        sql = f"select * from user where(nick=\"{ctx.author.display_name}\")"
        cur.execute(sql)
        query = cur.fetchone()
        if query is None:
            await ctx.channel.send("일단 \!등록부터 하고 오셔~")
        else:

            sql = f"select * from user where(nick=\"{nick}\")"
            cur.execute(sql)
            query = cur.fetchone()
            sql = f"update user set image={query[0] + 1} where(nick=\"{nick}\")"
            cur.execute(sql)
            db.commit()
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


@bot.command()
async def ver(ctx):
    await ctx.channel.send("update2 ver.")


@bot.command()
async def update(ctx):
    if ctx.author.id == 720435385703858297:
        await ctx.channel.send("모든 명령어를 삭제 중입니다.")
        for i in bot.commands:
            bot.remove_command(i.name)
        await ctx.channel.send("업데이트 중에는 봇 이용이 불가능합니다.")
        db.commit()
        db.close()
        await asyncio.sleep(10)
        sock.sendto("update".encode(), ("127.0.0.1", 8080))
        await bot.close()
    else:
        await ctx.channel.send("동건맨 아니면 업뎃 못함 ㅅㄱ")


bot.run(token)
