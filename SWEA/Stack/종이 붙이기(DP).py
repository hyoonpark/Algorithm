def paper(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        return paper(N-1) + (2*paper(N-2))


for t in range(1, int(input())+1):
    N = (int(input())) // 10
    print(f'#{t}', paper(N))
