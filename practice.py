# a=4
# b=5
# a=b
# b=a
# print(a)
#
# def fact(number):
#
#     if number==1:
#         return 1
#     else:
#         return number*fact(number-1)
#
# print(fact(5))
#
# nums = [4, 2, 3, 1]
# nums.sort()
# print(nums)
#
# student = {'name': 'John', 'age': 20}
# print(student['name'])

# a=30
# b=20
# c=10
#
# if a>b and a>c:
#     print("a is the largest number")
# elif  b>c and b>a:
#     print("b is the largest number")
# else:
#     print("c is the largest number  ")

# number=7
# isPrime=True
# for i in range(2,number):
#     if number%i==0:
#         isPrime=False
# print(isPrime)

#
# import array as arr
#
# numbers=arr.array('i',[1,2,3,4,5])
#
# numbers[4]=6
# targetValue=6
# for number in numbers:
#      for secoundNumber in numbers:
#          if number+secoundNumber==targetValue:
#              print(f"{{ {number} {secoundNumber} }}")
#
#
# print(6 % 3)
# print(6 // 3)
# for i in range(3):
#     print(i )

#
# try:
#     for i in range(3):
#         try:
#             if i % 2 == 0:
#                 raise ValueError("Even number")
#             else:
#                 print(i)
#         except ValueError as e:
#             print(e)
#             # raise
# except ValueError:
#     print("Outer exception caught")
# finally:
#     print("Finally block executed")


# def outer_function():
#     x = [1, 2, 3]
#
#     def inner_function():
#         nonlocal x
#         x.append(4)
#         return x
#
#     x = inner_function()
#     return x
#
#
# print(outer_function())

# x=10
# def change():
#     global x
#     x=20
#
# change()
# print(x)

# names=['a','b','c','d','e','f','g','h']
# with open("input.txt","w") as file:
#
#         file.write("")
#
# with open("input.txt","w") as file:
#     for name in names:
#         file.write(f"{name}\n")
#
# with open("input.txt","r") as file:
#     for line in file:
#         # print(len(line))
#         print(len(line.strip()))

# dict={
#     "name":"Chanura",
#     "Age":22
# }
# dict["country"]="srilanaa"
#
# for key,value in dict.items():
#     print(key,":",value)

# Input= [1, 2, 2, 3, 4, 4, 5]
# output=[]
#
# for i in Input:
#     output.append(i)
#     if i not in output:
#         output.append(i)
#
#
# print(output)
# output.clear()

# Input = [1, 2, 2, 3, 4, 4, 5]
# output = []
#
# for i in Input:
#     if i not in output:  # Check if the element is not already in the output
#         output.append(i)
#
# print(output)  # Output: [1, 2, 3, 4, 5]
# output.clear()
#
# a=["chanura","chanura","nimal"]
# out=list(set(a))
# print(out)


Input = "A man a plan a canal Panama"
listt = []
for i in Input:
    if i != " ":
        listt.append(i.lower())

print(listt)
reverse = []

for i in range(len(listt) - 1, -1, -1):
    reverse.append(listt[i])

print(reverse)
reverse.clear()
listt.clear()