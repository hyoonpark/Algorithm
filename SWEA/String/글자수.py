for t in range(1, int(input())+1):
    str1 = list(input())
    str2 = list(input())
    str_dict = {}
    max_num = 0
    for char in str1:
        str_dict[char] = 1
    for char in str2:
        if char in str1:
            str_dict[char] += 1
        else:
            pass
    for num in str_dict.values():
        if num > max_num:
            max_num = num
    print(f'#{t}', max_num - 1)