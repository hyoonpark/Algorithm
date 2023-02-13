def push(item):
    return S.append(item)

def pop():
    return S.pop()

for t in range(1, 11):
    N, P = input().split()
    S = []
    top = -1
    for num in P:
        if num not in S:
            push(num)
            top += 1
        elif num in S:
            if S[top] != num:
                push(num)
                top += 1
            elif S[top] == num:
                pop()
                top -= 1
    print(f'#{t}', ''.join(S))
