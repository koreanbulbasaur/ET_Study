def deQueue():
    global size, queue, front, rear
    if front == rear:
        print('큐가 비었음')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


size = 5
queue = ['크로니', None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print('추출한 데이터 -->', retData)
print(queue)
retData = deQueue()
