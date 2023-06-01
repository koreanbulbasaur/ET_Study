def isQueueFull():
    global size, queue, front, rear
    if rear != size-1:
        return False
    elif rear == size-1 and front == -1:
        return True
    else:
        for i in range(front+1, size):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


size = 5
queue = [None, None, 'kronii', 'Botan', 'Mio']
front = 1
rear = 4

print("큐가 꽉 찼는지 여부 ==>", isQueueFull())
print('큐 상태 ==>', queue)
