'''
#Q1 - Write a Python program that prints a rectangular pattern of asterisks (*).

x= int(input("number of rows: "))
y = int(input("number of columns :"))
for i in range(4):
    for j in range(i):
        print("*****",end="")
        break
    print()
    

#Q2-  Write a Python program to find the sum of all even numbers between 1 and 100
#      using a while loop.


i=0
c=0
while i<=98 :
    i+=2
    c+=i
print("the sum of all even numbers between 1 and 100 : ",c)

  
#Q3-  Create a list of the first 10 multiples of a given number using a for
#     loop.

num=int(input("enter the number : "))

multi =[]

for i in range(1,11) :
    multi.append(num*i)
print("first mulitiples of a given number ",multi)
        

--------------------
##Q4 - Write a Python program to find the maximum number in a list
#     without using the built-in max() function.

x=[5,4,2,6,3,7,1]
max=x[0]
c=[]
for i in range(1,len(x)):
    if x[i]>max:
        max=x[i]
c.append(max)
print(c)


##Q5 -Generate a Fibonacci sequence of a given length using for loop.
a=0
b=1
print(a)
print(b)
for i in range(0,11):
    c=a+b
    print(c)
    a=b
    b=c
    


#Q6 - Write a Python program to calculate the factorial of a number
#     using a for loop

num= int(input("Enter a number : "))
f=1
for i in range(1,7):
    f=f*i
print(f)


#Q7 - ) Write a Python program to reverse a list without using the built-in
#       reverse() method or slicing
x=[5,3,1,2,4]


#Q8 -  Write a Python program to print all prime numbers between 1 and
#      50.

for i in range(1,51):
    if prime number

#Q9 Perform various list operations like appending, inserting,
#   removing, and sorting.
a=[1,"Martin",23,"salesman"]
a.append(15000)
print(a)

a.insert(3,"unmarried")
print(a)

b=[1,2,3,4,5]
b.remove(4)
print(b)

b.sort(reverse=True)
print(b)

#Q12 -  Write a Python program that prints a pattern of asterisks (*).
 
for i in range(5):
    for j in range(i,5):
        print("*" , end="")
    print()

#Q13- Write a Python program that determines if a student passes or
#     fails based on their score
mark = float(input(" Enter the mark :"))
if(mark>33):
    print("congrats u passed")
else:
    print("falied")

#Q14- Write a Python program to classify a person based on their age

age=int(input("Enter your age : "))
if age<13 :
    print("child")
elif age>13 and age<19:
    print("Teenager")
elif age>20 and age<60:
    print("Adult")
else:
    print("Senior citizen")
'''
#Q15  Write a Python program that prints numbers from 1 to 20 but
#      skips multiples of 3

x=[5,4,2,6,3,7,1,6]
print(x[0])
