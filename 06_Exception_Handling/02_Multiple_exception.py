try:
    a=int(input("Enter a number: "))
    print(a)

except ValueError as v:
    print("Enter a valid number") 
    a=int(input("Enter a number: "))

except Exception as e:
    print(f"The number is {a}")


print(f"The number is {a}")
print("Thank You")