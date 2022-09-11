# Find the radius of a circle if the radius is greater than zero
import math
pi=float(3.14)
radius=int(input("Enter the radius: "))
if radius < 0:
    print("The radius is smaller than zero")
    exit
area=math.pi * radius * radius
print(area)
