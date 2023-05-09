# '''
# #print 10 times hello world
# a="Hello world"
# for i in range(0,10):
#     print(a)

# #print index of python
# a="python"
# b=len(a)
# for i in range(b):
#     print(i)

# #print of seperate line in python
# a="python"
# for i in a:
#     print(i)
# '''

# '''
# #print index=python
# a="python"
# b=len(a)
# for i in range(b):
#     print(i, "=", a[i])

# #sum and multiple
# a=[1,2,3,4,5,6]
# b=len(a)
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)
# mul=2
# for i in a:
#     mul=mul*i
# print(mul)
# '''
# '''
# #print integer and string of seperate line
# a=[1,2,'a','b']
# integer=[]
# string=[]
# for i in a:
#     if type(i)==int:
#         integer.append(i)
#     elif type(i)==str:
#         string.append(i)
# print(integer)
# print(string)

# #reverse of string
# a="hello"
# intstring=""
# for i in a:
#     intstring=i+intstring
# print(intstring)

# list="12345"
# reverse_string=""
# for i in list:
#     reverse_string=i+reverse_string
# print(reverse_string)

# #reverse of list
# a=[1,2,3,4,5]
# reverse=[]
# for i in a:
#     reverse=[i]+reverse
# print(reverse)


# name="madam"
# reverse=""
# for i in name:
#     reverse=i+reverse
# print(reverse)
# if name==reverse:
#     print("it is palandram")
# else:
#     print("it is not a palandram")
# '''

# # a=2
# # for i in range(1,11):
# #     print(a,'x',i,'=',a*i)

# # a=2
# # for i in range(10,0,-1):
# #     print(a,'x',i,'=',a*i)


# #calculate digit and alphabet
# a="sus1234"
# letter=0
# digit=0
# for i in a:
#     if i.isdigit():
#         digit=digit+1
#     elif i.isalpha():
#         letter=letter+1
# print(digit)
# print(letter)

#
# username="Susmi"
# password="2244"
# for i in range(5):
#     username1=input("enter a valid name")
#     password1=int(input("enter a valid password"))
#     if username==username1 and password==password1:
#         print("logged in")
#         break
#     else:
#         print("invalid")
# else:
#     print("5 attempts finished")

# for i in range(0,50):
#     print(i,"---",50-i)

# a=5
# factorial=1
# for i in range(1,a+1):
#     factorial=factorial*i
# print(factorial)

# a=[1,2,3,4,5]
# b=11
# for i in a:
#     print(b,"=",i)
#     b=b+1

# a=int(input("enter any number"))
# for i in range(a):
#     if i%2==0:
#         print(i,"even")
#     elif i%2==1:
#         print(i,"odd")



# a=15
# odd=[]
# even=[]
# for i in range(a):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd) 

# a=10
# even=0
# odd=0
# for i in range(a):
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd+i
# print(even)
# print(odd)


# 
# for i in range(1,10):
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")

# a=int(input("enter any number"))
# sum=0
# for i in range(1,a):
#     sum=sum+i
# print(sum)

# a=int(input("enter any number"))
# odd=0
# for i in range(a):
#     if i%2== 0:
#         pass
#     else:
#         odd=odd+i
# print(odd)

# a=int(input("enter any number"))
# 
# mul=2
# for i in range(1,11):
#     print(i,"x",mul,"=",mul*i)

# list=[1,2,3,4,5]
# for i in list:
#     print([i])


# a="sus223"
# digit=0
# letter=0
# list=[]
# for i in a:
#     if i.isdigit():
#         digit=digit+1
#     elif i.isalpha():
#         letter=letter+1
# print(digit)
# print(letter)

# name=input("enter any valid name")
# reverse=""
# for i in name:
#     reverse=i+reverse
# print(reverse)
# if name==reverse:
#     print("It is palindrone")
# else:
#     print("It is not palindrone")


# a=input("enter any valid word")
# reverse_string=""
# for i in a:
#     reverse_string=i+reverse_string
# print(reverse_string)

# a=10
# even=0
# odd=0
# for i in range(a):
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")


# a=6
# factorial=1
# for i in range(1,a+1):
#     factorial=factorial*i
# print(factorial)


# a="3355susmita"
# digit=0
# letter=0
# for i in a:
#     if i.isdigit():
#         digit=digit+1
#     elif i.isalpha():
#         letter=letter+1
# print(digit)
# print(letter)


# for i in range(1,26):
#     print(i)


# username="susi"
# password="4422"
# for i in range(5):
#     user_name=input("enter a valid name")
#     pass_word=int(input("enter a valid password"))
#     if username==user_name and password==pass_word:
#         print("login")
#         break
#     else:
#         print("invalid")
# else:
#     print("5 attempts finished")