import string
import random


round = 1
correct_count = 0
wrong_count = 0
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
        correct_count += 1
    else:
        print('오타ㅠㅠ')
        wrong_count += 1
    round += 1
print('------게임끝------')
print('맞은개수: {}'.format(correct_count))
print('틀린개수: {}'.format(wrong_count))
