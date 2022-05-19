#lists

motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)
#accessing list items using index
print(motorcycles[0])
print("I love " + motorcycles[0])
#changing elements inside a list
print(motorcycles[0])

#adding elements in a list
motorcycles.append('bugatti')
print(motorcycles)
motorcycles.append('bugatti , tiger')

plateNumber = ['H123 ', 'S148' , 'Y231']
print(motorcycles[0]+ " " + plateNumber[0])
print(motorcycles[0]+ " " +plateNumber[0] + motorcycles[1]+" " +plateNumber[1])
#print("The" + motorcycles[0] "motorcycle you are chasing down has the following" + (plateNumber[0]"plate number")

#deleting an item from a list
del motorcycles[2]
print(motorcycles) 

#deleting using the pop method
poppedMotorcycle = motorcycles.pop()
mOwner = "Junne"
print(motorcycles)


print(f"My name is {mOwner}  and I own a {motorcycles[0]} motorcycle plate number {plateNumber[2]}")
#removing an item from a list
motorcycles.remove('honda')
print(motorcycles)
