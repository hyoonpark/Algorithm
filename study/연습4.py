'''
0. 중위순회를 할 줄 안다.
1. 노드번호에 맞춰 트리에 정보를 저장한다.
2. 중위순회 함수를 만들어 문자들을 더한후 출력한다.
'''

def inOrder(n):
    global char
    if n <= N:
        inOrder(n*2)
        char += tree[n]
        inOrder(n*2+1)



for tc in range(1, 11):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    char = ''
    for i in range(1, N+1):
        lst = list(input().split())
        tree[i] = lst[1]
    inOrder(1)
    print(f'#{tc}', char)