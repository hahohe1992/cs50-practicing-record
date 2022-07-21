print("hello, world!")
#Type
a = 28      #int
b = 1.5     #float
c = "Hello" #str
d = True    #bool
e = None    #NoneType

#input
name = input("Name: ")
print("Hello, " + name)

#condition
number = input("Number: ")
if int(number) > 0:
  print("number is positive")
elif int(number) < 0:
  print("number is negative")
else:
  print("number is 0")

#sequences
name = "Harry"
print(name[0])
print(name[1])

names = ["Harry", "Ron", "Hermione"]
print(names)
print(names[0])
print(names[1])

coordinateX = 10.0
coordinateY = 20.0
coordinate = (10.0, 20.0)

#Data Structures
#list: sequence of mutable values
#tuple: sequence of immutable values
#set: collection of unique values
#dict: collection of key-value pairs
#---
#Define a list of names
nameList = ["Harry", "Ron", "Hermione", "Ginny"]
print(nameList)
nameList.append("Draco")
print(nameList)
nameList.sort()   #sort the list by alphabet
print(nameList)

#Define a empty set

s = set()
#Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(s)
#Remove element inside the set
s.remove(2)
print(s)

print(f"The set has {len(s)} elements")

#loops
for i in [0,1,2,3,4,5]:
  print(i)

for i in range(6):
  print(i)

for character in nameList:
  print(character)

for alphabet in name:
  print(alphabet)

#Dictionaries
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses["Harry"])


#function
def square(x):
  return x * x

for i in range(10):
  print(f"The square of {i} is {square(i)}")

#import other py files
from functions import multiple

for i in range(10):
  print(f"The multiple of {i} and {i+1} is {multiple(i, i+1)}")

#或改成import整個module：
#import functions
#呼叫時指定該module裡的function名稱
#functions.multiple


