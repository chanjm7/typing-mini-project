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
c.execute("CREATE TABLE IF NOT EXISTS users(name text, correct_count text, wrong_count text, time_taken text, regdate text)")
#게임 및 유저정보
game_round = 1
correct_count = 0
wrong_count = 0
user_name = input('저장할 이름을 정해주세요: ')

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
time_taken = round(time.time() - start_time, 2)
print('------게임끝------')
print('걸린시간: {}초'.format(time_taken))
print('맞은개수: {}'.format(correct_count))
print('틀린개수: {}'.format(wrong_count))

#user데이터 삽입
c.execute("INSERT INTO users(name, correct_count, wrong_count, time_taken, regdate) VALUES (?, ?, ?, ?, ?)", (user_name, correct_count, wrong_count, time_taken, nowDatetime))



