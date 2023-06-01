def factorial(n):
    output = 1
    
    for i in range(1, n + 1):
        output *= i
    
    return output

for num in range(1, 6):
    print(f"{num}!", factorial(num))