n = int(input("Enter a number :"))
n2 = int(input("Enter another number :"))

smaller = min(n, n2)

hcf = 1

for i in range(1, smaller+1):
    if n % i == 0 and n2 % i == 0:
        hcf = i

print(f"The HCF of {n} and {n2} is {hcf}")
