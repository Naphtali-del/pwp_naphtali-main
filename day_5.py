number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True

    for value in range(2, number):
        if number % value == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")