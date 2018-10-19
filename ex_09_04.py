count = dict()
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)
for line in fhand:
    if not line.startswith('From '):
        continue
    lsplit = line.split()
    count[lsplit[1]] = count.get(lsplit[1], 0) + 1
email = None
email_count = None
for k,v in count.items():
    if email_count is None or v > email_count:
        email_count = v
        email = k
print(email, email_count)
