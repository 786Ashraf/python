""" j="Jarawalan"
f="Faisalabad"
l="Lahore"
res="{}{}{}"
tot=res.format(j,f,l)
print(tot) """
#################
# a="jaranwala faisalabad lahore"
#print(a[0:1].upper()+a[1:9],a[10:11].upper()+a[11:20],a[21:22].upper()+a[22:])
#print(a[0:1]+a[1:9].upper(),a[10:11]+a[11:20].upper(),a[21:22]+a[22:].upper())
###############
""" a="hellow ai class"
b=a.split(" ")
print(b) 
a="jaranwala"
b=a.replace("j","J")
a="faisalabad"
c=a.replace("f","F")
a="lahore"
d=a.replace("l","L")
print(b,c,d) """
####################
a="faisalabad lahore jarawalan"
print(a.replace("f","F").replace("l","L").replace("j","J"))
#print(a.replace("f" "F" "l" "L" "j" "J"))
a="Faisalabad Lahore Jarawalan Karachi"
print(a.replace("F","f").replace("L","l").replace("J","j").replace("K","k"))
