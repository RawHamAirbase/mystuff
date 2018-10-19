tot = 0.0
count = 0.0

while True:
    try:
        num = input('Enter a number:')
        if num == 'done':
            break
        else:
            numf = float(num)
    except:
        print('Error: not a valid input')
        continue
    tot += numf
    count += 1
if count == 0:
    print('No data to show')
else:
    print(tot,count,tot/count)
