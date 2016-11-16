import json
import urllib.request
with urllib.request.urlopen('http://dibya.xyz:6969/current') as response:
   html = response.read()
   data = json.loads(html.decode("utf-8") )['data']

print(data)