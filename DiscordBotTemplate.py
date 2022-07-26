import discord
from discord.ext import commands

#Change the command_prefix value to anything you'd like!
bot = commands.Bot(command_prefix='?', description="Description Here")

#Checks if the bot is online
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def info(ctx):
    await ctx.send('Describe the bot here!')

@bot.command()
async def stats(ctx, team):
    if team == "Kobras":
        await ctx.send("Korean Kobras: 0-0-0")
    elif team == "Badgers":
        await ctx.send("Boston Badgers: 0-0-0")
    elif team == "Villians":
        await ctx.send("Illest Villians: 0-0-0")
    elif team == "Pigeons":
        await ctx.send("New York Pigeons: 0-0-0")
    else:
        await ctx.send("Invalid team name")

bot.run('Blurred for obvious reasons')
