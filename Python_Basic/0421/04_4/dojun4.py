a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
b = []

for value in a:
    if type(value) == list:
        for v in value:
            b.append(v)
    else:
        b.append(value)
    
print(f'{a}를 평탄화하면')
print(f'{b}입니다')