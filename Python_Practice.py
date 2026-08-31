#Printing
from typing import Dict

print("Raksha")
print("Raksha", 1)
print("Raksha", 2,"Ansh")

# addign delimeter
print("Raksha", 3,"Ansh",sep='%')

TOTAL = 10+20\
    +30
print(TOTAL)

#String split
x = "Ansh is motu"
words = x.split()   # default separator is whitespace
print(words)

# if and else
#odd and even
num = range(1,21)
even = []
odd = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# Dict comprehension - Inverting a dict
# Comprehension is just a loop but in compressed.

original = {"a":1, "b":2, "c":3}
inverted = {value:key for key, value in original.items()}
print(inverted)

reversed_dict = dict(reversed(list(original.items())))
print(reversed_dict)


# List comprehension with filter
number = [1,2,3,4,5,6,7,8,9,10]
evens = [i for i in number if i % 2 == 0]
odds = [i for i in number if i % 2 != 0]
print(evens)
print(odds)

# Normal loop
even = []
for i in number:
    if i % 2 == 0:
        even.append(i)
print(even)

# Loops
#num = int(input("Enter a number: "))
num = 5
print(num)

for i in range(1,11):
    if i%2 ==0:
        print(i)

for i in range(20,0,-1):
    print(i)

total = 0
for i in range(1,51):
    total = total + i
print(total)

#num = int(input("Enter a number"))
num = 5
print(num)

for i in range(1,num+1):
    if i % 3 ==0:
        print(i)

print("Give the count")
count = 0
for i in range(1,31):
    if i%2 ==0:
        count = count + 1
print(count)

print("Print the number of multiplication below 50")
num = 5
for i in range(1,50):
    result = num*i
    if result > 50:
        break
    print(result)

print("Print the sequence 2 4  8 16 32 .. till 10 ")

for i in range(1,11):
    print(2**i)
    0
# Patterns
for i in range(1,num+1):
    for j in range(0,i):
        print(i, end=" ")
    print()

# Practice on the above

price = {"apple": 1,"Banana":2,"Orange":3 }
inverted_price = { value:key for key, value in price.items()}
print(inverted_price)

works = ["hi", "Hello", "yo","World"]
len_com = [i for i in works if len(i)>2]
print(len_com)

num = range(1,21)
odds =[]
for i in num:
    if i % 2 == 1:
        odds.append(i*i)
print(odds)

#Functions

def greet():
    print("Hello World")

greet()
greet()

#Inputs parameters and arguments

def greet(name):
    print("Hello", name,"!")
    print(f"Hello {name}!")

greet("Raksha")
greet("Ansh")

def add(a,b):
    print(a+b)

add(50,5)

def describe(animal,sound):
    print(f"A {animal} says {sound}")

describe("Dog","Woof")

#Returning values
#Returning hands a value back to whoever called the function, so you can store it or reuse it

def add(a,b):
    return a+b

result = add(5,5)   # result holds the value of that is returned as 10 here
print(result*10)# 100 (we resued the returned value )

def add_print(a,b):
    print(a+b)

x = add_print(5,5)
print(x)  #return null as we are not returing anything

def is_even(n):
    if n % 2 == 0:
        return True
    return False

x= is_even(5)
print(x)

#Positional arguments

def power(base, exponent):
    return base ** exponent

power(2,3) # All positional
power(base=2,exponent=3) # all keywords
power(2,exponent = 3) #positional then keywords
# power(base = 2,3) # Error = positional argument follows keyword argument

#Default arguments
#Give a parameter a fallback value so caller can skip it.

def greet(name , greeting = "Hello"):
    return f"{greeting} {name}!"

greet("Raksha") #Hello Raksha (used defualt one )
greet("Ansh","Hi") # Hi Ansh (overode it )

def bad(item,bucket=[]):
    bucket.append(item)
    return bucket

bad(1)
bad(2)

def good(item,bucket = None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

y =good(1)
y = good(2)
print(y)

#*args — Any number of positional arugment

#Sometimes you dont know how many values will come in.
# *args scoops all the extra positional arguments into a tuple

def total(*args):
    return sum(args)

x=total(1,2,3,4,5,6,7,8,9,10)
print(x)
x=total()
print(x)
x=total(1,2,3)
print(x)

#The name args is just convention --the * is what does the work
#( collect the rest into a tuple)

def total(*alll):
    return sum(alll)

def describe(**kwargs):
    return kwargs

x=describe(name="Raksha",age=23)
print(x)
# It lets a function accepts many optional setting without listing each one.

# Order is strict
#regular --> default --> *args --> **kwargs

def process(label,factor,*args,**kwargs):
    return {
        "label":label,
        "factor":factor,
        "extra_numbers":args,  #tuple
        "options":kwargs,   #dict
    }

x=process("run",2,3,4,5,6,mode="fast",debug="on")
print(x)

#keyword only arguments anything after a base * must be passed by name.

#Type hints (params + return )

def add(a,b) -> int:
    return a+b
x=add(1,2)
print(x)

def summaries(title:str,*value:float,unit:str ="USD",**meta:dict)->dict:
    return {
        "title":title,
        "sum":sum(value),
        "unit":unit,
        "meta":meta,
    }

X=summaries("Honey", 4,5,6,mode="fast",debug="on")
print(X)

#Docstring
def add(a,b):
    """String fucntion testing - Function used for addition """
    return a+b

x= help(add)
print(x)
x=add.__doc__
print(x)

#Function are values (first class object )
#In python a function is itself a value you can store, pass around and return.

def shout(text):
    return text.upper()

f = shout #It refers to f = shout("hi")
print(f("hi"))  # HI

#Passing a function into function
def apply(func,value):
    return func(value)

x=apply(shout,"Hello")
print(x)

#Lambda

square = lambda x:x*x
x=square(5)
print(x)

even =lambda x:x%2==0
x=even(5)
print(x)

y=sorted(["aabbbbb","bbb","c"], key = lambda x: len(x))
print(y)

#Map
my_list = [1,2,3,4,5,6,7]

def square(x):
    return x*x
result = list(map(square,my_list))
print(result)

result = list(map(lambda x:x*x,my_list))
print(result)

result = list(filter(lambda x:x%2==0,my_list))
print(result)

#OOP

class Dog:
    def __init__(self , name , age ):
        self.name = name
        self.age = age

rex = Dog("rex",1)  #object
bella = Dog("bella",4)

print(rex.name) #calling a function with object
print(rex.age)

# __init__
baby = Dog("Baby",3)
print(f"My dog name is {baby.name} and my dog age is {baby.age}")

# changing a attributes
rex.age = 5
print(rex.age)

# Methods

class Dog:
    def __init__(self , name , age ):
        self.name = name
        self.age = age

    def bark(self):        #a method that reads data
        return f"My dog name is {self.name}"

    def hav_birthday(self):   #method that changes age/ data
        self.age = self.age +1

Rex = Dog("Rex",5)
x = Rex.bark()
print(x)

Rex.hav_birthday()
print(Rex.age)