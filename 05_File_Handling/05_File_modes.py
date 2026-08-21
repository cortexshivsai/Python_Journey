# Write Mode (w)
# Creates a new file or overwrites an existing file.
file = open("sample.txt", "w")
file.write("Hello, Python!\n")
file.close()
print("Data written using 'w' mode.")


# Read Mode (r)
file = open("sample.txt", "r")
print("\nReading File:")
print(file.read())
file.close()


# Append Mode (a)
file = open("sample.txt", "a")
file.write("This line is appended.\n")
file.close()
print("\nData appended using 'a' mode.")


# Read Again
file = open("sample.txt", "r")
print(file.read())
file.close()


# Read and Write Mode (r+)
file = open("sample.txt", "r+")
print("\nUsing r+ mode:")
print(file.read())
file.close()