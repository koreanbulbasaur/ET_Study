# 랜덤한 숫자를 만듦
import random

# 간단한 한글 리스트를 만듭니다.
hanguls = list('가나다라마바사아자차카타파하')

# 파일을 쓰기 모드
with open(r'C:\Projects\0424\05_3\with.txt', 'w', encoding='UTF-8') as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write(f"{name}, {weight}, {height}\n")
