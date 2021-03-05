import string
import random


round = 1
while round != 5+1:
    length = random.randint(3,7)
    answer = ""
    for i in range(length):
        answer += random.choice(string.ascii_lowercase)
    print('------{}라운드------'.format(round))
    print(answer)
    user_input = input('입력: ')
    if user_input == answer:
        print('굿굿굿')
    else:
        print('오타ㅠㅠ')
    
    round += 1
