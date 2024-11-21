#sk OOPS - Object Oriented Programming

#class - prototype/Blueprint    - logical entity
#object - instances/examples of class - real world 
#         *properties-attributes
#         * behaviours-methods
#__init__()     - constructor method


#self - referenece of that object
'''
class Watch:
    def __init__(Self,Brand,Color):
        Self.Brand_name=Brand
        Self.color=Color
        Self.time="12:00PM"
    def display_time(Self):
        print(f"Time:{Self.time}")

Watch1=Watch("Rolex","Silver")
Watch2=Watch("Titan","BLack")
Watch1.display_time()

print(Watch1.Brand_name,Watch1.color)
print(Watch2)
'''

'''
class Watch:
    def __init__(self,Brand,Color,Price):
        self.Brand_name=Brand
        self.color=Color
        self.time="12:00PM"
        self.price=Price
    def display_time(self):
        print(f"Time:{self.time}")

    def Showdetails(self):
        print(f" Brand : {self.Brand_name},Color : {self.color},Time: {self.time},price : {self.price}")

    def update_time(self,new_time):
        self.time=new_time
        print(f"updatetime :{self.time}")

    def is_affordable(self,budget):
        if self.price<=budget:
            print("it's affordable")
        else:
            print("not affordable")
            
Watch1=Watch("Rolex","Silver",250000)
Watch2=Watch("Titan","BLack",6999)
Watch1.display_time()


Watch1.Showdetails()
Watch2.Showdetails()
Watch1.is_affordable(5000000)
Watch1.update_time("2:00PM")


#4 pillars

  - Data encapsulation
  - Data abstraction
  - Data inheritance
  - Data polymorphisam     eg: + operator


class Animal:                           #parent class
    def __init__ (self,name):
        self.name=name

class Dog(Animal):                      #child class
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def speak(self):
        return "woo!!!"

class Cat(Animal):
    def speak(self):
        return "meow!!!"

animal1=Animal("Sample")
animal2=Dog("Buddy",10)
animal3=Cat("Levi")

print(animal1.name)
print(f"name :{animal2.name},\n speaks :{animal2.speak()},\n age :{animal2.age}")
print(f"name :{animal3.name},\nspeaks {animal3.speak()}")
'''



#BANK ACCOUNT
class Bankaccount:
    def __init__(self,account_number,date_of_opening,balance,customer_name):
        self.account_number=account_number 
        self.date_of_opening=date_of_opening
        self.balance=balance
        self.customer=customer_name
        
    def deposits(self):
        deposit=int(input("Enter your deposit : "))
        self.balance+=deposit
        print(f"{self.balance } deposited successfully")

    def withdraws(self):
        withdraw=int(input("Enter your withdrawal : "))
        if self.balance<withdraw:
            print("insufficient balance !")
        else:
            self.balance-=withdraw
            print(f"{self.balance} withdrawn successfully")

    def check_balance(self):
        print(self.balance)

    def print_customer_details(self):
        print(f"Account number:{self.account_number},\nopening date:{self.date_of_opening},\nbalance:{self.balance},\ncustomer name :{self.customer}")

accnt_1=Bankaccount(123,'01-07-2007',500,'tony')

accnt_1.print_customer_details()

accnt_1.withdraws()

accnt_1.deposits()

accnt_1.check_balance()



"""
get from user the a/c no,opn date,bal,c_name

def __init__(self,account_number,date_of_opening,balance,customer_name):
        self.account_number=account_number 
        self.date_of_opening=date_of_opening
        self.balance=balance
        self.customer=customer_name



account_number=int(input("enter your account :"))
date_of_opening = input("Enter the date :"))
balance=int(input("enter your balance :")
customer_name=input("enter your name :")

acc1=bankaccount(account_number,date_of_opening,balance,customer_name)

acc1.print_customer_deatils()
"""











