# Emdee five for life
# Hackthebox web challenge
# 15/10/2020

#importing modules
import hashlib
from lxml import html
import requests
import re

# Getting the text for encryption from website
url = 'http://165.232.39.143:31906/' #HTB challenge link
r = requests.session()
page = r.get(url)
content = html.fromstring(page.content)
string = content.xpath('//h3/text()')
str1 = string[0]
print("The string to encrypt : ",str1)

# ENCRYPTED THE TEXT
hash = hashlib.md5(str1.encode()).hexdigest()
print("MD5 Encrypted string : ",hash)

# Sending the encrypted text into the website and submit
data = { 'hash' : hash }
x = r.post(url = url ,data = data)

# Getting the response and printing the flag
response = str(x.text)
flag = re.findall('HTB.*}',response)
if flag:
    print("The flag is : ",flag[0])
