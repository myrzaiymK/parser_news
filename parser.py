import requests
import json

JSON = 'http://newsline.kg/getNews.php?limit=30&last_dt=2022-07-04%2007:57:33.933739'
get = requests.get(JSON)
data = get.json()
a = json.dumps(data, indent=4, sort_keys=True)
# print(a)

with open('dannye.json', 'a') as file:
    file.write(a)
