queue = ['크로니', '파우나', '무메이', None, None]
front = -1
rear = 2

print('-'*10, '큐 상태', '-'*10)
print('[출구] <-- ', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')
print('-'*25)

front += 1
data = queue[front]
queue[front] = None
print('deQueue --> ', data)
front += 1
data = queue[front]
queue[front] = None
print('deQueue --> ', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue --> ', data)
print('-'*25)

print('-'*10, '큐 상태', '-'*10)
print('[출구] <-- ', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')
