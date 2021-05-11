try:
    from discord.ext import commands
    import discord
    import asyncio
    from time import sleep
    from random import randint
    import config
    from os import system
except ImportError:
    print("Trying to install the required modules! THIS MAY DISPLAY LARGE ERRORS!\nPlease try to run this script again once all of the modules have been successfully installed.\n")
    input("Press enter to start installing... ")
    system("py -m pip install -r requirements.txt")
    system("python -m pip install -r requirements.txt")
    system("python3 -m pip install -r requirements.txt")
    input("\n\nDone installing modules! please restart the script now. Press enter to continue... ")
    quit()

bot = commands.Bot(config.preifx, self_bot=True)

@bot.event
async def on_ready():
    print("""
           _   _ _______     __   ____  _   _   _______ ____  _____  
     /\   | \ | |  __ \ \   / /  / __ \| \ | | |__   __/ __ \|  __ \ 
    /  \  |  \| | |  | \ \_/ /  | |  | |  \| |    | | | |  | | |__) |
   / /\ \ | . ` | |  | |\   /   | |  | | . ` |    | | | |  | |  ___/ 
  / ____ \| |\  | |__| | | |    | |__| | |\  |    | | | |__| | |     
 /_/    \_\_| \_|_____/  |_|     \____/|_| \_|    |_|  \____/|_|    
                            Credits:
                       Andy: (andylol#1234)
              Thanks to omens for anti selfbot detection
    """)
    if config.stream:
        await bot.change_presence(activity=discord.Streaming(name="Andy On Top", url=""))

@bot.command()
async def bump(ctx):
    print('Auto bump started')

    async def sendMsg(msg):
        async with ctx.typing():
            await asyncio.sleep(randint(3, 7))
        await ctx.send(msg)

    while True:
        await sendMsg(config.disboard_prefix + " bump")
        sleep(int(config.wait_time))

bot.run(config.token, bot=False)