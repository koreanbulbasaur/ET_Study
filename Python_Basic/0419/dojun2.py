width = input('밑변의 길이를 입력해주세요: ')
heigh = input('높이의 길이를 입력해주세요: ')

a = float(width)
b = float(heigh)

c = (a ** 2 +  b ** 2) ** (1/2)
print(f'= 빗변의 길이는 {c}입니다.')