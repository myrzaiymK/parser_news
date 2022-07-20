import requests
import json
import datetime

with open('dannye.json', 'a') as file:
    file.write(a)

datetime = str(datetime.datetime.now()) 
JSON = 'http://newsline.kg/getNews.php?limit=30&last_dt=' + datetime
get = requests.get(JSON)
data = get.json()
a = json.dumps(data, indent=4, sort_keys=True)
# print(a)
