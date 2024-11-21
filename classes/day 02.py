#guido van rossum -invented 1991
# interprtor convert high level language to low level (computer language )
# easy to write
#object oriented
#dynamic typed
#open

# Logical operators

print (5>2 and  5==5)#true
print (5>2 and 4==5) #False
print (5>10 and 5==5) #False
print(5>10 and 5!=5) #false

print(5>2 or 5==5) #true
print(5>2 or 4==5) #true
print(5>10 or 5==5) #true
print (5>10 or 5!=5) #False

print(not 5>2) #false


#1 exemption concate
print ("Hello " + "world")

#2 exemption
print("Hello " *5)

#Variables
x = 'codeme'
print(x)

username = 'zain'
print(username)

rollno=17
print (rollno)

x= 10
y = 20
print(x+y)

print(y**x)
print(y/x)
#dynamic typed programming language
x = 10
x= 'hello'
print (x)

#Escape sequences
print('hello \nworld')
print('hello \tworld')

print("i'm 20 years old")
print ("my name is \"zain\" ")

#swapping
  # method 1 
a=10
b=5
temp= a
a=b
b=temp
print(a)
print(b)
  # method 2
a=10
b=5
a,b=b,a
print(a)
print(b)

a,b,c = 10,5,15
a,b,c=b,c,a

print(a)
print(b)
print(c)

#Type casting
x="12.3" #str
y= float(x) # converting to float
print (y*10)

print (type(y))



x=155
print (type (x))
y=float(x)
print(y)

print (type (y))

x=123.4
y=int(x)
print(y)

'''inplace operator'''
a=10
a+=15 # 10+15 = 25
print(a)


#identity operator - is , is not ,id()
#membership operator - in ,not in
