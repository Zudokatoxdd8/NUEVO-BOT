import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix= "!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def conocer_sobre_reciclar(ctx):
    await ctx.send('El reciclaje trata de convertir residuos plásticos, la basura que consumimos diariamente, en nuevos productos o en materia prima para su posterior utilización, esto como una medida ante el creciente derroche de este material')

@bot.command()
async def caneca_roja(ctx):
    await ctx.send('En la bolsa roja se deben depositar únicamente para residuos hospitalarios y similares que contengan bacterias, parásitos, virus, hongos e infecciosos')

@bot.command()
async def caneca_verde(ctx):
    await ctx.send('Para depositar residuos orgánicos aprovechables como los restos de comida, desechos agrícolas etc')  

@bot.command()
async def caneca_negra(ctx):
    await ctx.send('Para depositar residuos no aprovechables como el papel higiénico; servilletas, papeles y cartones contaminados con comida') 

@bot.command()
async def clear(ctx, amount: int = 100):
    if amount > 100:
        amount = 100  # Discord permite borrar un máximo de 100 mensajes por vez
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f'{len(deleted)} mensajes eliminados', delete_after=1)

@bot.command()
async def roja(ctx):
    with open("images/roja.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def verde(ctx):
    with open("images/verde.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def negra(ctx):
    with open("images/negra.jpeg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



#token
bot.run('token')
