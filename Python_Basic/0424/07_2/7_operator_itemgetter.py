from operator import itemgetter

books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
},
    {
    "제목": "내가 그린 기린 그림책",
    "가격": 20000
}]

print("# 가장 저렴한 책")
print(min(books, key=itemgetter("가격")))
print()

print("# 가장 비싼 책")
print(max(books, key=itemgetter("가격")))
