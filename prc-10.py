""" st={"item1","item2"}
(st1,st2)=st
#st.replace("item1","ashraf")
print(st1)
print(st2)
st1="ashraf"
st2="abc"
st3=st1 +" "+st2
print(st3) """

#####################################
""" ls1=["ashraf","ali","akram","subhan"]
tup=("asghar","ashraf","ali","inaam")
ls2=list((tup))
ls3=ls1+ls2
#print(ls3)
st1=set((ls3))
#print(st1)
st2=set((tup))
#print(st2)
st3=st1|st2
#st3=st1.intersection(st2)
print(st3)
st4=st1 & st2
print(st4)
st5=st1-st2
print(st5) """

#########################
tup=("ali","asghar","ashraf","akbar","aslam","arshad","ibrahim","waqas","inam","jawad")
(tup1,tup2,tup3,tup4,tup5,tup6,tup7,tup8,*tup9)=tup
#print(tup)
tup9.insert(0,"noman")
print(tup9)

ls=list((tup))
#print(ls)

ls.insert(0,"nova")
print(ls)
st=set((ls))
print(st)