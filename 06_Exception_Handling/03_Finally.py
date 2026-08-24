try:
    a=int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)
finally:
    print(f"The number is {a}")
    print("Thank You")           