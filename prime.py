a = int(input("enter a number:"))

if a == 0 or a == 1:
    print(a, " is not a prime")

elif a > 1:
    for i in range(2, a):
        if (a % i == 0):
            print(a, "is not a prime number")
            break

    else:
        print(a, "is a prime number")
