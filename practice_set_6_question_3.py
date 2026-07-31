a="Make a lot of maney"
b="Buy now"
c="Subscribe now"
d="Click this"

msg=input("Enter your messege:")

if(a in msg or b in msg or c in msg or d in msg):
    print("This comment is a spam!")
else:
    print("This comment is not a spam.")     