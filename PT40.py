x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("The point lies in First Quadrant")
elif x < 0 and y > 0:
    print("The point lies in Second Quadrant")
elif x < 0 and y < 0:
    print("The point lies in Third Quadrant")
elif x > 0 and y < 0:
    print("The point lies in Fourth Quadrant")
elif x == 0 and y == 0:
    print("The point lies at the Origin")
elif x == 0:
    print("The point lies on the Y-axis")
else:
    print("The point lies on the X-axis")
