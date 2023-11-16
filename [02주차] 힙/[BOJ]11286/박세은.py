import heapq

heap = []
ans = []
N = int(input())

# 힙 원소 추가

for i in range(N):
    x = int(input())
    heapq.heappush(heap, x)
    
for j in heap :
    if j == 0 :
        if len(heap) == 0 :
            ans.append(0)
        
        else :
            heap.remove(j)
            ans.append(heapq.heappop(heap))
            
for v in ans :
    
        
print(ans)
        

