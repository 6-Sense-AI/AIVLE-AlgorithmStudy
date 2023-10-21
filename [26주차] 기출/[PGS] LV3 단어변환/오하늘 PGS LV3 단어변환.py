from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if not target in words: # 타겟이 없으면
        return 0

    def bfs(begin, target, words): # bfs 렛츠고
        q = deque()
        q.append([begin, 0])
        
        while q:
            word, step = q.popleft()
            
            if word == target: # 타깃과 같으면
                return step
            
            for w in words : # 단어장
                cnt = 0
                for i in range(len(word)) :# 내 현재 단어
                    if word[i] != w[i] :
                        cnt+= 1
                if cnt == 1: # 1개만 다름
                    q.append([w, step+1]) # 스탭을 더해준다
                
    answer = bfs(begin, target, words)
    
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))