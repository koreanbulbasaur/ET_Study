# try except 구문으로 예외를 처리
try:
    # 숫자로 변환
    n_input = int(input("정수 입력> "))

    print("원의 반지름 :", n_input)
    print("원의 둘레 :", 2 * 3.14 * n_input)
    print("원의 넓이 :", 3.14 * n_input * n_input)
except:
    print("정수로 입력하지 않음")
else:
    print("예외가 발생하지 않음")
finally:
    print("일단 프로그램이 어떻게든 끝났음")
