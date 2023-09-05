n = int(input())  # 사람 수
tall = list(map(int, input().split()))  # 키 정보
tst = [i for i in range(0, n)]  # 남은 자리 인덱스 리스트
ans = [0 for _ in range(n)]  # 줄 선 순서 (답)

# 예제 4번으로 설명
# =============== #
# 키가 1인 사람 앞에 6명이 있어야 하므로 tst[6]번째에 기록된 인덱스 위치에 가야함
# tst[6] = 6 이므로 ans[6]에 1인 사람 기록. 이후 tst의 6번째 인덱스 삭제
# 끝까지 반복해준다

for i, j in enumerate(tall, start=1):
    ans[tst[j]] = str(i)  # join 함수 사용을 위해 문자열로 저장
    del tst[j]


print(" ".join(ans))
