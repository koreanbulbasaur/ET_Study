import random
import math


class Node():
    def __init__(self) -> None:
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return

    print(f"{current.data[0]} 편의점, 거리: {current.data[1]}")

    while current.link != start:
        current = current.link
        print(f"{current.data[0]} 편의점, 거리: {current.data[1]}")
    print()


def sort_data(data):
    # print(data)
    # 데이터를 숫자순으로 정렬
    data_sorted = sorted(data, key=lambda x: sum(x[1:]))

    # 각각의 데이터를 노드에 할당
    global head, current, pre
    for item in data_sorted:
        distance = math.sqrt(item[1] ** 2 + item[2] ** 2)
        node = Node()
        node.data = [item[0], distance]
        if head == None:
            head = node
        else:
            pre.link = node
        pre = node
        node.link = head


head, current, pre = None, None, None
market = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J']

if __name__ == "__main__":

    dataArray = ()

    for i in market:
        x = random.randrange(1, 100)
        y = random.randrange(1, 100)
        dataArray = dataArray + ((i, x, y),)

    sort_data(dataArray)

    printNodes(head)
