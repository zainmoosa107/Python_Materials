#task -2
    
#-------------------------------------------------
#1( to find factorial of a number)
i=int(input("enter a number:"))
f=1
while(i>0):
        f=f*i
        i=i-1
print(f)

#------------------------------------------------------

#2(print numbers from 1 to 10   )
i=1
while(i<=10):
        print(i)
        i+=1

#---------------------------------------------------

        
#3(print numbers from 1 to 10 (without 7)  )
i=1
while(i<=10):
        i+=1
        if(i==7):
                continue
        print(i)

#-------------------------------------------------


#4(password)

while(True):
        password=input("enter the password:")
        if(password=="majid"):
                            print("correct password")
        if(password=="quit"):
                            break

                            
#----------------------------------------------------


#5(sum of digits)
i=int(input("enter positive digits:"))
sum=0
while(i>0):
        sum=sum+i%10
        i=i//10
print(sum)

#---------------------------------------


#6 exponent
#---------
e=int(input("enter a exponent value:"))
i=0
while(i<e):
        i+=1
        if(i<=e):
                c=(i**e)
                d=c+i
                print(d)
                

#----------------------------------------


#7 to find factors of a number
#-----------------------------
while(True):
        n=int(input("enter a number:"))
        i=0
        while(i<n):
                i+=1
                if(n%i==0):
                        print(i)
