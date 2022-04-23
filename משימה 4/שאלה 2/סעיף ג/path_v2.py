def path_v2(A, s, t, k, summ=[0, {i:0 for i in range(16)}]):

    summ[0]+=1

    if k == 0:
        return s == t, summ

    if k == 1:
        if A[s][t] == 1:
            return True, summ
        return False, summ

    for i in range(len(A)):
        summ[1][i] += 1
        mid = k // 2
        if path_v2(A, s, i, mid, summ=summ)[0] and path_v2(A, i, t, k - mid, summ=summ)[0]:
            return True, summ
    return False, summ

print("A:", [[0 for i in range(4)] for j in range(4)])
print(path_v2([[0 for i in range(4)] for j in range(4)], 0, 4, 4))
