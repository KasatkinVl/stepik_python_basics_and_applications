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

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком



r = requests.get("https://api.artsy.net/api/artists/{artists_ID}", headers=headers)
r.encoding = 'utf-8'
# разбираем ответ сервера
j = json.loads(r.text)


print(j)
# print(j['sortable_name'], j['birthday'])