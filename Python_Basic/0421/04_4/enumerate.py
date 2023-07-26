# 변수를 선언합니다.
example_list = ["요소A", "요소B","요소C"]

# 그냥 출력
print("# 단순 출력")
print(example_list)
print('*'*100)

# enumerate() 함수를 적용해 출력합니다.
print('# enumerate() 함수 적용 출력')
print(enumerate(example_list))
print('*'*100)

#list() 함수로 강제 변환해 출력함
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print('*'*100)

# for 반복문과 enumerate() 함수 조합해서 사용하기
print("# 반복문과 조합")
for i, value in enumerate(example_list):
    print(f"{i}번째 요소는 {value}입니다.")