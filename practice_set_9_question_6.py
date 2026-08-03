with open("new.txt") as f:
    content=f.read()


if("Python" in content):
    print("Python is present in the content!")    
else:
    print("Python is not present in the content!")    