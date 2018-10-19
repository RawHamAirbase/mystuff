import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

links = list()
url = input('Enter url:')
count = int(input('How many to retrieve:'))
pos = int(input('Enter position:'))

while count > 0 :
    count = count - 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        newurl = tag.get('href', None)
        links.append(newurl)
    url = links[pos - 1]
    links.clear()
print(url)
