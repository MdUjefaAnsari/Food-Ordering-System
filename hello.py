# print character ascii value
# a=(input("enter any character: "))
# acii=(ord(a))
# print("The ascii value of ",a,"is = ",acii)
# ---------------------------------
# print alphabet ascii value 
# a=int(input("enter any alphabet: "))
# acii=str(chr(a))
# print("The ascii value of ",a,"is = ",acii)
# --------------------------
# convert capital letter to small letter 
# a=str(input(("enter capital letter A to Z :")))
# print(a.lower())
# ------------------

# take input and print their sum 
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=a+b
# print("The sum of",a,"and",b," is ",c)
# ================
# print small letter to capital letter 
# a=str(input("enter any character a to z: "))
# print(a.upper())
# ================
# print greatest number \\
# a=int(input("enter first number A: "))
# b=int(input("enter second number B: "))
# c=int(input("enter third number C: "))
# if a>b and a>c:
#     print("a is the greatest value",a)
# elif b>a and b>c:
#     print("b is the greatest value",b)
# elif c>a and c>b:
#     print("c is the greatest value",c)
# else:
#     print("Your entered values are same!!")
# ==================
# print reverse 
# num = int(input("Enter your number: "))

# rev_num = 0

# while (num > 0):
#     remainder = num % 10
#     rev_num = (rev_num * 10) + remainder
#     num = num // 10

# # Display the result
# print("The reverse number is : {}".format(rev_num))
# ============ 
# check wether it is capital or not 
# a=str(input("enter alphabet character: "))

# if a.isupper():
#     print("IT is UPpER Letter")
# elif a.islower():
#     print("it is LoWer letter")
# else:
#     print("It is not a letter!!")
# ==============
# check whether it is odd or even 
# number = int(input("enter any number: "))
# if (number%2) ==0:
#     print("your entered number is even")
# else:
#     print("Your entered number is odd")
# ============= 
# check whether it is rectangle or square 
# a=int(input())
# b=int(input())
# if a==b:
#     print("square!")
# else:
#     print("rectangle!")

# ====================
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
# num = 7

# To take input from the user
# num = int(input("Enter a number: "))

# factorial = 1

# check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)
# =====================================================
# Ask for enter the number from the use  
# number = int(input("Enter the integer number: "))  
  
# # Initiate value to null  
# revs_number = 0  
  
# # reverse the integer number using the while loop  
  
# while (number > 0):  
#     # Logic  
#     remainder = number % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
  
# # Display the result  
# print("The reverse number is : {}".format(revs_number))  
# =======================================
# txt=str(input("enter a number:"))
# # txt = "Hello World"
# print(txt[::-1])
# ============================= 
# \\\\\\\\\\\\\\\\\\\\\\\\print any message in sequence pattern////////////////// 
# str=input("enter any message: ")
# l=len(str)
# i=0
# for i in range(0,1):
#     for i in range(0,i+1):
#         print(str[i],end="")
#     print()
# ================================
# fabonacci series in python 
# a=int(input("Enter the terms"))
# f=0                                         #first element of series
# s=1                                         #second element of series
# if a<=0:
#     print("The requested series is",f)
# else:
#     print(f,s,end=" ")
#     for x in range(2,a):
#         next=f+s                           
#         print(next,end=" ")
#         f=s
#         s=next
# ====================================================== 
# print table 2 to 20 in python 
# num = int(input("enter any number :"))

# # To take input from the user
# # num = int(input("Display multiplication table of? "))

# # Iterate 10 times from i = 1 to 10
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)
# ========================================================
# This is the example of print simple pyramid pattern  
# n = int(input("Enter the number of rows"))  
# # outer loop to handle number of rows  
# for i in range(0, n):  
#     # inner loop to handle number of columns  
#     # values is changing according to outer loop  
#         for j in range(0, i + 1):  
#             # printing stars  
#             print("* ", end="")       
  
#         # ending line after each row  
#         print()
# ==================================================================
# print("The character pattern ")  
# asciiValue = 65     #ASCII value of A  
# for i in range(0, 5):  
#     for j in range(0, i + 1):  
#         # It will convert the ASCII value to the character  
#         alphabate = chr(asciiValue)  
#         print(alphabate, end=' ')  
#         asciiValue -= 1  
#         print(alphabate,end=' ')
#         asciiValue +=1
#     print()  
# ======================================
rows = int(input("Enter the number of rows: "))  

# This will print the rows  
for i in range(1, rows+1):  
    # This will print number of column  
    for j in range(1, i + 1):
        print(j, end=' ')  
    print("")  

