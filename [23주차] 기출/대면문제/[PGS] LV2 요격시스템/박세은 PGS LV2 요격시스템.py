def solution(targets):
    targets.sort()
    chain = [[] for _ in range(len(targets))]
    
    for i in range(len(targets)):
        for j in range(i+1, len(targets)):
            if targets[i][1] > targets[j][0]:
                chain[i].append(targets[j])
            
            else: break
    
    
