# Exception handling
#------------------------------

#x=int(input("enter a number :"))
#y=int(input("rnter a number:"))
#z=x/y     #critical satatement
#print (z)

'''
try:
    x=int(input("enter a number :"))
    print(10/x)
#except ZeroDivisionError:
#   print("division by zero is not allowed")

except ZeroDivisionError as e:
    print("division by zero is not allowed",e)    # get the error explaination
except ValueError :
    print("Please enter a number ")

finally :
    print("done")


print("hi")
try:
    x=int(input("enter a number :"))
    if x<0:
        raise ZeroDivisionError

except ZeroDivisionError as e:
    print("division by zero is not allowed",e)    # get the error explaination
except ValueError :
    print("Please enter a number ")
finally :
    print("Thank you")
 
#----------------------------------------------------------------------------
#Python modules
import math
#help(math)

print(math.pi)
print(math.factorial(5))


import math as m
print(m.sqrt(100))

from math import factorial,pi,floor,ceil
print(factorial(4))
print(pi)

from math import *
print(floor(7.9))
print(ceil(7.9))

#-----------------------------------------------------------------

from datetime import *
#help (datetime)
x=datetime.now()
print(x)
print(x.month)
print(x.year)
print(x.minute)
print(x.second)
print(x.strftime('%c'))

#  TO GET THE USER AGE  
x=datetime.now()
y=input("Enter you year of birth (eg:01-01-2003) :")
print(y)
z=y.split('-')
print(f"{x.year-int(z[2])} years {x.month-int(z[1])} months {x.day-int(z[0])} days ")


#y=int(input("Enter you year of birth :"))
#print("Age is :",(x.year-y))




#----------------------------------
from random import *
print(random())  #[0.0-1.0]

print(randint(1000,9999))

print(choice(["stone","paper","scissors"]))

x=[1,2,3,4,5]
shuffle(x)
print(x)                                     #user vs computer



#---------------
from string import*
print(ascii_letters)
print(digits)
print(punctuation)
print(printable)                   # password making

     
#file operations


from datetime import *
y=input("Enter you year of birth (eg:01-01-2003) :")
print(y)
z=y.split('-')
print(f"{x.year-int(z[2])} years {x.month-int(z[1])} months {x.day-int(z[0])} days ")




try:
    a=int(input("enter a number :"))
    b=int(input("enter a number : "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("sorry zero is not allowed to divide")
except ValueError:
    print("please enter a number ")
finally:
    print("thank you")


print("hello")
x=int(input(" Enter a number :"))
y=int(input("Enter a number: "))
try:
    z=x/y
    print(z)
except ValueError:
    print("please enter a number")
    
from math import *
print(pi)
print(sqrt(25))

from datetime import *
x=datetime.now()
y=input("Enter you year of birth (eg:01-01-2003) :")
print(y)
z=y.split('-')
print(f"{x.year-int(z[2])} years {x.month-int(z[1])} months {x.day-int(z[0])} days ")

try:
    a=int(input("enter a number :"))
    b=int(input("enter a number : "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("sorry zero is not allowed to divide")
except ValueError:
    print("please enter a number ")
finally:
    print("thank you")

from random import *
print(random())  #[0.0-1.0]

print(randint(1000,9999))

print(choice(["stone","paper","scissors"]))

x=[1,2,3,4,5]
shuffle(x)
print(x)  
'''
try:
    x=int(input("Enter a number : "))
    y=int(input("Enter a number : "))
    print(x/y)
except ZeroDivisionError:
    print("division by zero is not possible")
except ValueError:
    print("please enter a number")
finally:
    print("Thank you")
    
    
