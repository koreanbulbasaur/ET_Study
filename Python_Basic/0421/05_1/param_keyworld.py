def print_n_times(*values, n=2):
    # n번 반복
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        print()

# 함수 호출
print_n_times("Oh!", "Hi!", n=5)