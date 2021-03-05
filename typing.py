import string
import random

length = random.randint(3,7)
answer = ""
for i in range(length):
    answer += random.choice(string.ascii_lowercase)

print(answer)
user_input = input('입력: ')
if user_input == answer:
    print('굿굿굿')
else:
    print('오타ㅠㅠ')
