import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import requests


client = commands.Bot(command_prefix='--')
status = cycle(
    [
        'Jogo da Vida', 
        'Catanzinho', 
        'Amongão Suave',
        'FF7 - Remake',
        'Residento Mau',
        'Churrasco',
        'Biriba'
    ]
)

coins = 0



###################################
###        MAIN FUNCTIONS       ###
###################################

def get_random_insult():
    response = requests.get(
        r"https://insult.mattbas.org/api/insult")
    return response.text

def post_annoying_song():
    pass


###################################
###          BOT EVENTS         ###
###################################

@client.event
async def on_ready():
    change_status.start()
    print("Logged in as {0}".format(client.user))

@client.event
async def on_member_join(member):
    print(f"{member} has join the server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server.")


###################################
###          BOT TASKS          ###
###################################

@tasks.loop(seconds=random.randint(60, 600))
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


###################################
###         BOT COMMANDS        ###
###################################

@client.command()
async def ping(ctx):
    await ctx.send(f"Latência: {round(client.latency * 1000)}ms")

@client.command()
async def inspirar(ctx):
    await ctx.send(get_random_insult())

@client.command()
@commands.has_permissions(manage_messages=True)
async def apagar(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def moeda(ctx):
    global coins
    coins += 1
    isPlural = "moedas" if coins > 1 else "moeda" 

    await ctx.send(
        f"Opa! Uma moedinha!\n" + 
        "#################################################\n" +
        f"# Vinícius está com {coins} {isPlural}\n" +
        "#################################################\n"
    )

@client.command()
async def roubar(ctx):
    global coins
    coins -= 1
    coins = 0 if coins <= 0 else coins
    isPlural = "moedas" if coins > 1 else "moeda" 
    prompt = f"Por que me roubastes!?" if coins > 0 else "Minha carteira já tá vazia, merda..."

    await ctx.send(
        f"{prompt}\n" + 
        "#################################################\n" +
        f"# Vinícius está com {coins} {isPlural}\n" +
        "#################################################\n"
    )

###################################
###        COMMAND ERRORS       ###
###################################

@apagar.error
async def apagar_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltou especificar quantas linhas tu quer apagar, porra!")



client.run(os.getenv("TOKEN"))
