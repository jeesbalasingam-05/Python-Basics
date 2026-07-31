num = int(input("Enter a number: "))

for i in range(2, num):
    prime1 = True
    for j in range(2, i):
        if i % j == 0:
            prime1 = False
            break

    prime2 = True
    for j in range(2, num - i):
        if (num - i) % j == 0:
            prime2 = False
            break

    if prime1 and prime2:
        print(num, "=", i, "+", num - i)
        break
else:
    print("Cannot be expressed as the sum of two prime numbers.")
