ls=["karachi","jarawala","faisalabad"]
for x in range(len(ls)):
    print(ls[x],x)
   # print(ls[x],x+1)

i = 0
while i<len(ls):
   print(ls[i])
i=i+1

for x in range(10):
    print(x)
    
for x in range(1,10):
     print(x)

for x in range(1,10,2):
   print(x)
for x in range(2,10,2):
  print(x)

for x in range(10):
     print(x)

for x in range(0,21,2):
    print(x)

ls=[x for x in range(10)]
print(ls)

""" ls=["karachi","jarawala","faisalabad","kivi"]
ls2=[]
for x in ls:
  if "a" in x:
      ls2.append(x)
print(ls2) """

#list comprehension
ls=["karachi","jarawala","faisalabad","kivi"]
ls2=[x for x in ls if "a" in x]
print(ls2)

ls=["karachi","jarawala","faisalabad","kivi","test"]
ls2=[x for x in ls if "i" in x]
print(ls2)
ls=["karachi","jarawala","faisalabad","kivi"]
[print (x) for x in ls if "a" in x]

ls=["karachi","jarawala","faisalabad","kivi"]
ls2=[x for x in ls if x!= "karachi"]
print(ls2)

ls=["karachi","jarawala","faisalabad","kivi"]
ls2=[x.capitalize() for x in ls ]
print(ls2)

ls2=[x[0].upper() + x[1:-1].lower()+x[-1].upper() for x in ls]

ls2=[x[0]]


