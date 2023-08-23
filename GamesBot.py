import discord
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return


        catigories = ["all", "vr", "tech",
                      "pc", "xboxone", "xboxsx",
                      "ps4", "ps5", "stadia",
                      "nintendo", "mmo", "mobile",
                      "social", "fun", "industry",
                      "cybersport", "movies"]

        url_catigory = ["", "vr", "hard",
                        "pc", "xone", "xboxsx",
                        "ps4", "ps5", "stadia",
                        "nintendo_switch", "mmo", "mobile",
                        "social", "fun", "industry",
                        "cybersport", "movies"]


        for i in range(len(catigories)):
            if message.content.startswith(f"!news-{catigories[i]}"):
                url = "https://stopgame.ru/news/" + url_catigory[i]
                break
            else:
                continue


        if message.content.startswith('!news'):
            response = requests.get(url)
            text = response.text
            data = BeautifulSoup(text, 'html.parser')

            headings_list_view = data.find('div', class_='list-view')
            headings = headings_list_view.find_all('a', class_ ='_title_1tbpr_49')

            headings = headings[:3]
            response_text = "Новости: \n"

            for i in range(len(headings)):
                temp_response = headings[i]['href']
                response_text += "https://stopgame.ru" + temp_response + "\n"
            await message.channel.send(response_text)
        elif message.content.startswith('!help'):
            response_text = "Список команд: \n"

            for i in range(len(catigories)):
                response_text += f"!news-{catigories[i]}" + "\n"
            await message.channel.send(response_text)


client = MyClient(intents=intents)
client.run('MTE0MTYwODUxODg1Njc0NTAyMQ.GPT2qT.6A7oL9byHAu-A5advg98ushoTk4hSTxcK_cVU4')