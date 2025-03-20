ls=["lahore","faisalabad","jarawala"]
#print(ls[0].capitalize(),ls[1].capitalize(),ls[2].capitalize())

""" ls.insert(0,"lahorE")
ls.insert(1,"FaisalabaD")
ls.insert(2,"JarawanalA")
print(ls) """

ls=["lahore","faisalabad","jarawala"]
lp=[]
for x in ls:
    p=x[0:1].lower() + x[1:2].upper() +x[2:-2].lower() + x[-2:-1].upper() +x[-1:].lower()
    lp.append(p)
print(lp) 

""" ls=["lahore","faisalabad","jarawala"]
lp=[]
for i in ls:
    #p=i[-1:0]
    #lp.insert(p)
    lp.insert(0,i)
    print(lp) """