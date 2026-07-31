import math

n1 = int(input("Enter numerator of first fraction: "))
d1 = int(input("Enter denominator of first fraction: "))

n2 = int(input("Enter numerator of second fraction: "))
d2 = int(input("Enter denominator of second fraction: "))

num = n1 * d2 + n2 * d1
den = d1 * d2

gcd = math.gcd(num, den)

num = num // gcd
den = den // gcd

print("Sum =", num, "/", den)
