def isQueueEmpty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


size = 5
queue = [None for _ in range(size)]
front = rear = -1

print('큐가 비었는지 여부 ==>', isQueueEmpty())
