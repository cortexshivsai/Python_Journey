class emp:
    a=1
    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.name} {self.lname}"    
    
    @name.setter
    def name(self,value):
        self.fname=value.split()[0]
        self.lname=value.split()[1]


e=emp()
e.a=45

e.name="Shivsai Jagadale"
print(e.fname,e.lname)
e.show()