#!/usr/bin/python3
import re
import requests

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org' % (username)
print(url)
response = requests.get(url, auth=(username, password))

print(response.text)

next_password = (re.findall("<!--The password for natas2 is (.*) -->",response.text))[0]

print(next_password)
