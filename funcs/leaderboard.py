import nextcord


async def uprank(ctx, cur):
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


async def downrank(ctx, cur):
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
    print(result)
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
