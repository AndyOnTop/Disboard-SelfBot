from andyontop import *
from discord.ext import commands
import discord
import time

token = input("Whats your token? (Without quotation marks)")
bot = commands.Bot("/--/", self_bot=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ducchub")) # You can delete this line or change ducchub to your server name, its just a custom status
    andyontop = ascii('Andy On Top')
    print(andyontop)

@bot.command()
async def bump(ctx):
    print("Starting")
    while True:
        await ctx.send('!d bump')
        time.sleep(7260)

bot.run(token, bot=False)