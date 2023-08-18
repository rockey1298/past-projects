import urllib.request, urllib.parse, urllib.error
import xml
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = 'http://py4e-data.dr-chuck.net/comments_1623344.xml'
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print('data decode', data.decode())
    tree = ET.fromstring(data)
    print(tree)
    #print('printing what type of data tree is : ', data(tree))
    lst = tree.findall('comments/comment')
    print(tree.findall('.//count'))
    total = 0
    for item in lst:
        print(item.find('count').text)
        new = item.find('count').text
        total = total + int(new)
    print(total)





    break;



