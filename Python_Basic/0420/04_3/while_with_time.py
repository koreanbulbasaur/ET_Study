# 시간과 관련된 기능을 가져옴
import time

# 변수를 선언함
n = 0

# 5초 동안 반복함
target_tick = time.time() + 5
while time.time() < target_tick:
    n += 1
    
# 출력
print("5초 동안 {}번 반복함".format(n))