print("=============================================================")
print("======================Prime Number Checker===================")
print("=============================================================")
print()


prime = int(input("Enter a number: "))
print()
if prime > 1:
    for value in range(2, prime):
        if prime % value == 0:
            print(prime , "is not prime number.")
            break
        else:
            print(prime,'is a prime number.')
else:
    print(" Please enter a number greater than 1.")
