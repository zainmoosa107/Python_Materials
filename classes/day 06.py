'''
#Data structures - handle more than one values
# LIST , TUPLE , SET , DICTIONARY
#------------------------
# LIST
# *ordered - position
# Duplicates elements are accepted
# all datatypes are acceptable

Mark = [30,25,35,45,48]
     #  0 , 1,2, 3 , 4  Left to ryt starting from 0 to infinity- indexing
     #  -5,-4,-3,-2,-1  Ryt to left starting from -1 to infinity - negative indexing
print(Mark)


#items,elements


#indexing

print(Mark[2])
print(Mark[-1])
#------------------------------------------
# changing values in list

sample_list = [1,2,"Hello",45.50,True,"Codeme"]

print(sample_list)
print(sample_list[3])

# To change the value in list
sample_list[3] = "vritz"
print(sample_list)


print(len(sample_list))
#------------------------------------------------------------
#Slicing [start :end:steps]
data= [10,20,30,40,50,60]

print(data[1:4])         #[20, 30, 40]
print(data[1:])          #[20, 30, 40, 50, 60]
print(data [1:])         #[20, 30, 40, 50, 60]
print(data[:5])          #[10, 20, 30, 40, 50]
print(data[-4:-2])       #[30, 40]
print(data[-2 :-4])      #[]
print(data[:-2])         #[10, 20, 30, 40]
print(data [-5:])        #[20, 30, 40, 50, 60]


#steps
print(data[0:5:2])       #[10, 30, 50]
print(data[::3])        #[10, 40]
print(data[::-1])        #[60, 50, 40, 30, 20, 10]
print(data[-2:-5:-1])   #[50, 40, 30]

print(data[1:3:4])      #[20]


#in steps [::] 1,2,3,4,5,6 using [::-1] make 6,5,4,3,2,1

a=[1,2,3,4,5,6]

print(a[2:4])

'''
#-----------------------------------------------
#List methods()
 #append () - to add the value in list

mark = [ 30,25,35,45,30]
mark.append(55)
print("list.append(item)",mark)
print(mark)
mark1=[]
mark1.append(9)
print(mark1)

#insert()- inserting the value in position

mark2 =[11,22,33,44,55]
mark2.insert(1,17)    # insert(position ,value)
print(mark2)

#remove - remove the item
mark3 = [11,17,22,33,44,55]
mark3.remove(17)
print(mark3)

#pop - to remove the item using to the index position
#    - without giving any index position it will remove the last value

mark4 = [44,55,66,77,88]
mark4.pop(3)
print(mark4)

#sort - to get the values ascending and decending order



