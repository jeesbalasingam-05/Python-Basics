A=int(input("Enter a number:"))
B=int(input("Enter a number:"))

for num in range(A,B+1):
    sum=0
    temp=str(num)

    for i in temp:
        sum=sum+int(i)**len(temp)

    if sum==num:
        print(num)
