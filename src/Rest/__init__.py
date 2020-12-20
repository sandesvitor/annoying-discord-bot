import requests


insults_url = r'https://insult.mattbas.org/api/insult'


def get_random_insult():
    response = requests.get(insults_url)
    return response.text