#1 print softwarica 10 times
# i=1
# while i<11:
#    print("softwarica")
#    i+=1

#2sum of a list
# list=eval(input("Enter the numbers"))
# sum=0
# i=0
# while i<len(list):
#    sum+=list[i]
#    i+=1
# print(sum)
      

#3print each character using indexing
# x=input("Enter the characters")
# i=0
# while i<len(x):
#    print(x[i])
#    i+=1


#5 multiplication of a each element. given list=[4,5,3,2]
# list=[4,5,3,2]
# mul=1
# i=0
# while i<len(list):
#    mul=mul*list[i]
#    i+=1
# print(mul)


#4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
# list=[1,"a","c",2,3,4]

# i=0
# list1=[]
# while i<len(list):
#    if type(list[i])==int:
#       list1.append(list[i])
#    i+=1
# print(list1)


#6. multiplication table of a given number
# x=int(input("Enter the numbers"))
# i=1
# while i<11:
#    print(x,"*",i,"=",x*i)
#    i+=1


 #7. reverse a list
# list=eval(input("Enter the numbers"))
# rev=[]
# i=0
# while i<len(list):
#     rev=[list[i]]+rev
    
#     i+=1
# print(rev)


#8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]
# list=[1,2,3,4]
# i=0
# list1=[]
# while i<len(list):
#     l=list[i]+1
#     i+=1
#     list1.append(l)

# print(list1)


#9. given number is prime or not
# x=input("Enter the numbers")
# i=2
# str=""
# while i<x:
#     if x%i==0:
#      str=str+"Not prime"
#      break
#     i+=1
# if str:
#     print(str)
# else:
#     print(" prime")
# x=int(input("Enter the numbers"))

# i=2
# while i<x:
#     if x%i==0:
#         print(" not prime")
#         break
#     i+=1

# else:
#     print(x,"prime")

        
#10. Write a python program to display all the prime numbers within a given range.
# start=int(input("Enter the number: "))
# end=int(input("enter a number: "))

# while start<end:
#     j=2
#     while j<start:
#         if start%j==0:
#             break
#         j+=1
        
#     else:
#       print(start," prime")
#     start+=1


#11. Python program that accepts a string and calculate the number of digits and letters and space
# x=input('enter the numbers')
# digit=0
# letters=0
# space=0
# i=0
# while i<len(x):
#    if (x[i]).isdigit():
#       digit+=1
#    elif x[i].isalpha():
#       letters+=1
#    elif x[i].isspace():
#       space+=1
#    i+=1
# print(digit)
# print(space)
# print(letters)


# #12. Python program to check the validity of username and password input by users
# username1=input("Enter the name")
# password1=input("Enter the password")
# i=0
# while i<1:
#    username=input("Enter the name")
#    password=input("Enter the password")
#    if username==username1 and password==password1:
#       print("logged in")
      
#    else:
#       print("Not logged in")
#    i+=1



#13. program to print the given number is odd or even
# num=int(input("enter the numbers"))
# i=0
# while i<1:
#     if num%2==0:
#         print("even")
        
#     else:
#         print("odd")
    
#     i+=1


#14. factorial of a given number
# num=int(input("Enter the numbers"))
# fact=1
# i=1
# while i<num+1:
#     fact=fact*i

#     i+=1
# print(fact)



#15. program to check given number is palindrome or not
# x=input("Enter the numbers")
# str=""
# i=0
# while i<len(x):
#     str=x[i]+str
#     i+=1
# if str==x:
#     print("pallindrome")
# else:
#     print("Not a pallindrome")


#16. program to check given number is armstrong or not
# num=(input("Enter the numbers"))
# sum=0
# b=len(num)
# i=0
# while i<b:
#     sum=sum+int(num[i])**b
#     i+=1
# if sum==int(num):
#     print("Armstrong")
# else:
#     print("Not a armsteing")


#17 program to check number is perfect square
# num=int(input("Enter the numbers"))
# i=1
# while i<num:
#     if i*i==num:
#         print("square")
#         break
#     i+=1
# else:
#         print("not square")
    

#18program to check a number is a perfect number

# x=int(input("enter the numbers"))
# i=1
# sum=0
# while i<x:
#     if x

  
  
  



#19  print multiplication table from 1-8
# i=1
# while i<9:
#     j=1
#     while j<11:
#         print(i,"*",j,"=",i*j)
#         j+=1
#     i+=1

#20 given list=lst=[1,2,3,4] but print 1 and 2 only
# list=[1,2,3,4]
# list1=[]
# i=0 
# while i<len(list):
#  if i==2:
#   break
 
#  list1.append(list[i])
#  i+=1

# print(list1)
 



#21 python program to calculate the sum of all the odd numbers in the given range
# x=int(input("Enter the numbers"))
# sum=0
# i=1
# while i<x:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print(sum)

     


#22 python program to calculate the sum of all the even numbers in the given range
# x=int(input("Enter the numbers"))
# sum=0
# i=1
# while i<x:
#     if i%2==0:
#         sum+=i
#     i+=1
# print(sum)


#23 python program to count the space of a given string      wrong program
# x=input("Enter the string")
# space=0
# i=0
# while i<len(x):
#     if x[i].isspace():
#         space+=1
#     i+=1
# print(space)


#24 given list is [1,2,3,4] but expected output is [1,8,27,64]
# list=[1,2,3,4]
# list1=[]
# i=0
# while i<len(list):
#  x=list[i]**3
#  i+=1
#  list1.append(x)
# print(list1)






    



#25 multiplication of a list
# list=eval(input("Enter the list"))
# mul=1
# i=1
# while i<len(list):
#     mul=mul*list[i]
#     i+=1
# print(mul)
    
 

    

#26  place  break statements in the for loop so that it prints from 0-7 only including7 goven range=50
# i=0
# while i<50:
#     if i==8:
#      break
#     print(i)
#     i+=1





#27 write a for loops that iterates through the string and and prints every letter
# x=input("Enter the characters")
# i=0
# while i<len(x):
#     print(x[i],end=" ")
#     i+=1

#28  write a for lopp which print hello and each name in ihe last present in the given list
# list=["ram","shyam",1,2]
# i=0
# while i<len(list):
#     if list[i].isalpha():
#         print("Hello!",list[i])
#     i+=1


#29 Using a for loop and append each item method  each other with the dr prefix  to the list
# list=[1,2,3,4,"krishna","srila"]
# list1=[]
# i=0
# while i<len(list):
#     x=("dr "+str(list[i]))
#     list1.append(x)
    
#     i+=1
# print(list1)


#30  write a for loop which appends the square of a each number  to the new list
# list=eval(input("Enter the numbers in list"))
# list1=[]
# i=0
# while i<len(list):
#     x=list[i]**2
#     list1.append(x)
#     i+=1
# print(list1)


    
#31 write a for loop using an if statement  that append s each number to the new luist if it is positive
# list=eval(input("Enter the numbers"))
# list1=[]
# i=0
# while i<len(list):
#     if list[i]>=0:
#         list1.append(list[i])
#     i+=1
# print(list1)


# 32 write a program that prints all the numbers from 0-6 except 3 and 6 given list=[0,1,2,3,4,5,6]   
# list=[0,1,2,3,4,5,6]
# i=0
# list1=[]
# while i<len(list):
#     if list[i]!=3 and list[i]!=6:
#      list1.append(list[i])
     
#     i+=1
# print(list1)

#33 write a for loop whicj appends the type of each element in the first list to second list
# list=[1,3.4,"k","heu",83]
# i=0
# list1=[]
# while i<len(list):
#    x=type(list[i])
#    list1.append(x)
#    i+=1
# print("list1=",list1)


#34   use else block to display amessage "Done" after a successful execution of for loop
# i=0
# while i<5:
#     print(i)
#     i+=1
# else:
#     print("done")


#35 write a while loop statement to print the folowing series 105 98 -------7
# i=105
# while i>=7:
#     print(i,end=" ")
#     i-=7


#36  removal bad characters from the given string bad_chars=[':',':','!','*'] given string="py;th*on ! ;py * t*h:o !n"      mistake

# bad_chars=[':',';','!','*',".",",","'"]
# given_str="py:th;o'n.h;py * t*h:o !n,"
# i=0
# while i<len(bad_chars):
#     given_str=given_str.replace(bad_chars[i],"")
#     i+=1
# print(given_str)


#37   python program to count yhe number of even and odd  from a series of a numbers
# i=1
# even=0
# odd=0
# num=int(input("enter the numbers"))
# while i<num:
#     if i%2==0:
#         even=even+1
#     else:
#         odd+=1
#     i+=1
# print(even)
# print(odd)
   


#38  Given list is lst=[1,2,3,4] but print 1,2 and 4 only
# list=[1,2,3,4]
# i=0
# list1=[]
# while i<len(list):
#     if list[i]!=3:
#         list1.append(list[i])
#     i+=1
# print(list1)

# i=0
# while i<len(list):
#     if list[i]!=1:
#         print(list[i])
#     i+=1
    


 #39   Given list is lst=[1,2,3,4] but print 1 and 4 only
# lst=[1,2,3,4]
# list1=[]
# i=0
# while i<len(list):
#     if list[i]!=2 and list[i]!=3:
#         list1.append(list[i])
#     i+=1
# print(list1)


# lst=[1,2,3,4]
# for i in lst:
#    if i==2:
#       continue
#    if i==3:
#       continue
#    print(i)


#40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
# list=[1,2,3,4,5]
# list1=[]
# i=0
# while i<len(list):
#     if list[i]==3:
#         list1.append("")

#         list[i]="a"
#         list.insert(i+1,2)
#     i+=1
# print(list[i])
# list=[1,2,3,4,5]
# i=0
# while i<len(list):
#     if i==2:
#         list.remove(list[i])
#         list.insert(i-1,"a")
#     i+=1
# print(list)


#40  given list=[1,2,3,4] but expected output is [1,'a',2,4]
# list=[1,2,3,4]
# list1=[]
# for i in list:
#  if i==3:
#   list1.append("a")
#  else:
#   list1.append(i)
# list.remove(3)
# print(list1)
