# 날짜/시간과 관련된 기능을 가져옴
import datetime

# 현재 날짜/시간을 구함
now = datetime.datetime.now()

# 출력합니다.
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))