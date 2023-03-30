scale = list(map(int, input().split()))
while True:
    if scale[0]+scale[-1] != 9:
        print('mixed')
        break
    for i in range(7):
        if scale[i+1]-scale[i] == 1:
            continue
        else:
            break
    else:
        print('ascending')
        break
    for i in range(7):
        if scale[i]-scale[i+1] == 1:
            continue
        else:
            break
    else:
        print('descending')
        break
    print('mixed')
    break