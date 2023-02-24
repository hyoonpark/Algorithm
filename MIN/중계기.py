'''
(실패한 아이디어 델타검색으로 찾으려고 했음)
0. 2차원 배열을 받고, 제곱근을 어떻게 구할 것인가에 대한 아이디어 필요.
1. 인덱스의 제곱값을 리스트로 만들어 사용. (문제 조건을 보고 범위 잘 따질것)
2. 중계기의 위치 찾기.
3. 중계기와 집의 거리 제곱값의 최대값 찾기.
4. 최대값보다 같거나 큰 숫자중 가장 작은 값을 찾아 그 인덱스를 출력하고 멈추기.
'''

for tc in range(1, int(input())+1):
    N = int(input())    # map 크기
    town = [list(map(int, input().split())) for _ in range(N+1)]
    square = []    # 제곱근을 구하기 위해 제곱 리스트 만들어주기
    mx = 0    # 최대 거리 저장
    for x in range(16):    # 최대 거리의 제곱이 200이기 때문에
        square.append(x**2)
    for i in range(N+1):
        if 2 in town[i]:
            r = i
            c = town[i].index(2)
    for ni in range(N+1):
        for nj in range(N+1):
            if town[ni][nj] == 1:
                D = (ni - r)**2 + (nj - c)**2    # 거리의 제곱값
                if D > mx:
                    mx = D
    for s in square:
        if s >= mx:
            ans = square.index(s)    # 제곱근 찾기
            break

    print(f'#{tc}', ans)