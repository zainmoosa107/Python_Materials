
#DICTIONARY
#access
'''
person= {
    "Name":"zain",
    "Age":22
    }
print(person)

a=person.get ("Name")
print (a)

#Update
person["Name"]="Moosa"
print(person)

#Add
person["Place"]="Clt"
print(person)

#Remove
person.pop("Age")
print(person)
'''

students_marks={
    "anand" :92,
    "akhil" :84,
    "bension" :74,
    "cenoy" :64,
    "hafeed" :55,
    "jithin" :42,
    "nithin" :28
    }
students =["anand","akhil","bension","cenoy","hafeed","jithin","nithin"]
marks=['A+','A','B+','B','C','D','F']
#zip()
mark_sheet =dict(zip(students,marks))
print(mark_sheet)


#String Functions
#Alnum
name="Zain123"
print(name.isalnum())

#capitalize
name="zain"
print(name.capitalize())

#Upper()
print(name.upper())

#Lower()
name= "ZAin"
print(name.lower())

#Swapcase()
text="Good Morning"
print(text.swapcase())

#count()
print(text.count(""))

#Find()
print(text.find("M"))


#split and join
#----------------------
x="good morning"
print(x.split())


x="good$morning"
y=(x.split("$"))
print(y)
y.append('six')
print(y)

x="$".join(y)
print(x)



z="Good$morning"
i=z.split('$')
z='\n'.join(i)
print(i)
