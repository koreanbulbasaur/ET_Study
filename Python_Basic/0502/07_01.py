queue = [None for _ in range(5)]
front = rear = -1

rear += 1
queue[rear] = '크로니'
rear += 1
queue[rear] = '보탄'
rear += 1
queue[rear] = '미오'

print('-'*10, '큐 상태', '-'*10)
print('[출구] <-- ', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')
