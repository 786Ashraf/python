tup=("semester","annual","master")
#print(tup([0]))
#tup1,tup2,tup3)=tup#destructurized the object
#print(tup1)

(tup1,tup2,*tup3)=tup
print(tup2)

###############################
#set
st={"hellow","world"}
print(st)

st=set(("hellow","world","!"))
st.add("philospher")
#st.add("philospher","menu")#it wil creat error
st=set(("hellow","world"))
st2=set(("ab","cd"))     
st.update(st2)
st.pop()
print(st)
st=set(("hellow","world","!"))
ls=list(st)
print(ls)
st=set(("hellow","world","!",True,0,1))
print(st)
st=set((False,True,"hellow","world","!",0,1))
print(st)

st={"hellow","world","!"}
st.remove("hellow")
st.discard("hellow")#yi method already removed value ki wajah sy error jo aty hy ab errror nai ay ga
st.clear()
del st
print(st)

del st[0]# it will creat error
print(st)

st1={"hellow","world","!"}
st2={"menu","food","world"}
st3=st1+st2#error

st3=st1|st2
st3=st1.union(st2)

st3=st1.intersection(st2)
st3=st1 & st2
print(st3)

st3=st1.difference(st2)  #common values will be removed
#  or
st3=st1-st2
print(st3)
