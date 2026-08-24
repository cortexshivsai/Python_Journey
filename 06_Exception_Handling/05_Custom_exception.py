# Creating a custom exception
class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("You are eligible to vote.")

except InvalidAgeError as e:
    print("Custom Exception:", e)