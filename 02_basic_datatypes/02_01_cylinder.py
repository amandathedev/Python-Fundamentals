'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math

radius = 3.14
height = 5
volume = math.pi * (radius ** 2) * height
volume = round(volume, 2)

print("The volume of the cyliner is " + str(volume) + ".")