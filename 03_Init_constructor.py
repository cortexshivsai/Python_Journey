class emp:
    language="Python"
    salary=1200000

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object..")

    def getinfo(self):
        print(f"The language is {self.language} and The salary is {self.salary}") 


@staticmethod
def greet():
    print("Good Night..")   

shiv=emp("Shivsai",1200000,"Jacascript")
print(shiv.name,shiv.salary,shiv.language)     