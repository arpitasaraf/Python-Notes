import requests

url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'

response = requests.get(url)
jsonData = response.json() # converting response data into json 
# print(jsonData)

success = jsonData['success']
message =jsonData['message']

name = jsonData['data']['name']['first'] + ' ' + jsonData['data']['name']['last']
location = str(jsonData['data']['location']['street']['number']) + ' ' + str(jsonData['data']['location']['street']['name']) +  jsonData['data']['location']['city'] + ' ' + jsonData['data']['location']['state'] + ' ' +jsonData['data']['location']['country'] + ' ' + str(jsonData['data']['location']['postcode'])
# print(success)
# print(message)
# print(name)
print(location)