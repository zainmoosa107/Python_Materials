#-----------PYTHON TEST------------

#Q1Ans: Guido van Roosum

#Q2Ans: [3,4]

#Q3Ans : import module_name

#Q4Ans : !

#Q5Ans : lambda

#Q6Ans : Removes leading and trailing whitespace from a string

#Q7Ans : file = open('filename.txt,'r')

#Q8Ans : length()

#Q9 Ans: (c) - 10,20   20,10

#Q10 Ans: (b) - [x for x in iterable]


#Q11 
num=[1,2,3,4,5]
square=[]
for i in num:
    sqr=i**2
    square.append(sqr)
print(square)

#Q12
num=[1,2,5,7,6,4,9,8,10]
num.sort()
print(num[-2])

#Q13
num=[1,2,3,4,5,4,2,1,5]
num1=[]
for i in num:
    if i not in num1:
        num1.append(i)
print(num1)

#Q14
num=(1,2,3,4,5,6)
print(num[::-1])

#Q15
a=[(1),(2),(3),(4)]
b=[(3),(4),(5),(6)]
a1=set(a)
b1=set(b)
result=a1.intersection(b1)
print(result)

#Q16
a={1,2,3,4,5}
b={6,7,8,9,10}


#Q17
dict_1={'a':1,'b':2,'c':3}

x=dict_1.keys()
y=dict_1.values()

result=dict(zip(y,x))
print(result)

#Q19
num=int(input("Enter a number : "))
def factorial(num):
    if num==1:
        return 1
    else:
         return num*factorial(num-1)
print(factorial(num))

#Q20
num=[1,2,3,4,5,6,7,8,9]
even_num=list(filter(lambda x:x%2==0 , num))
print(even_num)

#21
num=[1,2,3,4,5,6]
sqr_num=list(map(lambda x:x**2, num))
print(sqr_num)

#22
'''
num=[1,2,3,4,5]
def sum(num):
'''

#23
text= "apple"
vowels= "aeiou"
count=0
for i in text:
  if i in vowels:
      count+=1
print(count)

#24
text="banana"
result=text.title()
print(result)


#26
class Bankaccount:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    def deposits(self):
        deposit=int(input("enter deposit amount : "))
        self.balance+=deposit
        print(f"{self.balance} deposited success fully")
    
    def withdraw(self):
        withdraw=int(input("enter withdrawal amount : "))
        if withdraw > self.balance:
                     print("insufficient balance")
        else:
            self.balance-=withdraw
            print(f"{self.balance} withdrawal is succesfull")

    def check_balance(self):
        print(f"Your account number : {self.account_no},\nyour balance : {self.balance}")

acc1=Bankaccount(123,500)
acc1.deposits()
acc1.withdraw()
acc1.check_balance()

#27
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
            
            
    


'''
#30

try:
    num=[1,2,3,4,5,6,7,8]
    Sum=0
    for i in num:
        Sum=sum(num)
    print(Sum)
except: 
'''








