# 변수 선언
i = 0

# 무한 반복함
while True:
    # 몇 번째 반복인지 출력함
    print(f"{i}번째 반복문")
    i = i + 1
    # 반복을 종료
    input_text = input("> 종료하시겠습니까?(y/n): ")
    if input_text in ["y", 'Y']:
        print("반복문을 종료함")
        break