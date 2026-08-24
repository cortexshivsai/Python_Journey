class emp:
    a=1

class coder(emp):
    b=2

class programmer(coder):
    c=3

o=emp()
print(o.a)

o=coder()
print(o.a,o.b)

o=programmer()
print(o.a,o.b,o.c)


