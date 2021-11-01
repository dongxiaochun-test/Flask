import queue
q = queue.Queue()
for i in range(10):
    print(f'进：{i}')
    q.put(i)

for k in range(10):
    m = q.get()
    print(f'出：{m}')