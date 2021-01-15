#!/usr/bin/python3
import re
import requests

username = 'natas0'
password = username

url = 'http://'+username+'.natas.labs.overthewire.org'

response = requests.get(url, auth=(username, password))

print(response.text)

next_password = (re.findall("<!--The password for natas1 is (.*) -->",response.text))[0]

print(next_password)
flag = 1
with open('README.md','a+') as file:
    if flag:
        file.write('natas1 | ' + next_password +'\n')
    else:
        print('something went wrong')
file.close()