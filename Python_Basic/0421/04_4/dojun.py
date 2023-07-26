lst = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3]
counter = {}

for number in lst:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1
    
print(lst , "에서")
print(f'사용된 숫자의 종류는 {len(counter)}개입니다.')
print("참고 :",counter)