#1
#print "python" 10 times
# a="python"
# i=0
# while i<10:
#     print(a)
#     i=i+1


#2
#sum of list
# a=[1,2,3,4,5]
# b=len(a)
# sum=0
# i=0
# while i<b:
#     sum=sum+a[i]
#     i=i+1
# print(sum)


#3
#indexing
# a="python"
# b=len(a)
# i=0
# while i<b:
#     print(i,"=",a[i])
#     i=i+1


#4
# list=[1,'a','b',2,3,4]
# b=len(list)
# integer=[]
# string=[]
# i=0
# while i<b:
#     if type(list[i])==int:
#         integer.append(list[i])
#     else:
#         string.append(list[i])
#     i=i+1
# print(integer)
# print(string)
    

#5
#multiplication
# a=2
# i=1
# while i<11:
#     print(a,"X",i,"=",a*i)
#     i=i+1


#6
#factorial
# a=int(input("entery any number"))
# factorial=1
# i=1
# while i<=a:
#     factorial=factorial*i
#     i=i+1
#print(factorial)

#7
#reverse
# a="python"
# b=len(a)
# reverse=""
# i=0
# while i<b:
#     reverse=a[i]+reverse
#     i=i+1
# print(reverse)

# or

#reverese of list
# a=[1,2,3,4]
# b=len(a)
# reverse=[]
# i=0
# while i<b:
#     reverse=[a[i]]+reverse
#     i=i+1
# print(reverse)


#8
# a=[1,2,3,4]
# sum=[]
# i=0
# while i<(len(a)):
#     sum=sum+[a[i]+1]
#     i=i+1
# print(sum)


#9
#prime number or not
# a=int(input("enter any number:"))
# i=2
# if a>1:
#     while i<a:
#         if a%i==0:
#             print(a,"is not prime")
#             break
#         i=i+1
#     else:
#         print("prime")


#10
# end=int(input("enter any number"))
# prime_number=[]
# i=2
# while i<end:
#     if end>1:
#         for j in range(2,i):
#             if i%j==0:
#                 print(i,"is not prime")
#         else:
#             prime_number.append(i)
#         i=i+1
# print(prime_number)

   
#11. Python program that accepts a string and calculate the number of digits and letters
# myInput = input("Please enter anything: ")
# i = 0
# digit = 0
# letter = 0
# while i < len(myInput):
#   if myInput[i].isdigit():
#     digit += 1
#   if myInput[i].isalpha():
#     letter += 1
#   i +=1
# print('digit', digit, 'letter', letter)


# 12. Python program to check the validity of username and password input by users
# userName = 'Robin'
# password = "Password"
# i = 0
# while True:
#   inputName = input("Pease enter your Name: ")
#   inputPassword = input("Pease enter your Password: ")
#   if i > 3:
#     print("Your pin is locked. Please contract earset branch")
#   if inputName == userName and inputPassword == password:
#     print("You are logged in. Welcome to our bank !!!")
#   else:
#     print("Your User Name or Password is wrong")
#     i += 1


# 13. program to print the given number is odd or even
# myInput = int(input("please enter a number: "))
# i = 0
# while i < 1:
#   if myInput % 2 == 0:
#     print("its an even number")
#   else:
#     print("its odd mumber")
#   i += 1


# 14. factorial of a given number
# num=int(input("Enter a number to find factorial: "))
# factorial=1
# if num<0:
#    print("Factorial does not defined for negative integer")
# else:
#   while(num>0):
#         factorial=factorial*num
#         num -= 1
        
#   print("factorial of the given number is: ")
#   print(factorial)


# 15. program to check given number is palindrome or not
# num = input("Enter The Number : ")
# rev = ""
# a = len(num)
# i = 0
# while i < len(num):
#     rev = rev + num[a-1]
#     a = a - 1
#     i += 1
# if rev == num:
#     print("It Is A Palindrome")
# else:
#     print("It Is Not A Palindrome")



# 16. program to check given number is armstrong or not
# take input from the user
# num = int(input("Enter a number: "))
# # initialize sum
# sum = 0
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


# 17. Python program to check a number is perfect square
# myInput = int(input("Please enter anything: "))
# i = 0
# count = 0
# while i < myInput:
#     if i * i == myInput:
#       count += 1
#     i += 1
# if count == 1 :
#   print('Its perfect')
# else:
#   print('Its  not perfect')



# 18. python program to check a number is perfect number
# num = int(input('Enter any positive integer: '))
# sum1 = 0
# i = 1
# if num <= 0:
#     print('Invalid Number.')
# else:
#     while(i < num):
#         if num % i == 0:
#             sum1 += + i
#             i += 1
#         else:
#             i += 1
#     if sum1 == num:
#         print(num, "is a perfect number")
#     else:
#         print(num, "is not a perfect


#19. Print multiplication table of  1,2,3,4,5,6,7,8
# i = 0
# j = 0
# while i < 10:
#   while j < 10:
#     print(i, '*', j, '=', i*j)
#     i += 1
#     j += 1


# 21. Python program to calculate the sum of all the odd numbers within the given range.
# num = [2, 3, 5, 6, 8 ]
# sum = 0
# i = 0
# while i < len(num):
#     if num[i] % 2 != 0:
#         sum += num[i]
#     i += 1
# print("The Sum Of Odd Number is :", sum)