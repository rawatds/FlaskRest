import requests

BASE_URL = "http://127.0.0.1:5000/"

videolist = [
    {'name': 'Lets Python', 'likes': 30, 'views': 150},
    {'name': 'Lets C', 'likes': 60, 'views': 153330},
    {'name': 'Lets C++', 'likes': 70, 'views': 23150}
]

print("Adding 3 ------")
for i in range(len(videolist)):
    response = requests.post(BASE_URL + "videos/" + str(i), videolist[i])
    print(response.json())

print("Get vid : 2")
input()
response = requests.get(BASE_URL + "videos/2")
print(response.json())

print("Del vid : 2")
input()
response = requests.delete(BASE_URL + "videos/2")
print(response)

print("Get vid : 2")
input()
response = requests.get(BASE_URL + "videos/2")
print(response.json())

#print(response.status_code)
# print(response.text)
# print(response.json())


print("Get all")
input()
response = requests.get(BASE_URL + "videos")
print(response)
