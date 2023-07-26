def isStackFull():
    global size, stack, top
    if (top >= size-1):
        return True
    else:
        return False


def isStackEmpty():
    global size, stack, top
    if (top == -1):
        return True
    else:
        return False


def push(data):
    global size, stack, top
    if (isStackFull()):
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data


def pop():
    global size, stack, top
    if (isStackEmpty()):
        print("스택이 비었음")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():  # 마지막에 넣은 값 확인
    global size, stack, top
    if (isStackEmpty()):
        print("스택이 비었음")
        return None
    return stack[top]


size = int(input("스택의 크기를 입력하세요 ==> "))
stack = [None for _ in range(size)]
top = -1

if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'x' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            while True:
                if data.isspace():
                    print("값을 입력해주세요.")
                    data = input("입력할 데이터 ==> ")
                else:
                    push(data)
                    print("스택 상태 :", stack)
                    break
        elif select == "E" or select == 'e':
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 :", stack)
        elif select == "V" or select == 'v':
            data = peek()
            print("확인된 데이터 ==>", data)
            print("스택 상태 :", stack)
        elif select == "":
            print("값을 입력해주세요.")
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
