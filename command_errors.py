@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, MissingPermissions):
        embed = discord.Embed(title=f"", description=f"> {ctx.author.name}, You are missing permissions!", colour=0xff4a4a)
        await ctx.send(embed=embed)

    if isinstance(error, MissingRequiredArgument):
        embed = discord.Embed(title=f"", description=f"> {ctx.author.name}, You are missing required arguments", colour=0xff4a4a)
        await ctx.send(embed=embed)

    if isinstance(error, CommandNotFound):
        embed = discord.Embed(title=f"", description=f"> {ctx.author.name}, Command was not found!", colour=0xff4a4a)
        await ctx.send(embed=embed)

    if isinstance(error, NoPrivateMessage):
        embed = discord.Embed(title=f"", description=f"> {ctx.author.name}, This command is disabled in DM.", colour=0xff4a4a)
        await ctx.send(embed=embed)

    if isinstance(error, CommandOnCooldown):
        embed = discord.Embed(title=f"", description=f"> {ctx.author.name}, This command is currently on cooldown.", colour=0xff4a4a)
        await ctx.send(embed=embed)

    if isinstance(error, MissingRole):
        embed = discord.Embed(title=f"", description=f"> {ctx.author.name}, You dont have the required role.", colour=0xff4a4a)
        await ctx.send(embed=embed)

    if isinstance(error, CommandInvokeError):
        embed = discord.Embed(title=f"", description=f"> {ctx.author.name}, Uncaptured issue!", colour=0xff4a4a)
        await ctx.send(embed=embed)