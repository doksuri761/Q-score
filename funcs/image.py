import random


async def up(ctx, cur, db):
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
        await ctx.channel.send(nick + "님의 이미지가 1 떡상했어요.")


async def down(ctx, cur, db):
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
        amount = random.randint(1, 100)
        if 81 > amount > 0:
            sql = f"update user set image={query[0] - 1} where(nick=\"{nick}\")"
            cur.execute(sql)
            db.commit()
            await ctx.channel.send(nick + "님의 이미지가 80% 확률에 의하여 1 떡락했어요.")
        elif 91 > amount < 81:
            sql = f"update user set image={query[0] - 2} where(nick=\"{nick}\")"
            cur.execute(sql)
            db.commit()
            await ctx.channel.send(nick + "님의 이미지가 10% 확률에 의하여 2 떡락했어요.")
        elif 96 > amount > 91:
            sql = f"update user set image={query[0] - 3} where(nick=\"{nick}\")"
            cur.execute(sql)
            db.commit()
            await ctx.channel.send(nick + "님의 이미지가 5% 확률에 의하여 3 떡락했어요.")
        elif 99 > amount > 96:
            sql = f"update user set image={query[0] - 4} where(nick=\"{nick}\")"
            cur.execute(sql)
            db.commit()
            await ctx.channel.send(nick + "님의 이미지가 3% 확률에 의하여 1 떡락했어요.")
        elif amount == 100:
            sql = f"update user set image={query[0] - 5} where(nick=\"{nick}\")"
            cur.execute(sql)
            db.commit()
            await ctx.channel.send(nick + "님의 이미지가 1% 확률에 의하여 5 떡락했어요.")
        else:
            sql = f"update user set image={query[0] - 1} where(nick=\"{nick}\")"
            cur.execute(sql)
            db.commit()
            await ctx.channel.send(nick + "님의 이미지가 80% 확률에 의하여 1 떡락했어요.")


async def get_image(ctx, cur):
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