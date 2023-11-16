from heapq import heapify, heappush, heappop

def solution(scoville, K):
    ans = 0
    heapify(scoville)    # 리스트를 heap으로 변환
    
    while True:
        # 요소가 하나밖에 남지 않았는데 K보다 작다면, 실패
        if len(scoville) <= 1 and scoville[0] < K:    
            return -1
        
        if scoville[0] >= K:    # heap에서 가장 작은 값이 K보다 크다면, 성공
            return ans
        
        ans += 1
        a, b = heappop(scoville), heappop(scoville)  # heap에서 1번째, 2번째로 작은 값 순서대로 빼기
        heappush(scoville, a + (b * 2))    # 두 값으로 조합한 결과 heap에 넣기