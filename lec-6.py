#lists
ls=["lahore","faisalabad","jarawala"]
print(type(ls),ls)
ls=[]
print(type(ls),ls)
ls=list(("lahore","faisalabad","jarawala")) #constructor  method
ls=["lahore","faisalabad","jarawala"]
print(ls[2:])

ls[1:2]=["multan"]
print(ls)
ls[1]=["multan"]
print(ls)
ls[0:1]=["karachi"]
ls[2:]=["multan"]

ls=["lahore","faisalabad","jarawala"]
ls.append(["peshawar"])
ls.insert(1,"peshawer")
ls.pop(0)#to remove specific index
ls.remove("faisalabad")#to remve wewill write the name of string
#del ls  #the list will be deleted
ls.clear()#it  will clear the list means values willbe deleted

ls=["apple","banana","mango"]
print(ls)
for x in ls:
    print(x)
