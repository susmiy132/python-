# #1. print "softwarica" 10 times
# for i in range(0,10):
#     print("softwarica")

# #2. Sum of list
# list=[1,2,3,4,5]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)

#3. print ech character using indexing
# a="python"
# b=len(a)
# for i in range(b):
#     print(i,"=",a[i])


#4. write a program to display integer from of a list.
# given list=[1,"a","c",2,3,4]
# list=[1,"a","c",2,3,4]
# integer=[]
# string=[]
# for i in list:
#     if type(i)==int:
#         integer.append(i)
#     else:
#         string.append(i)
# print(integer)

#5. Multiplication of a each element.
#given list=[4,5,3,2]
# a=[4,5,3,2]
# multiple=1
# for i in a:
#     multiple=multiple*i
# print(multiple)

#6. Multiplication table of a given number
# a=2
# mul=1
# for i in range(1,11):
#     print(a,"x",i,"=",a*i)

# #7. reverse a list
# a=[1,2,4,5,6]
# reverse=[]
# for i in a:
#     reverse=[i]+reverse
# print(reverse)


# #8. given list is [1,2,3,4] but expected output in new list[2,3,4,5]
# list=[1,2,3,4]
# sum=[]
# for i in list:
#     sum=sum+[i+1]
# print(sum)


#9. given number is prime or not.
# a=int(input("enter any number"))
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print("it is not a prime number")
#             break
#         else:
#             print("it is a prime number")
#             break
# else:
#     print("prime")


# #10. Write a python program to display all the prime numbers within a given range.
# start=int(input("enter a number: "))
# end=int(input("enter a number: "))
# prime_number=[]
# for num in range(start,end):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             # print(num,"is a prime number'")
#             prime_number.append(num)
# print(prime_number)


#11. python program that accepts a string and calcutale the number of digits and letters and space
# a="susmi3344"
# letter=0
# digit=0
# for i in a:
#     if i.isalpha():
#         letter=letter+1
#     elif i.isdigit():
#         digit=digit+1
# print(letter)
# print(digit)


#12 python program to check the validity of username and password input by user
# username="sumi"
# password="4488"
# for i in range(5):
#     user_name=str(input("enter a valid name:"))
#     pass_word=str(input("enter a valid password:"))
#     if username==user_name and password==pass_word:
#         print("login")
#         break
#     else:
#         print("invalid")
#         break
# else:
#     print("5 attempts finished")


#13. program to print the given number is odd or even
# a=int(input("enter any number"))
# for i in range(a):
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")


#14. factorial of a given number
# a=6
# factorial=1
# for i in range(1,a+1):
#     factorial=factorial*i
# print(factorial)


#15. program to check given number is palindrome or not.
# name=str(input("enter a valid name"))
# reverse=""
# for i in name:
#     reverse=i+reverse
# print(reverse)
# if name==reverse:
#     print("It is palindrone")
# else:
#     print("It is not a palindrone")


#16. program to check number is armstrong or not.
# a=input("enter a number: ")
# b=len(a)
# sum=0
# for i in a:
#  sum=sum+int(i)**b
# if sum==int(a):
#    print("armstrong")
# else:
#    print("not armstrong")



#17. python program to check a number is perfect square.
# import math
# num=int(input("enter any number"))
# root=math.sqrt(num)
# if int(root+0.5)**2==num:
#     print(num,"is a perfect square number")
# else:
#     print(num,"is not a perfect number")


# #18. python program to check a number is perfect number.
# num=int(input("enter any number"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
#     else:
#         pass
# if sum==num:
#     print("The number is perfect number")
# else:
#     print("The number is not  perfect number")


# #19 print multiplication table of 1,2,3,4,5,6,7,8
# for i in range(1,9):
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)


# #20. given list is lst=[1,2,3,4] but print 1 and 2 only
# lst=[1,2,3,4]
# for i in lst:
#     if i==3:
#          break
#     print(i)



# #21. python program to calculate the sum of all the odd numbers within the given range.
# a=15
# odd=0
# for i in range(a):
#     if i%2==0:
#         pass
#     else:
#         odd=odd+i
# print(odd)


# #22. python program to calculate the sum of all odd numbers withi the gven range.
# a=20
# even=0
# for i in range(a):
#     if i%2==0:
#         even=even+i
#     else:
#         pass
# print(even)


#23. write apython program to count the space of a given string
# str="su   ta"
# space=0
# for i in str:
#     if i.isspace():
#         space=space+1
#     else:
#         pass
# print(space)


# #24. given list is [1,2,3,4] but expected output is [1,8,27,64]
# a=[1,2,3,4]
# b=[]
# for i in a:
#     b.append(i**3)
# print(b)


#25. multiplication of a list
# a=[1,2,3,4,5]
# mul=1
# for i in a:
#     mul=mul*i
# print(mul)


#26. place a break statement in the floor so that it prints from 0 to 7 only(including7).given range(50).
# for i in range(50):
#     if i==7:
#         break
#     else:
#         print(i,end=" ")


#27. write a for loop that iterates through  string and prints every letters
# name="kanchanpur"
# a=len(name)
# for i in name:
#     print(i,end=' ')
# print("\n")
# for i in range(0,a):
#     print(name[i])


#28.Write a for loop which print "Hello!, 
# " plus each name in the list. i.e.: "Hello!, 
# Ram". Hint a=["ram","shyam",1,2] 
# expected output:  Hello!ram Hello!shyam

# a=["ram","shyam",1,2]
# b=[]
# for i in a:
#      b.append("Hello!"+str(i))
# print(b)


#29. Using a for loop and .append() method append each item with 
# a Dr. prefix to the lst. 
# Hint a=["ram","shyam"] 
# expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
# a=["ram","shyam"]
# b=[]
# for i in a:
#     b.append("Dr."+str(i))
# print(b)


# #30.Write a for loop which appends the square of each number to the new list.
# num=[8,6,12,9]
# square=[]
# for i in num:
#     if i**2:
#         square.append(i*i)
#         print(i,"is the square number is:",square)


#31.Write a for loop using an if statement, 
#that appends each number to the new list if it's positive. 
#given lst1=[111, 32, -9, -45, -17, 9, 85, -10]

# lst1=[111,32,-9,-45,-17,9,85,-10]
# positive=[]
# for i in lst1:
#     if i>0:
#         positive.append(i)
#     else:
#         pass
# print(positive)


#32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#given list=[0,1,2,3,4,5,6]
# list=[0,1,2,3,4,5,6]
# for i in list:
#     if i==3 or i==6:
#         continue
#     print(i)
    

#33.Write a for loop which appends the type of each element in the first list to the second list.
# list1=[1,"ram",6/4,12,"sanu",8]
# list2=[]
# for i in list1:
#     x=type(i)
#     list2.append(x)
# print(list2)


#34.Use else block to display a message “Done” after successful execution of for loop.
# for i in range(1,4):
#     print(i)
# else:
#     print("Done")


#35. Write a while loop statement to print the following series: 105 98 -------7
# a=105
# while(True):
#     print(a,end=" ")
#     a-=7
#     if a==0:
#         break    


#36.  removal bad characters from the given string. 
#Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n". 
#Expected output = pythonpython

# bad_chars=[';',':','!','*']
# string="py;th*o:n!;py*t*h:o!n"
# new=""
# for i in string:
#     for j in bad_chars:
#         if i==";" or i==":" or i=="!" or i=="*" or i.isspace():
#             continue
#         else:
#             new+=i
#             break
# print(new)


#37. Python program to count the number of even and odd numbers from a series of numbers.
# num=eval(input("enter a list of number"))
# even=0
# odd=0
# for i in num:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)


#38.Given list is lst=[1,2,3,4] but print 1 2 and 4 only

# lst=[1,2,3,4]
# for i in lst:
#     if i==1 or i==2 or i==4:
#         print(i,end=" ")


#39. Given list is lst=[1,2,3,4] but print 1 and 4 only
# lst=[1,2,3,4]
# for i in lst:
#     if i==1 or i==4:
#         print(i,end=" ")


#40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
# lst=[1,2,3,4]
# lst[1]="a"
# lst[2]=2
# print(lst)