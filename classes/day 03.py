'''# identity operator - is,is not and id() 

a=10
b=5
c=10

print(a is b)
print(a is c)

print( a is not b)
print(a is not c)

print (id(a))
print(id(b))
print(id(c))

a=5

print(id(a))
print(id(b))
print(id(c))


# a=10 it will be stored in database in which a is just a nametag
# c=10 therefore 10 is already in the database c is just a nametag
# object is under the class


# Membership operators - in ,not in

a="codeme hub"
print("me h" in "codeme hub")
print("me h" not in "codeme hub")
print("ist" not in "codeme hub")


print("me h" in (a) )
print ("me h" not in (a))


#round() - used to round a number to specified number of decimal places

x =3.14159
print(round(x))
print(round(x,2))
print(round(x,3))

#len() - to find the length of the object, such as string,list ,tuple
text = "welcome to codeme"
print(len(text))


#input()

name = input("Enter your name : ")
age = input( " Enter your age : ")

print( "Your name is " + name + " and i'm "+age+" years old " )

#string formatting
  # format method
name = input("Enter your name : ")
age = int (input( " Enter your age : "))
#print( "Your name is " + name + " and i'm "+age+" years old " ) ---- will not concat (string and int)


print("my name is {} and i'm {} years old ".format(name,age))
#{}placeholders --it can read or concat string,int,float etc


#f-string
name = input("Enter your name : ")
age = int (input( " Enter your age : "))
print(f"my name is {name} and i'm{age} year old")
'''
# statements- interpretor execude code

#Conditional Statement
#if statement
x = int(input("Enter a number  "))
if(x>10):
        print(f"{x} is greater than 10")
print("end")

#if else statement
z =int(input("Enter a number "))
if(x%2 == 0):
    print(f"{z}is even number")
else:
    print(f"{z} is odd number")
print("Program End")

#if else ladder, if elif else,while loop

        

