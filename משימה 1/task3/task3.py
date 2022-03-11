import time


def zeros(num):
    t0 = time.perf_counter()
    m = num
    cnt = 0
    while m > 0:
        if m % 10 == 0:
            cnt = cnt + 1
        m = m // 10
    t1 = time.perf_counter()
    print("Running time zeros: ", t1-t0, "sec")
    return cnt


def zeros2(num):
    t0 = time.perf_counter()
    cnt = 0
    snum = str(num)
    for digit in snum:
        if digit == "0":
            cnt = cnt + 1
    t1 = time.perf_counter()
    print("Running time zeros2: ", t1-t0, "sec")
    return cnt


def zeros3(num):
    t0 = time.perf_counter()
    cnt = str.count(str(num), "0")
    t1 = time.perf_counter()
    print("Running time zeros3: ", t1-t0, "sec")
    return cnt

num = 1
cnt = 0
print(num)
t0 = time.perf_counter()
for i in range(num):
    cnt = cnt + 1
t1 = time.perf_counter()
print("Running time: ", t1-t0, "sec")
print(((2**1000)/(10**7))*0.75)

"""
# ----- 2**1400 -----

num = 2**1400
print("number: ", "2**1400")
print("zeros:")
zeros(num)
print("zeros2:")
result = zeros2(num)
print(num, "has", result, "zeros")


# ----- 2**600 -----

num = 2**600
print("number: ", "2**600")
print("zeros:")
zeros(num)
print("zeros2:")
result = zeros2(num)
print(num, "has", result, "zeros")


# ----- 2**250 -----

num = 2**250
print("number: ", "2**250")
print("zeros:")
zeros(num)
print("zeros2:")
result = zeros2(num)
print(num, "has", result, "zeros")


# ----- 2**100 -----

num = 2**100
print("number: ", "2**100")
print("zeros:")
zeros(num)
print("zeros2:")
result = zeros2(num)
print(num, "has", result, "zeros")
"""

"""
# ----- 2**1400 -----

num = 2**1400
print("number: ", "2**1400")
result = zeros3(num)
print("2**1400 has", result, "zeros")


# ----- 2**600 -----

num = 2**600
print("number: ", "2**600")
result = zeros3(num)
print("2**600 has", result, "zeros")


# ----- 2**250 -----

num = 2**250
print("number: ", "2**250")
result = zeros3(num)
print("2**250 has", result, "zeros")

# ----- 2**100 -----

num = 2**100
print("number: ", "2**100")
result = zeros3(num)
print("2**100 has", result, "zeros")
"""

"""
zeros(int("1" + ("0"*999)))
zeros(int("1"*1000))
print()
zeros2(int("1" + ("0"*999)))
zeros2(int("1"*1000))
print()
zeros3(int("1" + ("0"*999)))
zeros3(int("1"*1000))
"""
