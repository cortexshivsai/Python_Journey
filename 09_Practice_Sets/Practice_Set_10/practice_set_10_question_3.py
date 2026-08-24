class demo:
    s=45

obj=demo()
print(obj.s)  #prints the class attribute because the instance attribute is not present  
obj.s=13 #instance attribute is set
print(obj.s)#prints the intsance attribute beacause the instance attribute is present.
# print(demo.obj)