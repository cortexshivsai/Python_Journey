class emp:
    a=1
    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

e=emp()
e.a=45
e.show()