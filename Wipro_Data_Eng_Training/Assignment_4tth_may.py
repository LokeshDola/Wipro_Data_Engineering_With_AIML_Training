#Section 1
#Second Largest Number
nums= [10, 20, 4, 45, 99]
nums = list(set(nums))
nums.sort()

print(nums[-2])

#Rotate List by K
nums=[1,2,3,4,5]
k=2

k=k%len(nums)
result = nums[-k:] + nums[:-k]

print(result)

#Find the missing number(1 to N
nums=[1,2,4,5]
n = len(nums) + 1
total = n * (n + 1 ) // 2
print(total - sum(nums))

# Move all zeros to end
nums=[0,1,0,3,12]
result = []
for i in nums:
    if i != 0:
        result.append(i)
for i in nums:
    if i == 0:
        result.append(i)

print(result)

#Find pairs with given sum
nums=[2,4,3,5,7,8]
target = 7

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])


# Section 2
#Sort the list of Tuples by Second Value
data = [(1,3), (2,1),(4,2)]
result = sorted(data, key = lambda x: x[1])
print(result)

#Convert Tuple list into Dictionary
data = [(1, "Rahul"), (2, "Sneha")]
result=dict(data)
print(result)

#Section 3
#Find the unique elements from Two list
list1 = [1,2,3,4]
List2 = [3,4,5,6]
union_set = set(list1).union(set(List2))
print(union_set)

#Check if two lists have common elements
#list1=[1,2,3]
#list2=[3,5,6]
list1=[1,2,3]
list2 =[4,5,6]
common = set(list1).intersection(set(list2))
if common:
    print("Yes")
else:
    print("NO")


#Section 4
#Frequency Count
data = [1,2,2,3,3,3]
freq = {}
for i in data:
    freq[i] = freq.get(i,0) + 1

print(freq)

#Find Key with maximum Value
d = {"a":10, "b":25, "c" :15}
max_key=max(d, key = d.get)
print(max_key)

#Merge Two Dictionaries
d1 = {"a":1, "b":2}
d2={"b":3, "c":4}

merged = {**d1, **d2}

print(merged)

#Group Elements by Frequency
list = [1,1,2,2,2,3]
result = {}
for i in list:
    result.setdefault(i, []).append(i)
print(result)


#Find First Non-Repeating Element
list = [4,5,1,2,0,4]
freq={}
for i in list:
    freq[i] = freq.get(i,0) + 1

for i in list:
    if freq[i] == 1:
        print(i)
        break


#Flatten nested list
list = [[1,2], [3,4], [5]]  
flat = []
for sub in list:
    for i in sub:
        flat.append(i)
print(flat)