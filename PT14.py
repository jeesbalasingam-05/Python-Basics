num=input("Enter a number: ")
sum=0

for i in num:
    sum=sum+int(i)**len(num)

if sum==int(num):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
