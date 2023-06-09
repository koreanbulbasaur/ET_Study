# 함수를 선언
def power(x): return x * x
def under_3(x): return x < 3


# 변수를 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용함
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) :", output_a)
print("map(power, list_input_a) :", list(output_a))
print()

# filter() 함수를 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) :", output_b)
print("filter(under_3, list_input_a) :", list(output_b))
