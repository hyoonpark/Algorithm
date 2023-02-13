def push(item):
    return S.append(item)

def pop():
    return S.pop()

for t in range(1, int(input())+1):
    chars = input()
    S = []
    top = -1
    for char in chars:
        if char not in S:
            push(char)
            top += 1
        elif char in S:
            if S[top] != char:
                push(char)
                top += 1
            elif S[top] == char:
                pop()
                top -= 1

    print(f'#{t}', len(S))