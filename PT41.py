import math

n = int(input("Enter the number of people (n): "))
r = int(input("Enter the number of seats (r): "))

permutation = math.factorial(n) // math.factorial(n - r)

print("Number of permutations =", permutation)
