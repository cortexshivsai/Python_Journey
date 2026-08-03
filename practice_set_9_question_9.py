with open("shiv22.txt") as f:
    content=f.read()
with open("shiv223.txt") as f:
    content2=f.read()  

if( content==content2 ) :
    print("Yes these files are identical...")
else:
    print("NO these files are not identical!")          