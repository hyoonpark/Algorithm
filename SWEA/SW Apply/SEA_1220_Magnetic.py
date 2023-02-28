# 방법1
'''
0. 가로 순회로 풀고 싶어서 전치행렬을 만들어 준다. 1 다음 2가 나오는 것을 찾을 수 있다.
1. zip 함수를 사용해서 전치행렬을 만든다.
2. flag를 활용하여 교착 상태를 찾는다.
'''


for tc in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)]
    mag_t = list(map(list, zip(*mag)))
    cnt = 0
    for i in range(N):
        flag = False
        for j in range(N):
            if mag_t[i][j] == 1:
                flag = True
            elif mag_t[i][j] == 2:
                if flag:
                    cnt += 1
                flag = False

    print(f'#{tc}', cnt)


# 방법2
'''
0. stack을 활용해서 푼다. (IM대비에 안 맞을거 같지만...)
1. 행렬을 전치시키고 스택이 비어있을 때 1을 만나면 넣어준다.
2. 스택에 요소가 있고, 2를 만나면 스택을 비워주고 교착 상태에 +1 해준다.
'''

for tc in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)]
    mag_t = list(map(list, zip(*mag)))
    cnt = 0
    for i in range(100):
        S = []
        for j in range(100):
            if not S and mag_t[i][j] == 1:
                S.append(1)
            elif S and mag_t[i][j] == 2:
                cnt += 1
                S.pop()
    print(f'#{tc}', cnt)