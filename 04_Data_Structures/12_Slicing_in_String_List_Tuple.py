# List Slicing
numbers = [10, 20, 30, 40, 50, 60]

print("Original List:", numbers)

print("First 3:", numbers[:3])# First 3 elements

print("Last 3:", numbers[-3:])# Last 3 elements

print("Index 2 to 4:", numbers[2:5])# Elements from index 2 to 4

print("Step 2:", numbers[::2])# Every second element

print("Reversed:", numbers[::-1])# Reverse the list


print("\n")

# String Slicing
text = "Python"

print("Original String:", text)

print("First 3 letters:", text[:3])
print("Last 3 letters:", text[-3:])
print("Middle letters:", text[1:5])
print("Every second letter:", text[::2])
print("Reverse:", text[::-1])


print("\n")

# Tuple Slicing
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Original Tuple:", fruits)

print("First 2:", fruits[:2])
print("Last 2:", fruits[-2:])
print("Middle:", fruits[1:4])
print("Reverse:", fruits[::-1])