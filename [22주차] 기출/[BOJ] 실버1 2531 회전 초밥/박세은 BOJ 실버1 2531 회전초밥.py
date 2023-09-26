n, d, k, c = map(int, input().split())
sushi = []

for _ in range(n):
    sushi.append(int(input()))

for i in range(k-1): # 컨베이어 벨트라서 추가로 검사할 부분 뒤에 추가
    sushi.append(sushi[i])

# 쿠폰으로 제공되는 스시 포함 상태로 시작
sushi_max = [c] # 답이 될 최대 스시리스트
test = [c] # 최대인지 테스트해주는 리스트

i = 0 # point 1
j = k-1 # point 2

while j-i == k-1: # j-i 개가 k-1 보다 작아지면 j가 끝부분에 도달한 것 이므로 반복문 종료
    test[0:0] = sushi[i:j+1] # 테스트 리스트에 i ~ j까지의 초밥 추가
    test = list(set(test)) # 중복 초밥 제거

    if len(test) > len(sushi_max): # 테스트 초밥이 최대면 값 바꿔주기
        sushi_max = test
    
    test = [c] # 테스트 초밥 초기화

    if j+1 < len(sushi): # j+1 이 리스트 범위를 넘지 않으면
        i += 1 # 포인터들 한칸씩 이동
        j += 1
    
    else:
        break # 리스트 범위를 벗어났으면 반복문 탈출

print(len(sushi_max))




