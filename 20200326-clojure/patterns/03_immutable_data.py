"""
An immutable object is an object whose state 
cannot be modified after it is created.
"""
import random

# Mutable Data
x = [10, 20, 30, 40]
x.append(50)

# Immutable Data
x = [10, 20, 30, 40]
x = x + [50]

# Mutable Data
x = [10, 20, 30, 40]
random.shuffle(x)
print(x)

# Immutable Data
x = [10, 20, 30, 40]
print(random.sample(x, k=len(x)))
print(x)
