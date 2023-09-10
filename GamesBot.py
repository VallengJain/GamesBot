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
        
        url_news = "https://stopgame.ru/news/"
        url_games = "https://stopgame.ru/games/"

#Вывод новстей
        catigories = ["all", "vr", "hard",
                      "pc", "xone", "xboxsx",
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
                url_news = "https://stopgame.ru/news/" + url_catigory[i]
                break
            else:
                continue


        if message.content.startswith('!news'):
            response_news = requests.get(url_news)
            text_news = response_news.text
            data_news = BeautifulSoup(text_news, 'html.parser')

            headings_list_view = data_news.find('div', class_ = 'list-view')
            headings_news = headings_list_view.find_all('a', class_ ='_title_1tbpr_49')

            headings_news = headings_news[:3]
            response_text = "Новости: \n"

            for i in range(len(headings_news)):
                temp_response = headings_news[i]['href']
                response_text += "https://stopgame.ru" + temp_response + "\n"
            await message.channel.send(response_text)
#Вывод списка комманд
        elif message.content.startswith('!help'):
            response_text = "Список команд: \n!help \n"

            for i in range(len(catigories)):
                response_text += f"!news-{catigories[i]}" + "\n"
            await message.channel.send(response_text)
#Вывод игр
        elif message.content.startswith('!games'):
            response_games = requests.get(url_games)
            text_games = response_games.text
            data_games = BeautifulSoup(text_games, 'html.parser')

            headings_games_list = data_games.find('div', class_ = '_main-grid_zxw47_315')
            headings_all_games = headings_games_list.find_all('div', class_ = '_main-block_zxw47_321')

            if message.content.startswith('!games-AAA') or message.content.startswith('!games-aaa'):
                for i in range(len(headings_all_games)):
                    if 'ААА ждём' in headings_all_games[i].text:
                        headings_games = headings_all_games[i]
                        break
                    else:
                        continue

            games = headings_games.find_all('a', class_ = '_card_1vde2_1')
            games = games[:3]
            response_text = "Игры: \n"

            for i in range(len(games)):
                temp_response = games[i]['href']
                response_text += "https://stopgame.ru" + temp_response + "\n"
            await message.channel.send(response_text)         


client = MyClient(intents=intents)
client.run('token')