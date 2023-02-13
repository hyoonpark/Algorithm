def push(item):
    return S.append(item)

def pop():
    return S.pop()

def isEmpty():
    return len(S) == 0

for t in range(1, int(input())+1):
    chars = input()
    S = []
    result = 1
    for char in chars:
        if char == '(' or char == '{':
            push(char)
        elif char == ')':
            if isEmpty():
                result = 0
                break
            if pop() != '(':
                result = 0
                break
        elif char == '}':
            if isEmpty():
                result = 0
                break
            if pop() != '{':
                result = 0
                break
    if S:
        result = 0
    print(f'#{t}', result)