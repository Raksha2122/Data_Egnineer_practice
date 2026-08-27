#Printing
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

