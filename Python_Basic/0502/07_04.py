def isQueueFull():
    global size, queue, front, rear
    if (rear == size - 1):
        return True
    else:
        return False


def enQueue(data):
    global size, queue, front, rear
    if (isQueueFull()):
        print('큐가 꽉참')
        return
    rear += 1
    queue[rear] = data


size = 5
queue = ['벨즈', '사나', '크로니', '파우나', None]
front = -1
rear = 4

print(queue)
enQueue("무메이")
print(queue)
enQueue('아이리스')
