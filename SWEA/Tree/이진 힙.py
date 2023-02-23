def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2



for tc in range(1, int(input())+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    heap = [0 for _ in range(N+1)]
    last = 0
    ans = 0

    for num in num_lst:
        enq(num)

    while N != 0:
        ans += heap[N//2]
        N //= 2

    print(f'#{tc}', ans)