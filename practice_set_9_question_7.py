with open("new.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("Python" in line):

        print(f"Python is present in the content at line no:{lineno}!")    
        break
    lineno+=1
else:
    print("Python is not present in the content!")    