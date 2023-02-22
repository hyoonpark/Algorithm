'''
1~N: 자연수 이진탐색트리에 저장
왼쪽, 현재, 오른쪽 노드 순으로 저장 ->중위??
완전 이진 트리의 노드 번호는 루트1번, 아래로 내려가면서 왼쪽 오른쪽 순 증가
N이 주어졌을 때 완전이진트리로 만든 이진탐색 트리 루트에 저장된값과
N//2번 노드(부모)에 저장된 값 출력
'''
def Search(node):
    global num
    if L[node]:
        Search(L[node])
    tree[node] = num
    num += 1
    if R[node]:
        Search(R[node])



for tc in range(1, int(input())+1):
    N = int(input())
    L = [0] * (N+1)
    R = [0] * (N+1)
    tree = [0] * (N+1)
    num = 1
    for i in range(1, N//2+1):
        L[i] = 2*i
        if 2*i+1 <= N:
            R[i] = 2*i+1
    Search(1)
    idx = tree[1]
    ans = tree[N//2]

    print(f'#{tc}', idx, ans)