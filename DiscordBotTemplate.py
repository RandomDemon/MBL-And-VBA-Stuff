import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?', description="Description Here")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def info(ctx):
    await ctx.send('Stat Bot for the MBL Discord Server')

@bot.command()
async def stats(ctx, team):
    if team == "Kobras":
        await ctx.send("Kobras: 4-2-1")
    elif team == "Badgers":
        await ctx.send("Badgers: 1-5-1")
    elif team == "Villians":
        await ctx.send("Villians: 6-1-0")
    elif team == "Pigeons":
        await ctx.send("Pigeons: 3-4-0")
    else:
        await ctx.send("Invalid team name")

bot.run('Put your token here')
