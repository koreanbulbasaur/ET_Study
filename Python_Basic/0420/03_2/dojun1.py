import datetime
now = datetime.datetime.now()
hour = now.hour
orange = input("입력 : ")

if orange in '안녕':
    print('안녕하세요.')
elif orange == '지금 몇 시야?':
    print(f'지금은 {hour}시입니다.')
elif orange == '지금 몇 시예요?':
    print(f'지금은 {hour}시입니다.')   
else:
    print(orange)
