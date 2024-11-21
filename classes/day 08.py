"""
x=[1,2,3,4]
for i in x:
    print(i)
for i in range(-1,17):
    print(i)
for i in range(1,17,5):     #range(strt,end,steps)
    print(i)
for i in range(0,len(x)):
    print(x[i])
colors=["red","black","blue","yellow","orange","green"]
traffic =["red","yellow","green"]
for i in colors:
        if(i in traffic):
            print(f"{i} in traffic)
        else:
            print(



mark=[]
for i in range(5):
    m=int(input("enter the marks: "))
    mark.append(m)
print(f"mark={mark}")

colors=["red","black","blue","yellow","orange","green","red","black","blue","yellow","orange","green"]
numbers=[1,2,3,4,5,6]

for i in colors:
    for j in numbers:
        print({i},{j})

for i in numbers:
    for j in colors:
        print({i},{j})

#1
numbers=[1,2,3,4,5]
square=[]
cube=[]
for i in numbers:
    c=i**2
    square.append(c)
print(f"squares={square}")
for k in numbers:
    t=k**3
    cube.append(t)
print(f"cubes={cube}")


#2
even=[]
odd=[]
for i in range(10):
    n=int(input("enter 10 numbers:"))
    if(n%2==0):
        even.append(n)
        print(f"even numbers={even}")
    else:
        odd.append(n)
        print(f"odd numbers={odd}")
"""
#3
x=[4,5,6,8]
y=[8,6,2,3]
z=[]
for i in x:    
    if(y.count(i)>0):
        z.append(i)
print(f"common numbers are :{z}")
            
    
