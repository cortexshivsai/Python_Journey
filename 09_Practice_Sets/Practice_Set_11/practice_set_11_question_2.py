class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod 
    def bark():
        print("BOW....BOW...!")

a=dog()
a.bark()        
    
