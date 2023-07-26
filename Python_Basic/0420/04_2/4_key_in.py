# 딕셔너리를 선언
dictionary = {
    "name" : "용인",
    "type" : "city",
    "ingredient" : ["에버랜드", "캐리비안 베이", "우리랜드", "와우정사"],
    "origin" : "korea"
}

# 사용자로부터 입력을 받음
key = input("> 접근하고자 하는 키: ")

# 출력
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")