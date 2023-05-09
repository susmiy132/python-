#comparision
'''
a=21
b=10
if(a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")

if(a!=b):
    print("a is not equal to b")
else:
    print("a is equal to b")

if(a<b):
    print("a is less than b")
else:
    print("a is not less than b")

if(a>b):
    print("a is greater than b")
else:
    print("a is not greater than b")'''


#and logical operators
'''
x=5
print(x>3 and x<8)
print(x>3 and x<4)

x=5
y=2
z=100
print(x>y and z)
print(x<y and z)
'''

#or logical operators
'''
x=5
print(x>3 or x<4)
print(x>8 or x<3)

#identity operators
x=5
y=5
z='python'
print(x is y)
print(x is not z)

#membership operators
a='python'
print("th" in a)
print("to" not in a)
'''

#bitwise operators 
'''
a=60
b=13
c=0

#and
c=a&b;
print("Value of c is",c)

#or (|)
c=a|b;
print("Value of c is",c)

#xor (^)
c=a^b;
print("Value of c is",c)

#negation 
c=~a;
print("Value of c is",c)

#left sift
c=a<<2;
print("Value of c is",c)

#right sift
c=a>>2;
print("Value of c is",c)

#a=5+7j
#print(type(a))

print(f"{0.1:.60f}")
print(f"{0.2:.60f}")
print(f"{0.1+0.2:.60f}")'''

a=10
print("The type of a is integer:", isinstance(a,bool))

#default arguments 
print("Hello{}, your balance is{}.".format("Adam",230))

#propositional arguments
print("Hello{0},your balance is{1}.".format("Adam",230))

#keyword arguments
print("Hello{name}, your balance is{bln}.".format(name="Adam",bln=230))

#name="python"
#print(name[:5])

