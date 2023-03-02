for tc in range(1, int(input())+1):
    clap = list(map(int, input()))
    total = 0    # 필요한 사람수
    cnt = 0    # 기립한 사람수
    ans = 0
    temp = 0
    for i in range(1, len(clap)):
        cnt += clap[i-1]
        total = i
        temp = total - cnt
        if temp >= ans:
            ans = temp
    print(f'#{tc}', ans)