#method have ()
#reassigning variables
name = "Junne Martin"
name = "  Doreen Kawira  "
age = 18
age = 43

username = "  junne  "
person = ("My name is " + (name) + " and I am " + str (age))
print(person)

#.format
print("My name is {} and i am  {}".format (name , age ))
print(f"My name is {name} and I am {age} years old")

#spaces and lines
print(f"My \t name is {name}  \n and i am {age} years old")
print(username)
print(username.strip())
print(name.rstrip())

#multiple line strings
msg = '''The kuccps placement is open.
 Have you registered yet.
 If you haven't you should before the deadline is reached.'''
print(msg)      

#SLICING
country ="Kenya"
print(country[:3])
print(country[3:])
print(country[-1:])
print(country[:-1])

#converting using .upper() to uppercase

name = "Junne Ntinyari "
print(name.upper())

#converting using .lower to lowercase

name = "JUNNE NTINYARI"
print(name.lower())


#concatenation- converting from one data type to another
#int>float - float(x)
#float>int - int(x)
#int>string - str(x)

number = 18
print(str(number))
j = 11
print(float(j))

f = 25.10
print(int(f))
d = 25.68
print(int(d))

fName = "Junne"
sName = "Ntinyari"
print(fName + sName)
fullName = fName + sName 
print(fullName)

#replace method
name = "Junne Ntinyari"
print(name.replace('J' , 'L'))

#split
dm = "Hey I'm already in town"
print(dm.split())

#length
print(len(dm))
