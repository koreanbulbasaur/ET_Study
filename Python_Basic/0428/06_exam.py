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


def check(expr):
    while True:
        push(expr)
        # print(stack)
        return expr


def reverse(stack):
    for idx, stac in enumerate(stack):
        if idx == len(exprAry) - 1:
            print(pop(), '==> 우리집')
        else:
            print(pop(), '==>', end=' ')


top = -1

if __name__ == "__main__":
    exprAry = ['주황', '초록', '파랑', '보라', '빨강', '노랑']
    size = len(exprAry)
    stack = [None for _ in range(size)]

    print('과자집에 가는 길 :', end=' ')
    for n, expr in enumerate(exprAry):
        if n == len(exprAry) - 1:
            print(expr, '==> 과자집')
        else:
            print(expr, '==>', end=' ')
        push(expr)

    print("우리집에 오는 길 :", end=' ')
    reverse(stack)
