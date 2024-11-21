#-------------------TASK - 03-----------------------
#Q1- Write a Python program to sum up all the items in a list.
'''
NUM=[1,2,3,4,5,6]
i=0
sum=0
while i <len(NUM):
    #print(x[i])
    sum+=NUM[i]
    i+=1
print(f"Total :{sum}")


#Q2 -  Write a Python program to get the largest number from a list

NUM_1=[1,2,3,4,5,6]

i=0
Max=NUM_1[0]
while i<len(NUM_1):
    if (Max< NUM_1[i]):
        Max=NUM_1[i]
    i+=1
print(f"Maximum value : {max}")

x=[2,4,10,15,6]
i=0
Min= x[0]
while i<len(x):
    if (Min>x[i]):
        Min= x[i]
    i+=1
print(f"MIN :{Min}")
    
        

#Q3- Write a Python program to Count occurrences of an element in a list
Y =[3,2,3,4,3,5,3]
i=0
num=3
count=0
while i<len(Y):
    if(num==Y[i]):
        count+=1
    i+=1
print(f"count of {num} is {count}")

'''

sample=[4,5,6,4,5,6,7]
number = int(input( "Enter a number : "))
i=0
count = 0
while i <len(sample) :
    if(number == sample[i]):
        count+= 1
    i+=1
if count==0:
    print(f"Item Not found")
else :
    print(f"count of {number} is {count}")

'''
#Q4 -Write a Python program to Sum the number of digits in a list.
sampl_list=[1,2,3,4,5]
i=0
a=sampl_list[i]
b=1
print(a)
print(b)




'''#Q5 - Write a Python program to count Even and Odd numbers in a list .
'''
'''
sample =[1,2,3,4,5,6,7]
i=0

even_num=[]
odd_num=[]
while i<len(sample):
    if i%2==0 :
        even_num.append(sample[i])
        print(even_num)
        i+=1
    else:
        odd_num.append(sample[i])
        i+=1
        print(odd_num)
'''
#Q6 - Write a Python program to print positive numbers in a list
'''
sample=[1,3,-2,-6,4,9]
i=0
positive=[]
negative=[]
while i<len(sample):
    if sample[i]>0:
        positive.append(sample[i])
        print(positive)
        i+=1
    else:
        negative.append(sample[i])
        print(negative)
        i+=1
        
#Q8 Write a Python program to remove duplicates from a list .

numbers=[1,2,3,4,5,6,7,2,0,1,4,5,2]
sample_set=set(numbers)
new_numbers=list(sample_set)
print(new_numbers)
'''
#Q9- Write a Python program to print the numbers of a specified list after removing even numbers from it.

a=[1,2,3,4,5,6,7,8,9]
i=0
b=[]
while i<len(a):
    if i%2!=0:
        b.append(a[i])
    i+=1
print(b)
    
    
        
