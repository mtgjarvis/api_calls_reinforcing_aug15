import requests
import json


res = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
body = json.loads(res.content)

# getting country
print(body[80])
print('')

legislatures_url = body[80]['legislatures'][0]['popolo_url']

print(legislatures_url)
print('')

guinea_bissau = requests.get('https://cdn.rawgit.com/everypolitician/everypolitician-data/addb879b07b17064d3d2c05f0d138cc216771cf7/data/Guinea-Bissau/Assembly/ep-popolo-v1.0.json')
gb_body = json.loads(guinea_bissau.content)

politician = gb_body['persons'][0]['name']

print(politician)
print('')

