n = int(input("Enter the value of N: "))
x = int(input("Enter the number of divisors: "))

count = 0

for num in range(1, n + 1):
    divisors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1

    if divisors == x:
        count += 1

print("Number of integers with exactly", x, "divisors =", count)
