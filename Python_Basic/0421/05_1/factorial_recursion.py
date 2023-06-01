def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
for num in range(1, 6):
    print(f"{num}!", factorial(num))
    
# 두 줄 팩토리얼
# def factorial(n):
#     return 1 if n <= 1 else n * factorial(n-1)