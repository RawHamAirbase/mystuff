import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL:')
xml_file = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml_file)

vals = tree.findall('comments/comment')
tot = 0
for val in vals:
    num = int((val.find('count').text))
    tot+=num
print(tot)
