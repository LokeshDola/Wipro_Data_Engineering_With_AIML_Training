numbers = [1,2,3,4,5]
#List Comprehension
squares = [x*x for x in numbers]
print(squares)
#

#List Comprehension with Condition
even = [x for x in numbers if x % 2==0]
print(even)

#List of Strings
names = ["rahul", "sneha"]
upper_names = [name.upper() for name in names]
print(upper_names)

