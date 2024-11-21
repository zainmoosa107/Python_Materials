#day-4
'''
while loop
----------
.its a looping conditional statements
.looping statements will continue if the given condition is True
'''
#method 1
#--------
i=1#(initialization)here we taken i as a variable assign as 3
while i<=6:#(condition)while loop will start if the condition is true (here i is less than 6 or i<6)
print(i)#if i is less than 6 it will print the number
i=i+=1#it will add 1 to i until i<=6 else loop continues till

print("the given above numbers are less than 6")#this statement exceute if the loop over
#method 2
----------
i=10#(initialization)
while i>=1:#(condition)while loop will start if the condition is true
print(i)
i=i-1
print("thanks")#this statement exceute if the loop over

#method 3
---------

i=1#(initialization)
while i<=10:#(condition)while loop will start if the condition is true (here i is less than 6 or i<6)
print(11-i)#if i is less than 6 it will print the number
i+=1#it will add 1 to i until i<=6 else loop continues till
print("the given above numbers are less than 6")#this statement exceute if the loop over

#method 4
#----------
i=1#(initialization)
while i<=10:#(condition)while loop will start if the condition is true
print(11-i)
i+=1
print("thankyou")#this statement exceute if the loop over

#iteration
#----------
#each cycle of loop is called iteration

#break statement
#---------------
#if we give break statement it jump out of the loop
#1
#--
count=0
while count<5:
count+=1
if count==3:
break
print(count)
print("end")

#2
#--

count=10
while count<=10:
print(count)
if count==1:
break
count-=1
print("end")

#----------------------------------------------------------------
