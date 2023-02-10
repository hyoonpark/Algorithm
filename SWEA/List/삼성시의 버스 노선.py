T = int(input())

for t in range(1, T+1):
    N = int(input())
    cnts = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnts[i] += 1
    P = int(input())
    answer_list = []
    for _ in range(P):
        C = int(input())
        answer_list.append(cnts[C])

    print(f'#{t}', *answer_list)

