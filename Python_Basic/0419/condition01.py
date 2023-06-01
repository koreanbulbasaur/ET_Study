# 입력을 받음
n = input("정수 입력> ")

# 마지막 자리 숫자를 추출
last_character = n[-1]

# 숫자로 변환하기
last_n = int(last_character)

# 짝수 확인
if last_n == 0 \
    or last_n == 2 \
    or last_n == 4 \
    or last_n == 6 \
    or last_n == 8:
        print("짝수입니다.")
        
# 홀수 확인
if last_n == 1 \
    or last_n == 3 \
    or last_n == 5 \
    or last_n == 7 \
    or last_n == 9:
        print("홀수입니다.")