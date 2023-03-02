'''
0. 배열을 만들어 주어진 범위에 해당 숫자를 넣을 수 있다.
1. 슬라이싱을 통해 인덱스 1번 부터 출력할 수 있도록 한다.
'''

for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())    # N개 상자, Q회 동안 숫자 변경
    box = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())    # i로 바꿀 범위
        for b in range(L, R+1):
            box[b] = i
    ans = box[1:]
    print(f'#{tc}', *ans)