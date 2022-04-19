import random


async def up(ctx, cur, db):
    nick = int(ctx.message.content.replace("!떡상 ", "")[2:-1])
    if nick != ctx.author.id:
        sql = f"select * from user where(user_id=\"{ctx.author.display_name}\")"
        cur.execute(sql)
        query = cur.fetchone()
        if query is None:
            await ctx.channel.send("일단 \!등록부터 하고 오셔~")
        else:

            sql = f"select * from user where(user_id=\"{nick}\")"
            cur.execute(sql)
            query = cur.fetchone()
            sql = f"update user set image={query[0] + 1} where(user_id=\"{nick}\")"
            cur.execute(sql)
            db.commit()
            await ctx.channel.send(query[1] + "님의 이미지가 1 떡상했어요.")
    else:
        await ctx.channel.send("님 양심 없?")


async def down(ctx, cur, db):
    nick = int(ctx.message.content.replace("!떡락 ", "")[2:-1])
    if nick != ctx.author.id:
        sql = f"select * from user where(user_id=\"{ctx.author.display_name}\")"
        cur.execute(sql)
        query = cur.fetchone()
        if query is None:
            await ctx.channel.send("일단 \!등록부터 하고 오셔~")
        else:
            sql = f"select * from user where(user_id=\"{nick}\")"
            cur.execute(sql)
            query = cur.fetchone()
            amount = random.randint(1, 100)
            if 81 > amount > 0:
                sql = f"update user set image={query[0] - 1} where(user_id=\"{nick}\")"
                cur.execute(sql)
                db.commit()
                await ctx.channel.send(query[1] + "님의 이미지가 80% 확률에 의하여 1 떡락했어요.")
            elif 91 > amount < 81:
                sql = f"update user set image={query[0] - 2} where(user_id=\"{nick}\")"
                cur.execute(sql)
                db.commit()
                await ctx.channel.send(query[1] + "님의 이미지가 10% 확률에 의하여 2 떡락했어요.")
            elif 96 > amount > 91:
                sql = f"update user set image={query[0] - 3} where(user_id=\"{nick}\")"
                cur.execute(sql)
                db.commit()
                await ctx.channel.send(query[1] + "님의 이미지가 5% 확률에 의하여 3 떡락했어요.")
            elif 99 > amount > 96:
                sql = f"update user set image={query[0] - 4} where(user_id=\"{nick}\")"
                cur.execute(sql)
                db.commit()
                await ctx.channel.send(query[1] + "님의 이미지가 3% 확률에 의하여 4 떡락했어요.")
            elif amount == 100:
                sql = f"update user set image={query[0] - 5} where(user_id=\"{nick}\")"
                cur.execute(sql)
                db.commit()
                await ctx.channel.send(query[1] + "님의 이미지가 1% 확률에 의하여 5 떡락했어요.")
            else:
                sql = f"update user set image={query[0] - 1} where(user_id=\"{nick}\")"
                cur.execute(sql)
                db.commit()
                await ctx.channel.send(query[1] + "님의 이미지가 80% 확률에 의하여 1 떡락했어요.")
    else:
        await ctx.channel.send("님 양심 없?")


async def get_image(ctx, cur):
    nick = ctx.message.content.replace("!이미지", "")
    if nick == "":
        sql = f"select * from user where(user_id=\"{ctx.author.display_name}\")"
        cur.execute(sql)
        query = cur.fetchone()
        await ctx.channel.send(ctx.author.mention + f"님의 이미지는 {query[0]}입니다.")
    elif nick.find("@") == 1:
        nick = nick[2:-1]
        sql = f"select * from user where(user_id=\"{nick}\")"
        cur.execute(sql)
        query = cur.fetchone()
        await ctx.channel.send(query[1].capitalize() + f"님의 이미지는 {query[0]}입니다.")
    else:
        sql = f"select * from user where(user_id=\"{nick}\")"
        cur.execute(sql)
        query = cur.fetchone()
        await ctx.channel.send(query[1].capitalize() + f"님의 이미지는 {query[0]}입니다.")
