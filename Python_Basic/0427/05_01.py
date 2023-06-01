class Node():
    def __init__(self) -> None:
        self.data = None
        self.link = None


node1 = Node()
node1.data = "벨즈"
node1.link = node1

node2 = Node()
node2.data = "사나"
node1.link = node2
node2.link = node1

node3 = Node()
node3.data = "크로니"
node2.link = node3
node3.link = node1

node4 = Node()
node4.data = "파우나"
node3.link = node4
node4.link = node1

node5 = Node()
node5.data = "무메이"
node4.link = node5
node5.link = node1

current = node1
print(current.data, end=' ')
while current.link != node1:
    current = current.link
    print(current.data, end=' ')
