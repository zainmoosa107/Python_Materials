'''
Dictionary{}
---------------
'''

phn_number={
    "akshay" :987,
    "sarath": 123,
    "akhil": 456
    }
print(phn_number)
print(phn_number["akshay"])
phn_number["akshay"]=888
print(phn_number)

#functions
#get---- to get the value 
print(phn_number.get("sarath"))

#update() --- to change the value
phn_number.update({"sarath":999})
print(phn_number)

#to add new item or key

phn_number["den"]=555
print(phn_number)

phn_number.update({"ben":755})
print(phn_number)

#del,clear()
del phn_number["sarath"]
print(phn_number)

phn_number.clear()
print(phn_number)


#pop(),popitem()

roll_number={
    1:"anand",
    2:"bension",
    3:"hafeed"
    }
roll_number.pop(2)
print(roll_number)

roll_number.popitem()
print(roll_number)


#keys
roll_number={
    1:"anand",
    2:"bension",
    3:"hafeed"
    }
print(roll_number.keys())

#values()
print(roll_number.values())

#items()
print(roll_number.items())
#----------------------------------

print(roll_number)
for i in roll_number:
#  print(i)      # key
    print(roll_number[i]) # values
for i in roll_number.keys():
    print(i)
for i in roll_number.values():
    print(i)
for i in roll_number.items():
    print(i)

#-------------------------------------------------------

#merging
#------zip()- merging two list to dictionary or combining keys and values
'''
subject=[]
mark=[]
for i in range(5):
    subject=input( "Enter your subject name :")
    mar=int(input("Enter your mark : "))
    mark.append(mar)
print(subject)
print(mark)

subject=["physics","maths","biology","chemistry"]
mark =[35,45,50,33,15]
marksheet=dict(zip(subject,mark))
print(marksheet)
'''

#{'anand' :A+ , 'akhil :'A','bension':'B+','cenoy':'B','hafeed':'C','jithin':'D','nithin:'F'}
marksheet={
    "anand":92,
    "akhil":84,
    "bension":74,
    "cenoy":64,
    "hafeed":55,
    "jithin":42,
    "nithin":28
    }
names=['anand','akhil','bension','cenoy','hafeed','jithin','nithin']
grade=['A+','A','B+','B','C','D','E','F']
grademark=dict(zip(names,grade))
print(grademark)
