#1. Swap two numbers
a = 5
b = 10
print("before swapping a:",a)
print("before swapping b:", b)

#using temp variable
temp = a
a = b
b = temp

#without using temp variable
#a , b = b , a

print("after swapping a :",a)
print("after swapping b:", b)

#2. Length of the string
str = "Python"
print("Length of String:", len(str))

#3. print first element and alst  element of list
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])

#4. Count the number of vowels in list
str="education"
vowels = "aeiou"
count = 0
for ch in str:
    if ch in vowels:
        count += 1
print("No of Vowels:", count)



#5. Sum of Elements in List
numbers=[5, 10, 15, 20]
sum = 0

for i in numbers:
    sum += i
print("Sum of Numbers:", sum)

#6. Find Maximum number in the list
numbers=[3, 7, 2, 9, 5]
max_num=0
for i in numbers:
    if i>max_num:
        max_num=i;
print("Maximum Number:", max_num)

#7. print all the even numbers in list
numbers=[1,2,3,4,5,6,7,8]
for i in numbers:
    if i % 2 == 0:
        print("Even numbers:",i)

#8. Count Words in a sentence
sentence="Python is easy to learn"
word_count = 0
for word in sentence.split():
    word_count+=1
print("Total words in a sentence:", word_count)


#9. Covert Celsius to Fahrenheit
#formula
#F=(C x 9/5)+32
#input : 25

c = 25

f = (c * 9/5) + 32

print(f"{f:.0f}°F")



#10. Check Palindrome String
#input = "madam"
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")




