def f1(L):
    count = 0
    n = len(L)
    while n > 0:
        n = n // 2
        for i in range(n):
            flag=True
            for curr in L:
                if curr == i:
                    count += i
                    L.append(i)
                    flag=False
                    break
            if flag:
                count += len(L)
        print(len(L))
    print(count)
    return L

print(len(f1(list(range(100)))))
print("--------")
print(len(f1(list(range(25)) + ['a']*75)))
print("--------")
print(len(f1(['a']*25 + list(range(25, 50)) + ['a']*50)))
print("--------")
print(len(f1(['a']*100)))
