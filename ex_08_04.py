fname = input("Enter file name: ")
fhand = open(fname)
flist = list()
for line in fhand:
    lsplit = line.split()
    for word in lsplit:
        if word not in flist:
            flist.append(word)
flist.sort()
print(flist)
