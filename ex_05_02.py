largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numf = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = numf
    elif largest < numf:
        largest = numf
    if smallest is None:
        smallest = numf
    elif smallest > numf:
        smallest = numf

print("Maximum is", largest)
print('Minimum is', smallest)
