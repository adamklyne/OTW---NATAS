#!/usr/bin/python3
import re
import requests

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % (username)
auth = (username, password)

print(url)

response = requests.get(url, auth=auth)

print(response.text)



next_password = (re.findall("natas4:(.*)",response.text))[0]

print(next_password)
