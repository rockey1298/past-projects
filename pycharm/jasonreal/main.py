import collections, urllib
import json
from urllib import request

from bs4 import BeautifulSoup

collections.Callable = collections.abc.Callable
total = 0

resp = request.urlopen("http://py4e-data.dr-chuck.net/comments_1623345.json")
data = resp.read()
html = data.decode()
#print(html)

js = json.loads(data)
print(json.dumps(js))
# comments is the list of dict in js
for c in js["comments"]:
    print(c['count'])
    cadd = c['count']
    total = cadd + total
print(total)