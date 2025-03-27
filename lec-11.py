dic={"name":"amna"}
dic=dict({"name":"amna"})
dic=set({"name","amana"})
print(type(dic),dic)

#dic=list(["name","amana"])
#print(type(dic),dic)

dic=dict({"name":"amna","age":"20"})
#print(type(dic),dic,len(dic))

print(dic.get("name"))#method 1
print(dic["name"])#ethod 2

dic["name"]="bushara" #diretly updated
dic["color"]="fade"
dic.update({"color":"white","alpha":"1.09"})
#dic.pop("alpha") #last sy delete krta hy baqi sb main value pas nai krty laikin dic main key mention krna pry ga
dic.popitem()#to delete last item ;alpha ko delete kry ga
print(dic.keys())
print(dic.values())
print(dic.items()) #values ko separate separate kr k deta hy
print(dic)

