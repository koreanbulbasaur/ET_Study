class Node():
    def __init__(self) -> None:
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


def makeSimpleLinkedList(namePhone):
    global memory, head, current, pre
    printNodes(head)
    node = Node()
    node.data = namePhone
    memory.append(node)
    if head == None:
        head = node
        return

    if head.data[0] > namePhone[0]:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[0] > namePhone[0]:
            pre.link = node
            node.link = current
            return

    current.link = node


memory = []
head, current, pre = None, None, None
dataArray = [["다현", "010-1111-1111"], ["정연", "010-2222-2222"], ["쯔위", "010-3333-3333"],
             ["사나", "010-4444-4444"], ["지효", '010-5555-5555']]

if __name__ == "__main__":

    for data in dataArray:
        makeSimpleLinkedList(data)

    printNodes(head)
