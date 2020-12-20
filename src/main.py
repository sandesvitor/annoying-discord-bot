import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from itertools import cycle
import random
import os
import time

from deep_translator import GoogleTranslator
import Scrapper
import Rest

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
###          BOT EVENTS         ###
###################################

@client.event
async def on_ready():
    change_status.start()
    print("Logged in as {0}".format(client.user))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando Inválido!")


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
async def membros(ctx):
    print(ctx.author)
    print(ctx.channel)


@client.command()
async def amar(ctx):
    insult_en = Rest.get_random_insult()
    insult_pt = GoogleTranslator(source='en', target='pt').translate(insult_en)
    await ctx.send(insult_pt, tts=True)


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
    print("Commanded by user [{0}] of id [{1}]".format(ctx.author.name, ctx.author.id))
    print("---------------------------------------------------\n")
    await channel.connect()


@client.command(pass_content=True)
async def vaza(ctx):
    channel = ctx.author.voice.channel
    print("---------------------------------------------------")
    print("Vinícius is trying to leave voice channel:")
    print("Channel Name: {0}\nChannel Id: {1}".format(channel.name, channel.id))
    print("Commanded by user [{0}] of id [{1}]".format(ctx.author.name, ctx.author.id))
    print("---------------------------------------------------\n")
    server = ctx.message.guild.voice_client
    await server.disconnect()


@client.command(pass_content=True)
async def cancelado(ctx, keep_going=True):
    apology_en = Scrapper.get_apology()
    apology_pt = GoogleTranslator(source='en', target='pt').translate(apology_en)
    await ctx.send(apology_pt, tts=True)


###################################
###        COMMAND ERRORS       ###
###################################

@apagar.error
async def apagar_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltou especificar quantas linhas tu quer apagar, porra!")



client.run(os.getenv("TOKEN"))
