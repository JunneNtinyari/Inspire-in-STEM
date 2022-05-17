#assignment
#area of a circle

r = input("enter radius of circle")
pi = 22/7
area = int (r)  * pi * int (r)

print("The radius of the circle is " + r)
print("The area of the circle is " + str (area))

#area of a cylinder
r = input("enter radius of the circle ")
h = input("enter height of the cylinder ")
d = input("enter diameter of the circle ")
pi = 22/7
areaofaCylinder = int (r) * 2 * int (r) * pi + pi * int(d) * int(h)
print("The radius of the circle is " + r)
print ("The height of the cylinder is " + h)
print("The diameter of the circle is" + d)
print("The area of the cylinder is " + str (areaofaCylinder))



#the volume of a cube
length = input("what is the length of the cube")
volume = int (length) * int (length) *int (length)
print("The length of the cube is " + (length))
print("The volume of the cube is " + str (volume))

#volume of a cylinder
radius = input ("What is the radius of the cylinder?")
height = input ("What is the height of the cylinder")
pi = 22/7 
volume = pi * int (radius) * int(radius) * int(height)
print("The radius of the cylinder is " + (radius))
print("The height of the cylinder is " + (height))
print("The volume of the cylinder is " + str (volume))

#the volume of a cuboid
length = 5
width = 3 
height = 2
volume = length * width * height 
print("the volume of the cuboid is " + str(volume))

