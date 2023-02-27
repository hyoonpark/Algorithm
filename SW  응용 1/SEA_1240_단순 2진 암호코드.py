for tc in range(1, int(input())+1):
    rule = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    N, M = map(int, input().split())
    pw = [input() for _ in range(N)]
    s = 0
    e = 0
    lst = []
    for c in pw:
        if '1' in c:
            for i in range(M-1, -1, -1):
                if c[i] == 1:
                    s = i - 56
                    e = i
                    break
            for x in c[s:i+1:7]:
                lst.append(rule.get(x))