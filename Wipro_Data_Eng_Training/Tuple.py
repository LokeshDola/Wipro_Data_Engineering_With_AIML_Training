numbers=(10, 20, 30, 40)

print(numbers)

print(numbers[0])
print(numbers[1])

print(numbers[-1])
print(numbers[1:4])

#we can't modify tuples -- they are immutable

for num in reversed(numbers):
    print(num)


#mixed data types
data = ("Rahul", 25, 3430303, True)
print(data)

#Tuple Packing
person=("Rahul",22, "Engineer")
print(person)

#Tuple unpacking
a,b,c= person
print(a)
print(b)
print(c)