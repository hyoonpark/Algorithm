for t in range(1, int(input())+1):
    N = int(input())
    char = ''
    for n in range(N):
        x, y = input().split()
        y = int(y)
        char += (x*y)
    print(f'#{t}')
    for i in range(len(char)):
        if (i+1)%10 == 0:
            print(char[i])
        else:
            print(char[i], end='')
    print()