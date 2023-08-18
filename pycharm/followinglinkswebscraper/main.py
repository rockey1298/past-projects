from bs4 import BeautifulSoup
import requests, collections
from urllib import request
wee = []
testing = []
total = 0
collections.Callable = collections.abc.Callable

# fucking around with urllib
resp = request.urlopen("http://py4e-data.dr-chuck.net/known_by_Hendri.html")
#print("taking a peek")
#print(resp.peek)
data = resp.read()
#print('printing data')
#print(type(data))
html = data.decode("UTF-8")


soup = BeautifulSoup(html, 'html.parser')

mylist = soup.find_all('a', href=True)
print('printing soup find all a href as mylist!')
print(mylist)

i = 0
#what would happen if we changed the l and mylist to the new website data ?
cool = 0

while cool < 7:
    print('start of while loop')
    for l in mylist:
        i += 1
        print('printing links!')
        print(l['href'])
        if i == 18 :
            # at the 3rd point, click on that link
            newresp = request.urlopen(l['href'])
            newdata = newresp.read()
            newhtml = newdata.decode("UTF-8")
            newsoup = BeautifulSoup(newhtml, 'html.parser')
            #print('printing newsoup')
            #print(newsoup)
            newlist = newsoup.find_all('a', href=True)
            print('printing newlist')
            print(newlist)
            mylist = mylist.clear()
            mylist = newlist
            i = 0
            cool += 1




#print(html)
#print(soup)

