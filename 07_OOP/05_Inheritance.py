class emp:
    company="TATA"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
class programmer(emp):
    # company="TCS"
    def showLang(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a=emp()
b=programmer()
print(a.company,b.company)                