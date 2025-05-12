from twitchio.ext import commands

bot = commands.Bot(
    token="oauth:your_oauth_token_here",  # you can generate a new OAuth token at https://twitchtokengenerator.com/ 
    prefix="!",
    initial_channels=["your_channel_here"] # replace with your twitch channel name
)

# you can add more commands here(e.g. !socials, !about, etc.)
@bot.command(name="beer")
async def beer(ctx):
    await ctx.send("cheers! 🍻")

@bot.command(name="joke")
async def joke(ctx):
    await ctx.send("why did the scarecrow win an award? because he was outstanding in his field!")

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("hi! how are you?")

bot.run()