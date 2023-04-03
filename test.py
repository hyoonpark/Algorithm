'''
3
7 5
5 4 2 7 1 2 3
8 6
10 10 1 3 1 5 4 7
3 1
1 3 1
'''
def conb(idx):
    global MAX
    if idx == N:
        # 부분집합이M개가 아니면 필요없음
        if sum(sel) != M:
            return
        # 만약 0이 연속해서 나오면 안됨!
        cnt = 0
        # 점수합
        total = 0
        for i in range(N):
            if cnt == 2:
                return
            if sel[i]:
                # 1이 나왔으니까 0표시 리셋
                cnt = 0
                # 1이나왔으니 그 idx total에 저장
                total += rocks[i]
            # 0이나옴!
            else:
                cnt +=1
        if cnt == 2:
            return
        # 점수가 최대가 되면 MAX갱신
        if total >= MAX:
            MAX = total
        # print(sel,total,MAX)
        return
    # 포함함
    sel[idx] = 1
    conb(idx+1)
    # 포함안함
    sel[idx] = 0
    conb(idx+1)

T = int(input())
for tc in range(1,T+1):
    # 돌 N개, M번만큼
    N, M = map(int, input().split())
    # 징검다리
    rocks = list(map(int, input().split()))
    # 부분집합에 포함되는것 표시할 리스트
    sel = [0]*N
    # 최대점수를 담을 변수
    MAX = 0
    conb(0)
    print(f'#{tc}', MAX)