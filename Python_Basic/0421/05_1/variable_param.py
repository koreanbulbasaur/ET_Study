def print_n_times(n, *values):
    # n 번 반복함
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()

# 함수를 호출
print_n_times(3, "안녕하세요", "즐거운", "불금")