def isQueueFull():
    global size, queue, front, rear
    if ((rear+1) % size == front):
        return True
    else:
        return False


def isQueueEmpty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def enQueue(data):
    global size, queue, front, rear
    if isQueueFull():
        print('큐가 꽉 참')
        return
    rear = (rear+1) % size
    queue[rear] = data


def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        print("식당 영업 종료!")
        return None
    front = (front+1) % size
    data = queue[0]
    queue[0] = None
    for i in range(size):
        if queue[i] == None:
            if i == len(queue)-1:
                queue[i] = None
                # print(queue)
            else:
                queue[i] = queue[i+1]
                queue[i+1] = None
        else:
            pass
    return data


def peek():
    global size, queue, front, rear
    if isQueueEmpty():
        print('식당 영업 종료!')
        return None
    return queue[(front+1) % size]


size = 5
queue = ['kronii', 'Anya', 'Botan', 'Mio', 'roboco']
front = rear = -1
if __name__ == '__main__':
    for data in queue:
        enQueue(data)
    print('대기 줄 상태 :', queue)

    for i in range(5):
        data = deQueue()
        print(f'{data} 님 식당에 들어와주세요')
        print('대기 줄 상태 :', queue)
        if isQueueEmpty():
            print("식당 영업 종료!")
