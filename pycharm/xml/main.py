import collections, xml.etree.ElementTree as ET
from urllib import request

from bs4 import BeautifulSoup

wee = []
testing = []
total = 0
collections.Callable = collections.abc.Callable

#  around with urllib
resp = request.urlopen("http://py4e-data.dr-chuck.net/comments_42.xml")
#print("taking a peek")
#print(resp.peek)
data = resp.read()
#print('printing data')
#print(type(data))
html = data.decode("UTF-8")

print(html)
soup = BeautifulSoup(html, 'html.parser')

mylist = soup.find_all('a', href=True)
print('printing soup find all a href as mylist!')
print(mylist)

stuff = ET.fromstring(html)
lst = stuff.findall('count')
print('User count:', len(lst))
for item in lst:
    print(item)






