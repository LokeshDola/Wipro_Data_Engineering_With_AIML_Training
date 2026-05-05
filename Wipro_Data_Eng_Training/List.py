numbers= [10, 20, 30, 40, 50]

#print(numbers)

#print(numbers[0])
#print(numbers[2])
#print(numbers[4])

#negative indexing
#print(numbers[-1])
#print(numbers[-2])

#modifying elements
#numbers[1]=99
#print(numbers)

#adding elements tp list
numbers.append(60)
print(numbers)


numbers.insert(1, 70)
print(numbers)

numbers.remove(70)
print(numbers)

numbers.pop()#removes the last number
print(numbers)

print(len(numbers))

for num in numbers:
    print(num)

#Slice
print(numbers[0:3])#[0:n-1]