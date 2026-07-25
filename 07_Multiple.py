class emp:
    company="TATA"
    name="Shivsai"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class coder:
    language="Python"
    def lang(self):
        print(f"Your language is: {self.language}")   

class programmer(emp,coder):
    # company="TCS"
    def showLang(self):
        print(f"The name is {self.name} and he is good in {self.language} language")


a=emp()
b=programmer()
b.show()
b.lang()
b.showLang()              