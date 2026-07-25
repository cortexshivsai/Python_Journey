class emp:
    name=input("Enter your name:")
    company="Microsoft"  #Class attribute
s1=emp()
print(s1.name,s1.company)
s1.company="Google"  #instance attrbute
print(s1.name,s1.company)

#instance attribute take preference over class attributes during assignment and retrieval.