import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command()
async def comoreciclounabotelladeplastico(ctx):
    await ctx.channel.send("usandolo como maceta")

@bot.command()
async def hola(ctx):
    await ctx.channel.send("hola soy pablo escobar y cuido el medioambiente")



@bot.command()
async def quemanualidadessepuedehacerconunabotelladeplastico(ctx):
    await ctx.channel.send("1:podrias hacer una maceta 2:podrias hacer una maraca 3:podrias hacer un comedero de animales")












bot.run("token")    
