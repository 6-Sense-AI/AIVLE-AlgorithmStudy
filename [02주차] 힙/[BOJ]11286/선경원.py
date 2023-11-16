abs_heap = []
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(abs_heap, (abs(num), num))
