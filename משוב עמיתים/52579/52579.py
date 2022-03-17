from timeit import timeit


def max_even_seq(n):
    str_n = str(n)
    counter = 0
    max = 0
    for ch in str_n:
        if int(ch) % 2 == 0:
            counter += 1
        elif counter > max:
            max = counter
            counter = 0
    return(max)
    pass

########
# Tester
########

def test():
    if max_even_seq(23300247524689) != 4:
        print("error in max_even_seq")


print("123468579", "result:", max_even_seq(123468579), "exepted: 3")
print("2461285", "result:", max_even_seq(2461285), "exepted: 3")
print("1359", "result:", max_even_seq(1359), "exepted: 0")
print("2468", "result:", max_even_seq(2468), "exepted: 4")


print(timeit(lambda: max_even_seq(11111111111111111111), number=10000))
print(timeit(lambda: max_even_seq(22222222222222222222), number=10000))
print(timeit(lambda: max_even_seq(12121212121212121212), number=10000))
print(timeit(lambda: max_even_seq(99999999999999999999), number=10000))
