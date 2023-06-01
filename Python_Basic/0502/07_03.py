def isQueueFull():
    global size, queue, front, rear
    if (rear == size - 1):
        return True
    else:
        return False


size = 5
queue = ['벨즈', '사나', '크로니', '파우나', '무메이']
front = -1
rear = 4

print('큐가 꽉 찼는지 여부 ==>', isQueueFull())
