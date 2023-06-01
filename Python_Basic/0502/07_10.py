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
    rear += 1
    queue[rear] = data


def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        print("큐가 빔")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global size, queue, front, rear
    if isQueueEmpty():
        print('큐가 빔')
        return None
    return queue[front+1]


size = int(input('큐 크기를 입력하세요 ==> '))
queue = [None for _ in range(size)]
front = rear = -1
if __name__ == '__main__':
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'x' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            while True:
                if data.isspace() or data == '':
                    print("값을 입력해주세요.")
                    data = input("입력할 데이터 ==> ")
                else:
                    enQueue(data)
                    print("큐 상태 :", queue)
                    break
        elif select == "E" or select == 'e':
            data = deQueue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태 :", queue)
        elif select == "V" or select == 'v':
            data = peek()
            print("확인된 데이터 ==>", data)
            print("큐 상태 :", queue)
        elif select == "":
            print("값을 입력해주세요.")
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
