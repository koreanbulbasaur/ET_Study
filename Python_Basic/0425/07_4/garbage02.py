class Test:
    def __init__(self, name) -> None:
        self.name = name
        print(f"{self.name} - 생성됨")

    def __del__(self):
        print(f"{self.name} - 파괴됨")


a = Test("A")
b = Test("B")
c = Test("C")
