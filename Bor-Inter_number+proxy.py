import requests

proxies = {
  'http': 'http://185.239.239.252:3128',
  'https': 'http://88.198.24.108:8080',
}
with open("C:\\Users\\User\\Downloads\\dataset_24476_3.txt") as data:
    numbers = data.read().splitlines()

for i in numbers:

    api_url = 'http://numbersapi.com/{}/math?json=true'
    number_url = api_url.format(int(i))

    res = requests.get(number_url, proxies=proxies)
    info = res.json()

    if info["found"] == True:
        print("Interesting")
    else:
        print("Boring")

# import requests as re
#
# with open('dataset_24476_3.txt') as file:
#     for num in file:
#         response = re.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()﻿
#         ﻿
#         print('Interesting') if response['found'] else print('Boring')﻿