#multi line string
#b="hellow world" 
 #    new country""
 #    "
b="""hellow world are you
what """
print (b)
a=24
b=43
print(str(a)+str(b))
# format method(to solve type casting issues)
#format in strings and integers
marks=45
total="your total marks is 100 and you got {}"
obt=total.format(marks)
print(obt)
age=23
total=100
obt=90
#res="your ageis {}and toatal marks {} andobtain marks{}"
#tot=res.format(age,total,obt)
#print (tot)
#if parameters agy pichy hun
res="your ageis {0}and toatal marks {2} andobtain marks{1}"
tot=res.format(age,obt,total)
print(tot)

##################
# string slicing
a="hellow world"
print(a[0:2])
print(a[-3:-1])
#jb last index ko includekrna ho to(shuru wala na likho to shuru sy include kry ga agr last wala nai likhato end tk sara shamil ho ga)
print(a[0:])
print(a[:5])
# split in string
a="hellow ai class"
b=a.split(" ")
print(a,b)
#is sy list generate ho gi split ho k
#upper case and lower case in string
st="hellow world"
up=st.upper()
low=st.lower()
print(up,low)
#sentenc ka pehla lafz capital kry ga
print(st.capitalize())
#multiwordska pahla lafz capital
print(st.title())
a="hellow"
b="world"
print(a.capitalize() + " " + b.capitalize())
p="jarawalan faisalabad lahore"

j="Jarawalan"
f="Faisalabad"
l="Lahore"
res="jarawalan{}faisalabad{}lahore"
tot=res.format(j,f,l)
#replace method
a="hellow"
b=a.replace("h","H")
print(b)