num1=int(input("Enter a num1:"))
num2=int(input("Enter a num2:"))
num3=int(input("Enter a num3:"))

if((num1>num2)&(num1>num3)):
    print("num1 is greater")

elif((num2>num1)&(num2>num3)):
    print("num2 is greater")

else:
    print("num3 is greater")
