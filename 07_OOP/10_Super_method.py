class emp:
    def __init__(self):
        print("Constructor of employee")
    a=1    

class coder(emp):
    language="Python"
    def __init__(self):
        print("Constructor of Coder..")  
    b=2     

class programmer(coder):
  
    def __init__(self):
        super().__init__()
        print("Constructor of programmer..")
    c=3    


# a=emp()
a=programmer()
print(a.a,a.b,a.c)            