import asyncio
import sys


async def update(ctx, sock, bot):
    if ctx.author.id == 720435385703858297:
        await ctx.channel.send("모든 명령어를 삭제 중입니다.")
        for i in bot.commands:
            bot.remove_command(i.name)
        await ctx.channel.send("업데이트 중에는 봇 이용이 불가능합니다.")
        await asyncio.sleep(10)
        sock.sendto("update".encode(), ("127.0.0.1", 8080))
        sys.exit(1)
    else:
        await ctx.channel.send("동건맨 아니면 업뎃 못함 ㅅㄱ")
