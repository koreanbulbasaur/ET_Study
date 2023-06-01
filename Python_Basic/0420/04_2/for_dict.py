# 딕셔너리를 선언
dictionary = {
    "name" : "용인",
    "type" : "city",
    "ingredient" : ["에버랜드", "캐리비안 베이", "우리랜드", "와우정사"],
    "origin" : "korea"
}

# for 반복문을 사용
for key in dictionary:
    # 출력
    print(key, ":", dictionary[key])