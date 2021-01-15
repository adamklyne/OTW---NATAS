#!/usr/bin/python3
import re
import requests
import base64

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/'%(username)
auth = (username, password)


print(url)
response = requests.get(url, auth=auth)
print(response.text)

encodedSecret = '3d3d516343746d4d6d6c315669563362'
decode = bytes.fromhex(encodedSecret)
print(decode[::-1])
decoded = base64.b64decode(decode[::-1])
print(decoded)
#print(secret)
payload = {'secret' : decoded, 'submit' : 'Submit'}
print(payload)

response = requests.post(url, auth=auth, data=payload)
print(response.text)
next_password = (re.findall("The password for natas9 is (.*)",response.text))[0]

print(next_password)




