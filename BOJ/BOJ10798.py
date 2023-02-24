str_lst = [list(input()) for _ in range(5)]
mx = 0
char = ''
for lst in str_lst:
    if len(lst) > mx:
        mx = len(lst)
for j in range(mx):
    for i in range(5):
        if j < len(str_lst[i]):
            char += str_lst[i][j]

print(char)