# 테스트3번이 안되는데 과연 어디서 잘못된걸까..

from collections import defaultdict, deque
def solution(begin, target, words):
    visited = dict()
    for w in words:
        visited[w] = False
    visited[begin] = True
    graph = defaultdict(list)
    
    for w in words:
        if dif_count(w,begin) == 1:
            graph[begin].append(w)
        for v in words:
            if dif_count(w,v) == 1:
                graph[w].append(v)
                graph[v].append(w)
    
    return bfs(graph, visited, begin, target, 0)
    
def bfs(graph, visited, st, end, cnt):
    que = deque([(st,end,cnt)])
    
    while que:
        st, end, cnt = que.popleft()
        visited[st] = True
        if end in graph[st]:
            cnt += 1
            st = end
            break
        else:
            for g in graph[st]:
                if visited[g] == False:
                    que.append((g,end,cnt+1))
                    visited[g] = True
                    
    
    if st!=end and end not in graph.keys():
        cnt = 0
    
    return cnt

def dif_count(w1,w2):
    count = 0
    w1_lst = list(w1)
    w2_lst = list(w2)
    
    for w_ in w1_lst:
        if w_ not in w2_lst:
            count += 1
    return count

