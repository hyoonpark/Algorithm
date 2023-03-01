'''
0. 손님이 오기전까지 구워진 붕어빵을 계산하고, 앞에 손님이 다녀간 만큼 빼준 것이 현재 붕어빵 수!
1. 손님이 오는 시간은 제각각 다르므로 sort 메서드로 오름차순 정리 해준다.
2. 손님이 왔을때 붕어빵의 수가 0 이거나 음수면 Impossible 출력!
'''

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    cus = list(map(int, input().split()))
    cus.sort()    # 오는 시간을 오름차순으로 정리
    ans = 'Possible'
    rslt = 0
    for n in range(N):
        rslt = (cus[n] // M)*K - n
        if rslt <= 0:
            ans = 'Impossible'
            break

    print(f'#{tc}', ans)