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

gender = json['data']['gender']
print(gender)
email = json['data']['email']
print(email)
age =json['data']['dob']['age'] 
print(age)
username = json['data']['login']['username']
print(username)
phone= json['data']['phone']
print(phone)


