# Functons
#kivi libraries is uded to make android application(apk(application programming kit))
# tkinter to make desktop applcation(.execution)

""" def s():
    print("ashraf")
s()  """
##############
#empty function (ap k0 hy laikin kahin zaroorat pr skty hy )
def fun():
    pass
fun()
#argument
def func(name="akash"):
    print("hellow world"+name)
func("akash")
#parameter
def func(name):
    print("hellow world"+name)
func("akash")

def func(name,age):
    print("hellow world" +name + str(age))
func("ashraf",24)   
##########################
#arbitrary arguments
def func(name,*age):
    #print(name +" "+ str(age[0]))#0 is index 
    print(name +" "+ str(age[1]))#1 is index 
func("ashraf",24,25)   
###################
#arbitrary keywords arguments
def func(**krgs):
    print(krgs["name"]+ str(krgs["age"]))#name is key
func(name="ashraf",age=34)   
#########################
#exception handling
x=23

try:
    print(y)
except:
    print("error:y is not defind")
finally:
    print("this is always executed")    

    ######################
    #anonymous function
    x=lambda a: a*5
    print(x(5))

x=lambda a,b: a**5
print(x(5,2))

x=lambda a,b,c: a*b/c
print(x(5,2,2))
