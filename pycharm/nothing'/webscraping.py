'''
import urllib.request, urllib.parse, urllib.error, collections
from bs4 import BeautifulSoup
import ssl
# Ignore ssl errors http://py4e-data.dr-chuck.net/comments_1623342.html
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# wtf
collections.Callable = collections.abc.Callable



url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# retrieving all the anchor tags

tags = soup.findAll('span')
for tag in tags:
    print(tag)
    #find = tag[22:25]
    #print(find)

print('lol shit')
'''

from bs4 import BeautifulSoup
import requests, collections
newlist = []
wee = []
testing = []
total = 0
collections.Callable = collections.abc.Callable


url = "http://py4e-data.dr-chuck.net/comments_1623342.html"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
mylist = soup.find_all('span')
#printing out all the span objects
print(mylist)
#looping through my list of span objects, unsure of how to work with the object to get just numbers.
# looping through soup object, printing them out, and then adding them as strings to new list
for list in mylist:
    print(list)
    newlist.append(str(list))
#now in my newlist i am splitting out the number from the span, finding problems with splitting double and single digit numbers
for l in newlist:
    print(l[23:25])
    a = l[23:25]
    if a.endswith('<'):
        print(a)
        a = a[0]
        print(a)
    '''
    for a in l:
        if a.isdigit():
            print("youve done it: " + a)
            testing.append(a)
    '''

    wee.append(a)

for test in testing:
    print('testing: ' + test)


# not working, wee is the list of numbers from the spans but single digits are fucking it up
for w in wee:
    total = total + int(w)
    print(total)
print('your total is: ' + str(total))



