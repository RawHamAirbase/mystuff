score = input("Enter Score: ")
try:
    scf = float(score)
    if scf >= 0.9:
        print("A")
    elif scf >= 0.8:
        print("B")
    elif scf >= 0.7:
        print("C")
    elif scf >= 0.6:
        print("D")
    elif scf < 0.6:
        print("F")
except:
    print("Error: Out Of Range or Not a Number")
    quit()
