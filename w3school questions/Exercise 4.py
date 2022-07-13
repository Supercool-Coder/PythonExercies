# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# In geometry, the area enclosed by a circle of radius r is πr2. Here the Greek letter π represents a constant,
# approximately equal to 3.14159, which is equal to the ratio of the circumference of any circle to its diameter.
from math import pi
u = float(input("Input the radius of the circle : "))
print("This is the radius of" +str(u)+" is:" +str(pi*u**2))
print(f"This is value of radius {u} is: {pi*u**2}")