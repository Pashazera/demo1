import requests
import urllib.request as ur
from bs4 import BeautifulSoup
import json
import pandas as pd


BASE_PLAYER_URL = 'https://csgo.5eplay.com/api/data/rank/player?page=1&range=&major=1'
BASE_DATA_URL = 'https://csgo.5eplay.com/data/player/'
def getPlayer():
    player = []
    for i in range(1, 6):
        url = BASE_PLAYER_URL.replace('page=1', 'page=' + str(i))
        r = requests.get(url)
        state = json.loads(r.text).get('data')

        for x in state:
            player.append(x['player_tag'])
    return player


def getMap(play_list):
    map_list = []
    for player in play_list:
        url = BASE_DATA_URL + player
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, 'lxml')
        datalist1 = soup.findAll(name='p', attrs={'class': {'map-name tcenter font-industry'}})
        datalist2 = soup.findAll(name='div', attrs={'class': 'detail floatl ml40'})
        for x, y in zip(datalist1, datalist2):
            map = x.get_text()
            data = list(filter(None, y.get_text().split('\n')))
            total_number = data[1]
            rating = data[3]
            map_list.append([player,map,total_number,rating])
    return map_list


play_list = getPlayer()
map_list = getMap(play_list)
df = pd.DataFrame(data=map_list,columns=['player','map','total_number','rating'],index=None)
df.to_excel('player.xlsx')

# url = 'https://csgo.5eplay.com/data/player/s1mple'
# response = requests.get(url)
# content = response.content
#
# soup = BeautifulSoup(content,'lxml')
# datalist = soup.findAll(attrs={'class':'map-name tcenter font-industry'})
# datalist1 = soup.findAll(name='p',attrs={'class':{'map-name tcenter font-industry'}})
# datalist2 = soup.findAll(name='div',attrs={'class':'detail floatl ml40'})
#
#
# for x ,y in zip(datalist1,datalist2):
#     #print(x.get_text(),list(filter(None,y.get_text().split('\n'))))
#     map = x.get_text()
#     data = list(filter(None,y.get_text().split('\n')))
#     total_number = data[1]
#     rating = data[3]
#     print(map,total_number,rating)