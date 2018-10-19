fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count +=  1
    beg = line.find(str(0))
    xval = float(line[beg:])
    tot += xval

print("Average spam confidence:",tot/count)
