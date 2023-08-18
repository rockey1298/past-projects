from bs4 import BeautifulSoup
import requests, collections
from urllib import request
newlist = []
wee = []
testing = []
total = 0
collections.Callable = collections.abc.Callable

# fucking around with urllib
resp = request.urlopen("http://py4e-data.dr-chuck.net/comments_1623342.html")
#print("taking a peek")
#print(resp.peek)
data = resp.read()
#print('printing data')
#print(type(data))
html = data.decode("UTF-8")
#print(html)

soup = BeautifulSoup(html, 'html.parser')
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