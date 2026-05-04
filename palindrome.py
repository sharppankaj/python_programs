x = int(input("Enter a number:  "))
temp = x
rev = 0
while temp > 0:
    dig = temp % 10
    rev = rev * 10 + dig
    temp = temp // 10
    if x == rev:
        print(x, "is a palindrome")
    else:
        print(x, "is not a palindrome")
