dic1={"person1":{"name":"aman","age":30}}
#dic1.get("name")
#print(dic1)
dic1["person1"].pop("age")
#print(dic1)
dic1["person1"].update({"height":"5.6"})
#print(dic1)
dic1["person1"]["name"]="ashraf"
#print(dic1)
dic1["person1"]="ali"
print(dic1)

dic2={}

dic2.update({"name":"ashraf","height":"6"})
print(dic2)