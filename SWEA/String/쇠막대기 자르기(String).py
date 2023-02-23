for t in range(1, int(input())+1):
    string = input()
    new_string = string.replace('()', '|')
    stick = 0
    cuts = 0
    for i in new_string:
        if i == '(':
            stick += 1
            cuts += 1
        elif i == '|':
            cuts += stick
        elif i == ')':
            stick -= 1
    print(f'#{t}', cuts)