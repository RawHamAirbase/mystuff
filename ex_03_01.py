hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate Per Hour:"))
if hrs <= 40:
    print(hrs * rate)
elif hrs > 40:
    print((40 * rate) + ((hrs - 40) * (rate * 1.5)))
