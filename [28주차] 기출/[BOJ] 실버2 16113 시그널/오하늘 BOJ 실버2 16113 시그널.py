import sys
input = sys.stdin.readline

# 이게 왜 실2? 이것저것 해보다가 결국 인터넷을 보게 되었답니다..

n = int(input()) # 5의 배수니까 나누면 칸수가 정해짐
arr = list(input().strip())


# 숫자 배열 (이때 위에서 아래로 셈, 나는 그냥 왼->오 이렇게 셌다가 완전 꼬였음)
zero = ['#','#','#','#','#','#','.','.','.','#','#','#','#','#','#']
one = ['#','#','#','#','#']
two = ['#','.','#','#','#','#','.','#','.','#','#','#','#','.','#']
three = ['#','.','#','.','#','#','.','#','.','#','#','#','#','#','#']
four = ['#','#','#','.','.','.','.','#','.','.','#','#','#','#','#']
five = ['#','#','#','.','#','#','.','#','.','#','#','.','#','#','#']
six = ['#','#','#','#','#','#','.','#','.','#','#','.','#','#','#']
seven = ['#','.','.','.','.','#','.','.','.','.','#','#','#','#','#']
eight = ['#','#','#','#','#','#','.','#','.','#','#','#','#','#','#']
nine = ['#','#','#','.','#','#','.','#','.','#','#','#','#','#','#']
blank = ['.','.','.','.','.']

# LIST
# 수 넣어줄 리스트 생성
num = [arr[i * (len(arr)//5) : (i+1)*(len(arr)//5)] for i in range((len(arr) + (len(arr)//5)))]

tmp = [] # 개별 수 탐지
ans = [] # 답

for i in range(len(arr)//5):
    for j in range(5):
        tmp.append(num[j][i])
        if tmp == zero :
            ans.append(0)
            tmp = [] # 사용했으니 초기화
        elif tmp == one and i < (len(arr)//5)-1: # 0과 1의 시작이 같으므로 구분해야함
            if num[j][i+1] == '.': # 샾 뒤에 . 인 경우
                ans.append(1)
                tmp = []
        # 밑에 이거 안넣어주면 에러임. 근데 why ? .이면 되는거 아닌감..ㅠ
        elif tmp == one and i == (len(arr)//5)-1 and j == 4 :
            ans.append(1)
            temp = []
        elif tmp == two :
            ans.append(2)
            tmp = []
        elif tmp == three :
            ans.append(3)
            tmp = []
        elif tmp == four :
            ans.append(4)
            tmp = []
        elif tmp == five :
            ans.append(5)
            tmp = []
        elif tmp == six :
            ans.append(6)
            tmp = []
        elif tmp == seven :
            ans.append(7)
            tmp = []
        elif tmp == eight :
            ans.append(8)
            tmp = []
        elif tmp == nine :
            ans.append(9)
            tmp = []
        elif tmp == blank :
            tmp = []

for i in ans:
    print(i,end='')