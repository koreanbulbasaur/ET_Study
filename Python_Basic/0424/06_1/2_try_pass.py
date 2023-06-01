list_input_a = ["52", "223", "34", "spy", "104"]

# 반복을 적용
list_number = []
for item in list_input_a:
    # 숫자로 변환해서 리스트에 추가
    try:
        # 예외가 발생하면 알아서 다음으로 진행은 안 되겠지?
        float(item)

        # 예외 없이 통과했으면 list_number 리스트에 넣어줘!
        list_number.append(item)
    except:
        pass

# 출력
print(f"{list_input_a} 내부에 있는 숫자는")
print(f"{list_number}입니다.")
