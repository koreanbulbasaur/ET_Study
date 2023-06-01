def isStackEmpty():
    global size, stack, top
    if (top == -1):
        return True
    else:
        return False


def peek():
    global size, stack, top
    if (isStackEmpty()):
        print('스택이 비었음')
        return None
    return stack[top]


size = 5
stack = ['커피', '아이스티', '메론소다', None, None]
top = 2

print(stack)
retData = peek()
print("top의 데이터 확인 -->", retData)
print(stack)
