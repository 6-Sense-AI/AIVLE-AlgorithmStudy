# 해결 X
# DP라고 함,,,

def solution(temp, t1, t2, a, b, onboard):
    ans = 0
    now = 0
    last = len(onboard)
    
    while now < last - 1:
        srt = False
        for i in range(now, last):
            if onboard[i]:
                srt = i
                break
        if srt:
            end = last - 1
            for i in range(srt, last):
                if not onboard[i]:
                    end = i
                    break
            print(srt, end)
        else:
            break
        
        # 아래 방법 중에 하나 선택해야 함
        # 최소 온도로 설정, 유지
        # : (최소 온도 - 도달 시간) * a + (유지 시간) * b
        target1 = t1 if abs(temp - t1) < abs(temp - t2) else t2
        v1 = abs(temp - target1) * a + (end - abs(temp - target1) - 1) * b
        # 끄는 것 고려 최고 온도로 설정, 끄기
        # : (최고 온도 - 도달 시간) * a
        # 각 탑승 구간에서 최고로 좋은 정답 찾으면 될 듯...!
        temp = target1
        now = end
        ans += v1
        
        
        
    return ans