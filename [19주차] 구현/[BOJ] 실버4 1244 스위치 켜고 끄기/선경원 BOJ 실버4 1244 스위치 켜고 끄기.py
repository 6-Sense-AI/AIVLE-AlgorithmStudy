

## 스위치 개수 입력

n = int(input())

## 스위치 상태 입력

on_off = [-1] + list(map(int,input().split()))

## 학생 수 입력

students = int(input())

## 학생 성별, 받은 수 입력


def change(num):
    if on_off[num] == 0:
        on_off[num] = 1
    else:
        on_off[num] = 0
    return

for _ in range(students):
    gen, num = map(int, input().split())

    ## 남자 배수는 간격으로
    if gen == 1:
        for i in range(num, n+1, num):
            change(i)
    
    ## 여학생
    ## 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간
    else:

        ## 받은 자연수에 해당하는 스위치는 대칭과 관계 없이 무조건 바꿈
        change(num)

        for k in range(n//2):

            ## 범위 초과시 패스
            if num + k > n or num - k < 1 : 
                break

            ## 대칭 부분 바꿔주기
            if on_off[num + k] == on_off[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, n+1):
    print(on_off[i], end = " ")
    if i % 20 == 0 :
        print()
