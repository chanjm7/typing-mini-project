import string
import random
import sqlite3
import datetime
import time


now = datetime.datetime.now()
nowDatetime = now.strftime('%y-%m-%d %H:%M:%S')
print(nowDatetime)
game_round = 1
correct_count = 0
wrong_count = 0
start_time = time.time()
print(type(start_time))

while game_round != 5+1:
    length = random.randint(3,7)
    answer = ""
    for i in range(length):
        answer += random.choice(string.ascii_lowercase)
    print('------{}라운드------'.format(game_round))
    print(answer)
    user_input = input('입력: ')
    if user_input == answer:
        print('굿굿굿')
        correct_count += 1
    else:
        print('오타ㅠㅠ')
        wrong_count += 1
    game_round += 1
print('------게임끝------')
print('걸린시간: {}'.format(round(time.time() - start_time, 2)))
print('맞은개수: {}'.format(correct_count))
print('틀린개수: {}'.format(wrong_count))
