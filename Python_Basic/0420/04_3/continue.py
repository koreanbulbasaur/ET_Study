# 변수를 선언
numbers = [5, 21, 6, 34, 75, 0]

# 반복을 돌림
for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어감
    if number < 10:
        continue
    # 출력
    print(number)