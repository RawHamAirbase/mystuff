
def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    elif hours > 40:
        return (40 * rate) + ((hours - 40) * (rate * 1.5))

hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate Per Hour:"))
p = computepay(hours, rate)
print(p)
