fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    emails = line.split()
    print(emails[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
