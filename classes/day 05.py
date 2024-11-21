'''
salary = float (input( " Enter your name salary : ")
yoe = float( input( "Enter your experience : ")
if yoe>5 :
    print(f"Congrats you got a bonus {salary +(salary+(5/100))}")
else :
    print("oops")


l = float(input("Enter the length :"))
b=float(input("Enter the breadth :"))
if l = b :
    print("it's a square")


a= int(input( "Enter first value : "))
b =int(input( "Enter second value : " ))
if a>b :
    print(f"{a} is greater than {b}")
else :
    print(f" {b} is greater than {a} ")


mrp=100
qty= int(input( "Enter the quantity : " ))
total = mrp*qty

if total>1000 :
    print(f"Discount Total Price : {total - (total*(10/100))}")
else :
    print( "Total amount {total}")
'''

#-----------------------

'''# while loop
i=1
while i<=10:
    print(i)
    i+=1


i=1
while i<=10:
    print(i)
    if i ==5:
        break #control statement (exit) 
    i+=1
print( "end")

#Iteration - loop cycle(one cycle is called as Iteration)
'''

'''i=0
while i<=10:
    i+=1
    if i ==5:
        continue# control statement(exit) - to skip the num (to skip a iteration)
    print(i)
print( "end")
'''
#-------------------------------------
'''

count=0
while True:
    if count<5:
        password = input("Enter your password " )
        if password == "code12##" :
            break
        else :
            print("invalid password ")
    else :
        print ("oops limit reached")
        break
print("end")
'''
#---------------------------------------
'''
num = int(input("Enter the number"))
i =1
while i<=10 :
    print(f"{i}*{num}={i*num}")
    i+=1
print("end")'''
#-----------------------------------
'''
#1
i =0
while i<=18 :
    i+=2
    print(i)
'''
#------------------------------------
''''
num=1
while num <= 4:
    num+=1
    i=0
    while i <=9:
        i+=1
        print(f"{i} * {num} = {i*num}")

'''
#------------------------------------------------
'''num = 0
while num <=9:
    num+=1
    print(num)
    i=1
    while i<=9:
        i+=1
        print("i **=num")
'''
#-------------------------------------


    
    
    


