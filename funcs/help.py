import nextcord


async def helpf(ctx):
    embed = nextcord.Embed(title="도움이 필요하신가요?", description="제가 친절하게 도와 드리죠, 후후\n참고: []내부의 인수는 선택입니다.", color=0x00e1ff)
    embed.add_field(name="\!이미지 [닉네임|멘션]", value="닉네임 or 멘션을 넘기면 그 사람의 이미지를 보여줍니다.\n\!이미지만 전송시 내 이미지를 보여줘여!",
                    inline=False)
    embed.add_field(name="\!떡상, \!떡락 (멘션)", value="말 안해도 알죠?", inline=False)
    embed.add_field(name="\!떡상랭킹, \!떡락랭킹", value="서버의 랭킹을 보여 줍니다", inline=False)
    embed.add_field(name="\!살까말까, \!할까말까", value="살지 말지, 할지 말지 고민? 뿌셔드립니다.", inline=False)
    embed.add_field(name="\!등록", value="내 정보를 DB에 등록한닷!", inline=False)
    embed.set_footer(text="※ 본 봇의 \!등록 커맨드를 사용하는경우 본인의 고유 ID및 닉네임을 DB에 저장합니다.")
    await ctx.channel.send(embed=embed)
