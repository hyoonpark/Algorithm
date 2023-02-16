def Winner(start, end):
    if start == end:
        return start  # 한명 남았다는 의미이므로 가위바위보를 위해 리턴

    a = Winner(start, (start + end) // 2)
    b = Winner((start + end) // 2 + 1, end)
    return rsp(a, b)  # 가위바위보 실시


def rsp(x, y):
    if cards[x] == cards[y]:  # 비긴 경우
        return x
    elif cards[x] - cards[y] == 1 or cards[x] - cards[y] == -2:  # x가 이긴 경우
        return x
    return y



for t in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print(f'#{t}', Winner(0, N-1)+1)
