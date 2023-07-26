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
        # print("스택이 비었음")
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


def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if isStackEmpty():
        return True
    else:
        return False


size = 100
stack = [None for _ in range(size)]
top = -1

if __name__ == "__main__":
    exprAry = ['(A+B)', ')a+b()', '((A+B)-C', '(a+b]', '(<A+{b-v}/(d*h)>)']

    for expr in exprAry:
        top = -1
        print(expr, '==>', checkBracket(expr))
