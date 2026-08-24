a=int(input("Enter marks of Physics:"))
b=int(input("Enter marks of Chemistry:"))
c=int(input("Enter marks of Maths:"))

total=a+b+c
percentage=(100*total)/300

if(percentage>=40 and a>=33 and b>=33 and c>=33):
    print("You are passed with:",percentage)
else:
    print("You are failed:",percentage)    



