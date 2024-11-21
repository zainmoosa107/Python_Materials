row =5
for n in range(row):
    for space in range(4-n):  #if we receiving from user (row -1-n)
        print(" ",end=" ")
    for star in range(n+1):
        print("*",end=" ")
    print()
'''
----------------------------------------------------
# TUPLE()
 * Ordered
 * Indexing
 * Slicing
 * Duplicate items allowed
 * immutable - cannot change,edit,insert
'''
x=(1,5,3,2,4,2)
print(x[0])
print(x[2])
print(x[-3])
print(x[1:3])
print(x[-5:-2])
print(x[::-1])
print(type(x))

# to edit the tuple values
x=(1,5,3,2,4,2)
y=list(x)
print(y)
y.append(8)
x=tuple(y)
print(x)

'''
-----------------------------------------------
SET
 *Data structure
 *{}
 *Unordered
 *Duplicate items are not allowed
 *Unique - item
 *No indexing
'''
sample_set={5,3,"33",True}
sample_set.add(99)
print(sample_set)


#sample.remove("33")
#print(sample_set)  # remove and show error

sample_set.discard("33")
print(sample_set)  # it will print the set wheather the item is in list or not

sample_set.pop()
print(sample_set)


setA={"red","blue","green"}
setB={"blue","yellow","orange"}
#print(setA)
#print(setB)

'''print(setA.union(setB))# union combine two set
setA.update(setB) # update -updates the set 
print(setA)

print(setA.difference(setB))
setA.difference_update(setB)
print(setA)
'''
print(setA.symmetric_difference(setB))
setA.symmetric_difference_update(setB)
print(setA)

a={1,2,3,4,5}
b={4,5}
c={7,8,9}

print(a.issuperset(b))#true
print(b.issubset(a))
print(c.isdisjoint(b))

print(b.issuperset(a)) #false
print(a.issubset(b))



row=5
for i in range(row) :
    for spaace in(2-



