for tc in range(1, int(input())+1):
    rule = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    N, M = map(int, input().split())
    pw = [input() for _ in range(N)]
    s = 0
    e = 0
    Str = ''
    pw_lst = []
    cnt = 0
    ans = 0
    for c in pw:
        if '1' in c:
            for i in range(M-1, -1, -1):
                if c[i] == '1':
                    s = i - 55
                    e = i + 1
                    break
            Str = c[s:e]
            break
    for x in range(0, 56, 7):
        pw_lst.append(rule.get(Str[x:x+7]))
    for i in range(8):
        if i%2:
            cnt += pw_lst[i]
        else:
            cnt += (pw_lst[i]*3)
    if cnt%10 == 0:
        ans = sum(pw_lst)
    print(f'#{tc}', ans)