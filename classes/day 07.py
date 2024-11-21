mark=[10,20,15,25,20,30,45]
mark.sort()
print (mark)

mark=[10,20,15,25,20,30,45]
mark.sort(reverse = True)
print(mark)


#------------------
# joining list

#1 - +operator - not fixed can make back to 2 list

a=[1,2,3]
b=[4,5,6]
print(a+b)

#2 - extend - fix the join 

a =[1,2,3]
b=[4,5,6]
b.extend(a)
print (b)



#reverse
c=[1,2,3,4,5,6,7,8]
c.reverse()
print(c)
