import sys
input = sys.stdin.readline

# 단절점은 단말노드가 아닌지 확인하면 됨 -> 연결된 정점의 개수가 2개 이상
# 단절선은 항상임!

n = int(input())    # 정점의 수
tree = [[] for _ in range(n + 1)]    # 트리의 연결 정보
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 단말노드인지 확인하는 함수
def is_end_node(node):
    if len(tree[node]) > 1:
        return False
    else:
        return True

q = int(input())    # 질의의 수
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:    # k번 정점이 단절점인지
        if not is_end_node(k):
            print('yes')
        else:
            print('no')
    else:    # k번 간선이 단절선인지
        print('yes')