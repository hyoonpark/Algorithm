for _ in range(int(input())):
    str1 = input()
    N = 5
    M = len(str1) * 4 + 1
    i = 1
    j = 0
    while i < 6:
        if i == 1 or i == 5:
            arr1 = list('.' * M)
            for x in range(2, M, 4):
                arr1[x] = '#'
            i += 1
            print(''.join(arr1))
        elif i == 3:
            arr2 = list('.' * M)
            for x in range(0, M, 4):
                arr2[x] = '#'
            for x in range(2, M, 4):
                arr2[x] = str1[j]
                j += 1
            i += 1
            print(''.join(arr2))
        else:
            arr3 = list('.' * M)
            for x in range(1, M, 2):
                arr3[x] = '#'
            i += 1
            print(''.join(arr3))