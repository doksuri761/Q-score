import random


async def decider(ctx):
    if ctx.message.content == "!살까말까":
        await ctx.channel.send("인수 낸놔!")
    else:
        product = ctx.message.content.replace("!살까말까 ", "")
        msg = [f"민수 : {product}은(는) 당신을 원하고 있습니다.", "리하: 이눔!!! 그만사!!"]
        await ctx.channel.send(random.choice(msg))
