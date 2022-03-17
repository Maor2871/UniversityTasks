from timeit import timeit


def max_even_seq(n):
    n_str = str(n)
    store_ls = []
    for i in range(len(n_str)):
        counter = 0
        while int(n_str[i])%2 == 0:
            i = i+1
            counter = counter + 1
        store_ls = store_ls +  [counter]
    return max(store_ls)


########
# Tester - left here so it will be easier to check, it does pass it :) 
########

def test():
    if max_even_seq(23300247524689) != 4:
        print("error in max_even_seq")

print("123468579", "result:", max_even_seq(123468579), "exepted: 3")
print("2461285", "result:", max_even_seq(2461285), "exepted: 3")
print("1359", "result:", max_even_seq(1359), "exepted: 0")
# print("2468", "result:", max_even_seq(2468), "exepted: 4")


print(timeit(lambda: max_even_seq(11111111111111111111), number=10000))
print(timeit(lambda: max_even_seq(32222222222222222223), number=10000))
print(timeit(lambda: max_even_seq(12121212121212121212), number=10000))
print(timeit(lambda: max_even_seq(99999999999999999999), number=10000))
