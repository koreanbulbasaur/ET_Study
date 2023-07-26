class Test:
    def __init__(self, name) -> None:
        self.name = name
        print(f"{self.name} - 생성됨")

    def __del__(self):
        print(f"{self.name} - 파괴됨")


Test("A")
Test("B")
Test("C")
