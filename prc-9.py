""" tup=("gujranwala","faisalabad","lahore")
ls=list((tup))
print(ls)
list=[]
for x in ls:
      ls=x[0:1].upper()+x[1:-1].lower()+x[-1:].upper()
      list.append(ls)
print(list)
tup=tuple((list))
print(tup) """
 ######################################
""" temp=()
tup1=("faisalabad","jaranwala","lahore")
tup2=(1,2,3,4,5)

#tup3=tup2+tup1
temp=tup2
tup2=tup1
tup1=temp
tup3=tup2+tup1

print(tup3)

 """
#####################################
""" tup1=("faisalabad","jaranwala","lahore")
tup2=(1,2,3,4,5)

tup3=tup2+tup1
print(tup3)
tup3=tup3[5:]+tup3[:5]
print(tup3)
 """
tup1=("faisalabad","jaranwala","lahore")
tup2=(1,2,3,4,5)

tup3=tup2+tup1
ls=list((tup3))
rev=[]
for x in ls:
      #ls=x[0:1].upper()+x[1:-1].lower()+x[-1:].upper()
      # 
 rev.insert(0,x)
print(rev)

 
