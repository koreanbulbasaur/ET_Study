def hanoitop(n, start, end, support):
    if n == 1:
        print(start, "→", end)
    else:
        hanoitop(n-1, start, support, end)
        print(start, "→", end)
        hanoitop(n-1, support, end, start)


n = int(input("원판의 개수를 입력해주세요 :"))
hanoitop(n, "A_Top", "B_Top", "C_Top")
