'''
#regular functions
#def greet():           in greet(x,y=10) here y=10 is default parameter
#   return "hello world"
#print(greet())        in here greet()- argument





#anonymous function (Lambda)
 #lambda function in  programming is a small anonymous functin defined with the
 #lambda keyword.It can have any numberof arguments but only have one expression.
 # The expression is evuated and returned
#lambda parameters : experession



greet = lambda :"hello world "
print(greet())


add= lambda x,y :x+y
print(add(5,4))



#functions of lambda

#map(function,iterable) :

number=[1,2,3,4,5]
square=list(map(lambda i:i**2,number))
print(square)


#filter(function,iterable) : items out of an iterable
numbers=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,numbers))
print(even)


char=['a','b','c','d','e','f']

vaw=list(filter(lambda x:x in "aeiou",char))
print(vaw)




#reduce
from functools import reduce

numbers=[1,2,3,4,5]
product=reduce(lambda x,y:x*y ,numbers)    
print(product)

#initialization : initially x takes the first element of the iterable and y takes the
                # second element
    #each time,x accumulate the result of the lambda function applied to x and y.




#---------------------------------------

#List comprehensions
numbers=[1,2,3,4,5]
#sqr=[]
#for i in numbers:
#    sqr.append(i**2)
#print(sqr)


sqr=[i**2 for i in numbers]
print(sqr)
'''



numbers=[1,2,3,4,5,6,7,8,9,10]

eve_double=[]
for i in numbers:
    if(i%2==0):
        eve_double.append(i*2)
print(eve_double)

eve_double=[i*2 for i in numbers if i%2==0]
print(eve_double)

names=['Alice','Bob','Charlie','David']
initials=[]
for i in names:
   initials.append(i[0])
print(initials)

initals=[i[0] for i in names]
print(initials)


words=['apple','banana','cherry','dates','blueberry','kiwi']
words_with_a=[]
for  i in words:
    if 'a' in i:
        words_with_a.append(i)
print(words_with_a)


word_with_a=[i for i in words if 'a' in i]
print(word_with_a)



numbers=[1,2,3,4,5]
squares_or_cubes=[]
for i in numbers:
    if i%2==0:
        squares_or_cubes.append(i**2)
    else:
        squares_or_cubes.append(i**3)
print(squares_or_cubes)

squares_or_cubes=[i**2 if i%2==0 else i**3 for i in numbers]
print(squares_or_cubes)

# when if else condition,,,
#       [exp(if) if condition else exp(else) for item in iterable]



#exception handling
#try
#except
#raise
#finally



