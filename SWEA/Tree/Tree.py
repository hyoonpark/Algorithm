# 부모 번호를 인덱스로 자식 번호를 저장

E, N = map(int, input().split())    # 간선, 노드 번호
n_lst = list(map(int, input().split()))
tree = [[0 for _ in range(E+2)] for _ in range(2)]
for i in range(0, E*2, 2):
    p, c = n_lst[i], n_lst[i+1]    # 부모와 자식 노드 번호
    if tree[0][p] == 0:
        tree[0][p] = c
    else:
        tree[1][p] = c
print(tree)


# 자식 번호를 인덱스로 부모 번호를 저장

E, N = map(int, input().split())    # 간선, 노드 번호
n_lst = list(map(int, input().split()))
tree = [0 for _ in range(E+2)]
for i in range(0, E*2, 2):
    p, c = n_lst[i], n_lst[i+1]    # 부모와 자식 노드 번호
    tree[c] = p
print(tree)


# 루트 찾기, 조상 찾기
# e.g) 1번 노드의 조상 찾기

anc = []
c = 1
while tree[c] != 0:    # 루트인지 확인
    c = tree[c]
    anc.append(c)
root = c
print(root)