with open(r'C:\Projects\0424\05_3\info.txt', "r", encoding='UTF-8') as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")

        # 데이터가 문제없는지 확인합니다.: 문제가 있으면 지나감
        if (not name) or (not weight) or (not height):
            continue

        # 결과를 계산함
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        # 출력함
        print('\n'.join([
            f"이름 : {name}",
            f"몸무게 : {weight}",
            f"키 : {height}",
            f"BMI : {bmi}",
            f"결과 : {result}"
        ]))
        print('-' * 50)
