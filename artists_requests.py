import requests
import json

########### Get a Token ############
client_id = 'aacb9458bc44eadf6980'
client_secret = '5679b580f27349b7b9831290fe6dd8f7'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]


########### Request ############
artist_dict = {}

with open("C:\\Users\\User\\Downloads\\dataset_24476_4.txt") as data:
    artists = data.read().splitlines()

for i in artists:

    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token" : token}

    # инициируем запрос с заголовком
    api_url = "https://api.artsy.net/api/artists/{}"
    artists_url = api_url.format(i)

    r = requests.get(artists_url, headers=headers)
    r.encoding = 'utf-8'

    # разбираем ответ сервера
    j = json.loads(r.text)

    artist_dict[j['sortable_name']] = j['birthday']
    # print(j)

    buff = sorted(artist_dict.items(), key=lambda x: (x[1], x[0]))

for i in range(len(buff)):
    print(buff[i][0])
