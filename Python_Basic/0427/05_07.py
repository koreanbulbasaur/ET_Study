class Node():
    def __init__(self) -> None:
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return

    print(current.data, end=' ')

    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            return current
    return Node()


memory = []
head, current, pre = None, None, None
dataArray = ["벨즈", "사나", "크로니", "파우나", "무메이"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    fNode = findNode("크로니")
    print(fNode.data)

    fNode = findNode("무메이")
    print(fNode.data)

    fNode = findNode("미누")
    print(fNode.data)
