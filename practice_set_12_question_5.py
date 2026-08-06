n=int(input("Enter any number:"))
table=[n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(str(table)+"\n")
