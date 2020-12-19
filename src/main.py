import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from itertools import cycle
import random
import os
import requests
import json
import time

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

shut_ups = [
    "por favor, cala a boca.",
    "sério, não aguento mais!",
    "cale-se, maldição!",
    "morra, seu verme falador..."
]

coins = 0



###################################
###        MAIN FUNCTIONS       ###
###################################

def get_random_insult():
    response = requests.get(
        r'http://xinga-me.appspot.com/api')
    json_data = json.loads(response.text)
    quote = "Aqui vai: " + json_data["xingamento"] + "!\n"
    return quote

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

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando Inválido!")

# @client.event
# async def on_message(message):
#     if (message.author == client.user):
#         return
    
#     shut_up_index = random.randint(0, (len(shut_ups) - 1))
#     await message.channel.send("{0}, {1}".format(message.author, shut_ups[shut_up_index]), tts=True)


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
    await ctx.send(f"Latência: {round(client.latency * 1000)}ms", tts=True)

@client.command()
async def amar(ctx):
    await ctx.send(get_random_insult(), tts=True)

@client.command()
@commands.has_permissions(manage_messages=True)
async def apagar(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def pagar(ctx, amount=1):
    global coins
    coins += amount
    isPlural = "moedas" if coins > 1 else "moeda" 

    await ctx.send(
        f"Opa! Uma moedinha!\n" + 
        "+----------------->\n" +
        "|\n" +
        f"|\tVinícius está com {coins} {isPlural}\n" +
        "|\n"
        "+----------------->\n"
    )

@client.command()
async def roubar(ctx, amount=1):
    global coins
    coins -= amount
    coins = 0 if coins <= 0 else coins
    isPlural = "moedas" if coins > 1 else "moeda" 
    prompt = f"Por que me roubastes!?" if coins > 0 else "Minha carteira já tá vazia, merda..."

    await ctx.send(
        f"{prompt}\n" + 
        "+----------------->\n" +
        "|\n"
        f"|\tVinícius está com {coins} {isPlural}\n" +
        "|\n"
        "+----------------->\n"
    )

@client.command(pass_content=True)
async def entra(ctx):
    channel = ctx.author.voice.channel
    print("---------------------------------------------------")
    print("Vinícius is trying to enter voice channel:")
    print("Channel Name: {0}\nChannel Id: {1}".format(channel.name, channel.id))
    print("---------------------------------------------------\n")
    await channel.connect()

@client.command(pass_content=True)
async def vaza(ctx):
    channel = ctx.author.voice.channel
    print("---------------------------------------------------")
    print("Vinícius is trying to leave voice channel:")
    print("Channel Name: {0}\nChannel Id: {1}".format(channel.name, channel.id))
    print("---------------------------------------------------\n")
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command(pass_content=True)
async def babaca(ctx, keep_going=True):
    while keep_going == True:
        # time.sleep(0.5)
        await ctx.send("Eu sou um merda")


###################################
###        COMMAND ERRORS       ###
###################################

@apagar.error
async def apagar_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltou especificar quantas linhas tu quer apagar, porra!")


client.run(os.getenv("TOKEN"))
