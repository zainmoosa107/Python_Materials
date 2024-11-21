#OOPS
#class -is a blue print of objects
#object- structural data or member of clss

# class syntax - class SampleMade *starts with capital letter *cannot use space


class Sample:
    x=10

    def fun(self):        # self built in for class
        print("Hello")    # here,def is called as method, cause inside class
        
s1=Sample()
s2=Sample()

print(s1.x)        

print(s2.x)

s1.fun()


class Sample1:
    x=10

    def fun(self):       
        x="Hi"
        print(f"Value of x is {x}")   
        
s1=Sample1()
s2=Sample1()
s1.fun()


class Sample2:
    x=10                      #global scope

    def fun(self):        
        x="Hi"
        print(self.x)         #calling global object attribute
        
s1=Sample2()
s2=Sample2()
s1.fun()

#modifing the attribute
class Sample3:
    x=10
    
s1=Sample3()
s2=Sample3()
s1.x="python"  #modifing

print(s1.x) 
print(s2.x)    # accessing  object attribute




class Student:
    def details(self,name,age):
        self.n=name
        self.a=age
st1=Student()
st2=Student()

st1.details("james",21)

print(st1.n)
print(st1.a)


class Student1:
    def details(self,name,age):
        self.n=name
        self.a=age
    def display(self):
        print(f"name is '{self.n}'")
        print(f"age is '{self.a}'")
st3=Student1()
st4=Student1()

st3.details("james",21)

st3.display()



