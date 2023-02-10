T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    for i in range(M-N+1):
        if str2[i:i+N] == str1:
            print(f'#{t}', 1)
            break
    else:
        print(f'#{t}', 0)