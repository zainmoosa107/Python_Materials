'''
a= "top spot"
x=a.split( )
y="".join(x)
y==y[::-1]
print(y)

#Q13
for i in range(5):
    for j in range(i+1):
        print(i+1,end =" ")
    print()

for i in range(5):
    for k in range(5-i):
         print(k,end= " ")
    print()

count=0
for i in range(4):
    for j in range(i+1):
        count+=1
        print(count,end=" ")
    print()
'''

num=int(input("enter a number : "))
def prime_number(num):
    flag=True
    if num<=1:
        print("It's not a prime number ")
    for i in range(2,num):
        if num%i==0:
            flag=False
        break
    if flag:
        print("Prime")
    else:
        print("not in prime")
prime_number(num)

'''

#--------------------------
##Scope
#Global scope- can access outside varible in function

x=10
def greet():
    print("inside",x)

greet()
print("outside",x)

#we cannot make any change i.e addition sub etc inside the function

x=10
def greet():
    #x+=20
    print("inside",x)

greet()
x+=30
print("outside",x)


#Local scope
x=10
def greet():
    x=12 #local scope
    print("inside",x)
greet()
print("outside",x)

#Global keyword
x=15
def greet2():
    global x    #keyword
    x+=5
    print("inside",x)
greet2()
print("outside",x)

#---------------------------------------
#recursion is a programming technique where a function calls itself in order to solve
#a program

def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num-1)
num=int(input("Enter a number :"))
print(factorial(num))
'''

#lambda-filter, map,reduce
#list -comprehension


count=0
for i in range(4):
    for j in range(i+1):
        count+=1
        print(count,end=" ")
    print()

for i in range(0,5):
    for k in range(5-i):
         print(k,end= " ")
    print()


# to check  prime number
'''
while (True):
    num=int(input("Enter a number :"))
    def prime_number(num):
        flag = True
        if num<=1:
            print("it's not a prime number")
        for i in range(2,num):
            if num%2==0:
                flag=False
        if flag:
            print("prime")
        else:
            print("not prime")
    prime_number(num)
'''
def greet(name):
    print(f"Hello,{name}")
greet("zain")


def greet1(a,b):
    return a+b
add=greet1(4,6)
print(add)

def greet(name,place='clt'):
    return name,place
reg=greet("zain")
print(reg)

'''
y=5
def modify_global():

    print("inside",y)
modify_global()
print(y)
'''
y=45
def add():
    #y+=5
    print("inside",y)
add()
print(y)


x=10
def greet():
    x=12 #local scope
    print("inside",x)
greet()
print("outside",x)



a=5
def modifiy():
    global a
    a=20
    print("inside",a)
modifiy()
print(a,"outside")

num=int(input("Enter a number : "))
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(num))
