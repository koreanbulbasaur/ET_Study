# 딕셔너리를 선언
dictionary = {
    "name" : '무생체',
    "type" : '당절임'
}

# 요소 제거 전에 내용을 출력
print("요소 제거 이전:", dictionary)

# 딕셔너리의 요소를 제거
del dictionary["name"]
del dictionary['type']

# 요소 제거 후에 내용을 출력
print("요소 제거 이후:", dictionary)