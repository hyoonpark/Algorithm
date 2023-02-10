for t in range(1, int(input())+1):
    str1 = input()
    if str1 == str1[::-1]:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)