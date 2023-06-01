max_value = 0
a = 0
b = 0

for i in range(1, 101):
    j = 100 - i
    
    value = j * i
    if max_value > value:
        break
    else:
        max_value = value
        a = i
        b = j
    
print(f"최대가 되는 경우: {a} * {b} = {max_value}")