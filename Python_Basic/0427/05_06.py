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


def deleteNode(deleteData):
    global memory, head, current, pre
    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del (current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del (current)
            return


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

    deleteNode("사나")
    printNodes(head)

    deleteNode("크로니")
    printNodes(head)

    deleteNode("무메이")
    printNodes(head)

    deleteNode("미누")
    printNodes(head)
