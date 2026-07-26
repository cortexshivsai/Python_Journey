import random

numbers = [10, 20, 30, 40, 50, 80, 100, 75]

print("Random Integer:", random.randint(10, 120))
print("Random Float:", random.random())
print("Random Choice:", random.choice(numbers))

random.shuffle(numbers)
print("Shuffled List:", numbers)