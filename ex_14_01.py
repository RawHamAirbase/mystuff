import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')
data = urllib.request.urlopen(url).read()

print('Receiving:' + url )

info = json.loads(data)
print('Received', len(data), 'characters')
counts = info["comments"]
print('Count:', len(counts))

tot = 0
for item in counts:
    tot += int(item["count"])
print(tot)
