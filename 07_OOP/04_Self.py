class emp:
    name=input("Enter your name:")
    company="Microsoft"  #Class attribute

    def getInfo(self):
        print(f"Name is:{self.name} and company is:{self.company}")
s1=emp()
print(s1.name,s1.company)
s1.company="Google"  #instance attrbute
s1.getInfo()
