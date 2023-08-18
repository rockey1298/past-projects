import re

from bs4 import BeautifulSoup
import requests, collections
from urllib import request
total = 0
collections.Callable = collections.abc.Callable

resp = request.urlopen("http://py4e-data.dr-chuck.net/regex_sum_1623340.txt")

data = resp.read()

html = data.decode("UTF-8")

print(html)

y = re.findall('[@]+',html)
print(y)
#for number in y:
#    total = total + int(number)
#print(total)
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
z = re.findall('^\S+?@\S+', x)
print(z)
