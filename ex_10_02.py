fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
hour_count = dict()
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    fsplit = line.split()
    time = fsplit[5]
    time_split = time.split(':')
    hour_count[time_split[0]] = hour_count.get(time_split[0], 0 ) + 1
drev = list()
for k,v in hour_count.items():
    drev.append((k,v))
drev.sort()
for a,b in drev:
    print(a, b)
