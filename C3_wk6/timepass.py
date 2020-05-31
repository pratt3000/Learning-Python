import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')

uh = urllib.request.urlopen(url).read().decode()

info = json.loads(uh)

x = 0
for item in (info['comments']) :
    print('count', item['count'], type(item['count']))
    x = x + item['count']
print(x)