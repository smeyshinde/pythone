#add
a=input("enter the 1 number")
b=input("enter the 2 number")
add=int(a)+int(b)
print("add : ",add)

#sub
a=input("enter the 1 number")
b=input("enter the 2 number")
sub=int(a)-int(b)
print("sub : ",sub)

#mul
a=input("enter the 1 number")
b=input("enter the 2 number")
mul=int(a)*int(b)
print("mul : ",mul)

#dived
a=input("enter the 1 number")
b=input("enter the 2 number")
div=int(a)/int(b)
print("div : ",div)

#datatype
a=10
b=10.0
c='amey'
d=8.0j
print(" a is type of ",type(a))
print(" b is type of ",type(b))
print(" c is type of ",type(c))
print(" d is type of ",type(d))

#list
import numpy as np
l1=[1,2,3]
l2=[4,5,6]
print(" list is type of ",l1,type(l1))
print(" list is type of ",l2,type(l2))
na1=np.array(l1)
na2=np.array(l2)
na3=na1+na2
print("add of list is : ",na3)
na4=na1.insert(4,4)
na5=na2.insert(4,4)
print("new list is :",na4)
print("new list is :",na5)

#tuple
a=("red","green","white")
print("tuple is :",a,type(a))

#length of the list
l=[1,2,3,4,5,6,7,8,9]
s={1,2,3,4,5,6,7,8,9}
t=(1,2,3,4,5,6,7,8,9)
print(l)
print(" length of the list :",len(l))
print(s)
print(" length of the set :",len(s))
print(t)
print(" length of the tuple :",len(t))

#print any form the list
l=[1,2,3,4,5,6,7,8,9]
print(l)
print(l[1 :4])
l=[1,2,3,4,5,6,7,8,9]
print(l)
print("large number in the list : ".max(l))
print("samll number in the list : ".max(l))
