import collections, urllib
import json
import ssl
from urllib import request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

from bs4 import BeautifulSoup

collections.Callable = collections.abc.Callable
total = 0

resp = urllib.request.urlopen("http://py4e-data.dr-chuck.net/json?", context=ctx)
data = resp.read()
html = data.decode()

parms = dict()
parms['address'] = 'Technion'
parms['key'] = 42

url = 'http://py4e-data.dr-chuck.net/json?' + urllib.parse.urlencode(parms)

print(url)

resp = urllib.request.urlopen(url, context=ctx)
data = resp.read()
html = data.decode()
print(html)





