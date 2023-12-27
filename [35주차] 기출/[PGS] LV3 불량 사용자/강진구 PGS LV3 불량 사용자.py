def compare(id1,id2):
    cnt = 0
    cnt_ = 0
    for i1,i2 in zip(id1,id2):
        if i1 == i2:
            cnt += 1
        if i2 == '*':
            cnt_ += 1
    if cnt == len(id2) - cnt_:
        return True
    else:
        return False

def solution(user_id, banned_id):
    
    new_list = [[id,[]] for id in banned_id]
    
    for idx,ban in enumerate(banned_id):
        for user in user_id:
            if len(user)==len(ban):
                if compare(user,ban):
                    new_list[idx][1].append(user)
    
    path_list = []
    for element in new_list[0][1]:
        path_list.append([[element],0])
    
    total_path = []
    while path_list:
        temp_path = path_list.pop()
        if temp_path[1] == len(banned_id)-1:
            temp_path[0].sort()
            total_path.append(tuple(temp_path[0]))
            continue
        for element in new_list[temp_path[1]+1][1]:
            if element not in temp_path[0]:
                append_list = temp_path[0][:]
                append_list.append(element)
                path_list.append([append_list,temp_path[1]+1])
    
    return len(set(total_path))