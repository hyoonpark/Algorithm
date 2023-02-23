for t in range(1, int(input())+1):
    str_lst = []
    max_len = 0
    for _ in range(5):
        str_lst.append(input())
    for word in str_lst:
        if len(word) > max_len:
            max_len = len(word)
    words = ''
    for j in range(max_len):
        for i in range(5):
            if j < len(str_lst[i]):
                words += str_lst[i][j]
    print(f'#{t}', words)
