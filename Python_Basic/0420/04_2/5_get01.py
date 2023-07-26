# 딕셔너리를 선언
dictionary = {
    "name" : "용인",
    "type" : "city",
    "ingredient" : ["에버랜드", "캐리비안 베이", "우리랜드", "와우정사"],
    "origin" : "korea"
}

# 존재하지 않는 키에 접근
value = dictionary.get("존재하지 않는 키")
print("값:", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근함")