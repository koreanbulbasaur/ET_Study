# 딕셔너리 선언함
dictionary = {
    "name" : "깍두기",
    "type" : "김치",
    "ingredient" : ["무", "고춧가루", "소금", "액젓"],
    "origin" : "필리핀"
}

# 출력
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

# 값 변경
dictionary["name"] = "깍두기 김치"
print("name:", dictionary["name"])