numbers={10, 20, 30, 40}

print(numbers)
numbers={10,10,10,29,30,30,40, 50}

print(numbers)

#add
numbers.add(60)
print(numbers)

numbers.remove(29)
print(numbers)

for num in numbers:
    print(num)

print(len(numbers))

set1={1,2,3}
set2={3,4,5}

#union
result = set1.union(set2)
print(result)

#intersection
result=set1.intersection(set2)
print (result)
#difference
result=set1.difference(set2)
print(result)
result=set2.difference(set1)
print(result)

#list to set
numbers=[1,2,2,2,3,3,3,4,4,5,5,1,1]
unique_numbers=set(numbers)
print(unique_numbers)