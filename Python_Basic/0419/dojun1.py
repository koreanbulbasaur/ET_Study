sr = input('구의 반지름을 입력해주세요: ')
int_sr = int(sr)
pi = 3.141592

sv = (4 / 3) * pi * (int_sr ** 3)
print("= 구의 부피는 {}".format(sv))

ss = 4 * pi * int_sr ** 2
print(f"= 구의 겉넓이는 {ss}입니다.")