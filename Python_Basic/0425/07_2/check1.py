from primePy import primes

list_prime = []

for i in range(100, 1001):
    if primes.check(i) == True:
        list_prime.append(i)

print(f"100~1000 사이에 있는 소수의 개수는 {len(list_prime)}개 입니다.")
