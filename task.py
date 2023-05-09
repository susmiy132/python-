'''
#1. write a program to accept two integer and check wheather they are equal or not
a=10
b=20
if a==b:
    print("a is equal to b")
elif a!=b:
    print("a is not equal to b")
else:
    print("invalid")

#2. write a program to check wheather a given number is even or odd
a=int(input("enter any number"))
if a%2==0:
    print("a is even number")
else:
    print("a is odd number")

#3. write a program to check wheather a given number is positive or negative
a=int(input("enter any number"))
if a>0:
    print("a is a positive number")
elif a<0:
    print("a is a negative number")
else:
    print("zero")

#4. write a program to check wheather an alphabet is a vowel or a consonent.
letter=str(input("enter any letter"))
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("an alphabet is a vowel letter")
else:
    print("an alphabet is a consonent letter")

#5. print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a=int(input("enter any number"))
b=int(input("enter any number"))
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")
'''
'''
#6. print "Hello" if a is equal to b,and c is equal to d.
a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
d=int(input("enter any number"))
if a==b and c==d:
    print("Hello")
else:
    print("invalid")

#7. print "Hello" if a is equal to b, or if c is equal to d.
a=int(input("enter any number"))
b=int(input('enter anu number'))
c=int(input("enter any number"))
d=int(input("enter any number"))
if a==b or c==d:
    print("Hello") 
else:
    print("invalid")
'''

'''
#8. acccept input from user
# user%3==0 and user%5==0 print "FizzBuzz"
# user%3==0 print "Fizz"
# user%5==0 print "Buzz"
user=int(input("enter any number"))
if user%3==0 and user%5==0:
    print("FizzBuzz")
elif user%3==0:
    print("Fizz")
elif user%5==0:
    print("Buzz")
else:
    print(user)'''

'''
#9. Check wheater the user input number is even or odd and display it to user.
a=int(input("enter any number"))
if a%2==0:
    print("The given number is even")
else:
    print("The given number is odd")


#10. WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint: more than 70 = distinction, more than 60 = first, 
# more than 40 = pass, less than 40 = fail.
sub1=int(input("enter the marks of subject"))
sub2=int(input("enter the marks of subject"))
sub3=int(input("enter the marks of subject"))
sub4=int(input("enter the marks of subject"))
total_marks=sub1+sub2+sub3+sub4
percentage=total_marks/400*100
if percentage>70:
    print("distinction")
elif percentage>60 and percentage<70:
    print("first")
elif percentage>40 and percentage<60:
    print("pass")
elif percentage<40:
    print("fail")
else:
    print("invalid")


#11. what is the output of "APPLE">"apple"?
print('APPLE'>'apple')


#12. write a python program to display your details like name, age, address in three different lines.
name="Susmita Rana"
age="18"
address="kanchanpur"
print("My name is",name)
print(age,"year old")
print("My address is", address)
'''
'''
#13. write a python program which accepts the rdius of a circle from user and compute the area.
radius=int(input("enter the radius of a circle"))
area=3.14*radius**2
print(area)

#14. write a python program which accepts the smallest one.
user1=int(input("enter any number"))
user2=int(input("enter any number"))
user3=int(input("enter any number"))
if user1<user2 and user1<user3:
    print("the smallest number is",user1)
elif user2<user3 and user2<user1:
    print("the smallest number is",user2)
elif user3<user1 and user3<user2:
    print("the smallest number is",user3)
else:
    print("invalid")

#15
a=10
b=20
c=5
if a>b and a>c:
    print("a is the largest number is",a)
elif b>c and b>a:
    print("b is the largest number is",b)
elif c>a and c>b:
    print("c is the largest number is",c)
else:
    print("invalid")
'''

#16