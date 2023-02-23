def Dice(A, B, C):
    if A == B == C:
        return 10000 + (A * 1000)
    elif A == B or B == C or C == A:
        if A == B:
            return 1000 + (A * 100)
        elif B == C:
            return 1000 + (B * 100)
        elif C == A:
            return 1000 + (C * 100)
    else:
        return 100 * (max(A, B, C))

A, B, C = map(int, input().split())
print(Dice(A, B, C))