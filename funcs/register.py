async def register(ctx, cur, db):
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
