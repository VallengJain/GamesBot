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

        if message.content.startswith('!news'):
            url = "https://stopgame.ru/news"
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

client = MyClient(intents=intents)
client.run('token')