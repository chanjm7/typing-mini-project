import string
import random
import sqlite3
import datetime
import time


#데이터 베이스생성
conn = sqlite3.connect('/home/chanjmw35/Documents/dev/typing-mini-project/typing_game_data.db', isolation_level=None)
#데이터베이스 커서생성
c = conn.cursor()
#테이블 생성 
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, correct_conut text, wrong_count text, time_taken text, regdate text)")
#게임 정보
game_round = 1
correct_count = 0
wrong_count = 0

#현재시간
now = datetime.datetime.now()
nowDatetime = now.strftime('%y-%m-%d %H:%M:%S')
start_time = time.time()
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
print('걸린시간: {}초'.format(round(time.time() - start_time, 2)))
print('맞은개수: {}'.format(correct_count))
print('틀린개수: {}'.format(wrong_count))
