# 리스트를 선언하고 뒤집음
list_a = [1, 2, 3, 4, 6]
list_reversed = reversed(list_a)

# 출력
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 6]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 6])):", list(list_reversed))
print("")

# 반복문 적용
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 6]):")
for i in reversed(list_a):
    print("-", i)