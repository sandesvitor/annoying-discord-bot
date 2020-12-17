import discord
import os
import requests
# import json

client = discord.Client()

def get_random_insult():
    response = requests.get(r"https://insult.mattbas.org/api/insult")
    return response.text

def post_annoying_song():
    pass


@client.event
async def on_ready():
    print("Logged in as {0}".format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("--help"):
        await message.channel.send(
            "Eu sou o Vinny Babaquetti! Hoje vocês terão o prazer de interagir com minha pessoa. Meus comandos mágicos são:\n" +
            "\n" +
            "1) '--help' : para o qual repetirás esta mesma merda!\n" +
            "2) '--inspira' : ofereço-lhe meus humildes dois centavos sobre vossa pessoa!\n"
        )


    if message.content.startswith("--inspira"):
        await message.channel.send(get_random_insult())

client.run(os.getenv("TOKEN"))