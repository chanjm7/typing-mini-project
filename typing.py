import string
import random

length = random.randint(3,7)
result = ""
for i in range(length):
    result += random.choice(string.ascii_lowercase)
print(result)