# Skeleton file for HW6 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw6_ID.py).
from PIL import Image  # need to install PIL/PILLOW
import math

# Q1b
def sets_concat(s1, s2):
    s = set()
    for x in s1:
        for y in s2:
            s.add(x+y)
    return s


def generate_language(rule_dict, start_var, k):
    mem = dict()
    return generate_language_rec(rule_dict, start_var, k, mem)


def generate_language_rec(rule_dict, var, k, mem):
    if (var, k) in mem:
        return mem[(var, k)]

    s = set()
    if k == 0:
        if "" in rule_dict[var]:
            s.add("")
        mem[(var, k)] = s
        return s

    if k == 1:
        for var_rule in rule_dict[var]:
            if len(var_rule) == 1:
                s.add(var_rule)
        mem[(var, k)] = s
        return s

    for var_rule in rule_dict[var]:
        if len(var_rule) == 2:
            X, Y = var_rule[0], var_rule[1]
            for j in range(1, k):
                s = s.union(sets_concat(generate_language_rec(rule_dict, X, j, mem), generate_language_rec(rule_dict, Y, k - j, mem)))
    mem[(var, k)] = s
    return s

# Q1c
def what(rule_dict, start_var, k):
    mem = dict()
    return what_rec(rule_dict, start_var, k, mem)


def what_rec(rule_dict, var, k, mem):
    if (var, k) in mem:
        return mem[(var, k)]

    cnt = 0
    if k == 0:
        if "" in rule_dict[var]:
            cnt += 1
        mem[(var, k)] = cnt
        return cnt

    if k == 1:
        for x in rule_dict[var]:
            if len(x) == 1:
                cnt += 1
        mem[(var, k)] = cnt
        return cnt

    for var_rule in rule_dict[var]:
        if len(var_rule) == 2:
            X, Y = var_rule[0], var_rule[1]
            for j in range(1, k):
                cnt += what_rec(rule_dict, X, j, mem) * what_rec(rule_dict, Y, k - j, mem)
    mem[(var, k)] = cnt
    return cnt


# Q2a
def gen1():
   
    k = 0
    yield (0, 0)
    
    while True:

        k += 1
        
        yield (0, k)
        yield (0, -k)
        yield (k, 0)
        yield (-k, 0)
        
        for i in range(1, k):

            # Yield all the tuples with k/-k on the left, up to k/-k on the right.
            yield (k, i)
            yield (k, -i)
            yield (-k, i)
            yield (-k, -i)

            # Yield all the tuples when in the left all the numbers up to k/-k and on the right k/-k.
            yield (i, k)
            yield (i, -k)
            yield (-i, k)
            yield (-i, -k)    

# Q2b
def gen2(g):

    # a1 + a2 + ... + an.
    sum = 0

    while True:
        sum += next(g)
        yield sum

# Q2c
def gen3(g):
    pass  # replace this with your code (or don't, if there does not exist such generator with finite delay)

# Q2d
def gen4(rules_dict, start_var):
    """
        COMPLEXITY NOTE: I didn't want to overcomplicate things, but note that the current implementation does not use the memoization that already exists for all the previous k's.
                         To use the memoization, it is simply required to return "generate_language_rec(rule_dict, start_var, k, mem), mem" and call generate_language_rec with
                         the returned mem at the next call with the new k.
    """
    
    # The length of the current strings.
    k = 0
    
    # Iterate over the lengths of the strings in the language.
    while True:

        # There is a finite amount of string of length k in the language.
        for string in generate_language(rules_dict, start_var, k):
            yield string

        # Move to the next set of strings.
        k += 1


# Q2e
def gen5(g1, g2):
    pass  # replace this with your code (or don't, if there does not exist such generator with finite delay)

# Q3b
def repetition_threshold(W, L):
    """
        Note: if W and L are very large numbers and very close to 2 to the power of a natural number, you might not receive the accurate expected threshold becuase of the floating point problem.
              Therefore, it is advised to enter values of the form 2 ** k - 1.
    """
    return math.ceil((math.ceil(math.log(W, 2)) + math.ceil(math.log(L, 2)) + 1) / 8)

# Q3c

def maxmatch(T, p, W=2 ** 12 - 1, L=2 ** 5 - 1):
    assert isinstance(T, str)
    n = len(T)
    m = 0
    k = 0
    for offset in range(1, 1 + min(p, W)):
        match_len = 0
        j = p - offset
        while match_len < min(n - p, L) and T[j + match_len] == T[p + match_len]:
            match_len += 1
        if match_len > k:
            k = match_len
            m = offset
    return m, k

# Modify this code #
def LZW_compress_v2(text, c, W=2 ** 12 - 1, L=2 ** 5 - 1):
    intermediate = []
    n = len(text)
    p = 0

    # Calculate the number of bits required to add a repetition.
    repetition_bits = math.ceil(math.log(W, 2)) + math.ceil(math.log(L, 2)) + 1

    while p < n:
        m, k = maxmatch(text, p, W, L)

        # Calculate the number of bits required to add the huffman code of the current repetition. If k=0 huffman bits is 0.
        huffman_bits = sum([len(c[letter]) + 1 for letter in text[p - m: p - m + k]])

        if huffman_bits <= repetition_bits:
            intermediate.append(text[p])
            p += 1
        else:
            intermediate.append([m, k])
            p += k
    return intermediate

# Modify this code #
def inter_to_bin_v2(intermediate, c, W=2 ** 12 - 1, L=2 ** 5 - 1):
    W_width = math.floor(math.log(W, 2)) + 1
    L_width = math.floor(math.log(L, 2)) + 1
    bits = []
    for elem in intermediate:
        if type(elem) == str:
            bits.append("0")
            bits.append(c[elem])
        else:
            bits.append("1")
            m, k = elem
            bits.append((bin(m)[2:]).zfill(W_width))
            bits.append((bin(k)[2:]).zfill(L_width))
    return "".join(ch for ch in bits)

# Modify this code #
def bin_to_inter_v2(bits, htree, W=2 ** 12 - 1, L=2 ** 5 - 1):
    W_width = math.floor(math.log(W, 2)) + 1
    L_width = math.floor(math.log(L, 2)) + 1
    inter = []
    n = len(bits)
    p = 0
    while p < n:
        if bits[p] == "0":
            p += 1
            node = htree
            while not type(node) is str:
                node = node[int(bits[p])]
                p+=1
            inter.append(node)
        elif bits[p] == "1":
            p += 1
            m = int(bits[p:p + W_width], 2)
            p += W_width
            k = int(bits[p:p + L_width], 2)
            p += L_width
            inter.append([m, k])
    return inter

# This does not require any changes #
def LZW_decompress(intermediate):
    text_lst = []
    for i in range(len(intermediate)):
        if type(intermediate[i]) == str:
            text_lst.append(intermediate[i])
        else:
            m, k = intermediate[i]
            for j in range(k):
                text_lst.append(text_lst[-m])
    return "".join(text_lst)

# Q5a
def right_left(img):
    w, h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()

    # Add your code here #
    for x in range(w):
        for y in range(h):
            new_mat[x, y] = mat[w - x - 1, y]
            
    return new_img


# Q5b
def what2(img):
    w, h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()

    for y in range(h):
        row_values_ordered = [(mat[x, y], x) for x in range(w)]
        row_values_ordered.sort(key=lambda x: x[0])
        for x in range(w):
            new_mat[x, y] = row_values_ordered[x][0]

    return new_img

############
#  TESTER  #
############
def test():
    # Q1b
    rule_dict = {"S": {"AB", "BC"}, "A": {"BA", "a"}, "B": {"CC", "b"}, "C": {"AB", "a"}}
    res = generate_language(rule_dict, "S", 5)

    if ("baaba" not in res) or ("baab" in res) or ("babab" in res):
        print("Error in Q1b - generate_language")

    # Q3b
    if repetition_threshold(2**12-1, 2**5-1) != 3:
        print("Error in Q3b - repetition_threshold")

    # Q3c
    c = {'a': '0', 'b': '10', 'c': '110', 'd': '1110', 'e': '1111'}
    if LZW_compress_v2("abcdeabccde", c, 2**5-1, 2**3-1) != ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', [6, 3]] or \
        LZW_compress_v2("ededaaaaa", c, 2**5-1, 2**3-1) != ['e', 'd', [2, 2], 'a', 'a', 'a', 'a', 'a']:
        print("Error in Q3c - LZW_compress_v2")
    if inter_to_bin_v2(['e', 'd', [2, 2]], c, 2**5-1, 2**3-1) != "0111101110100010010":
        print("Error in Q3c - inter_to_bin_v2")
    htree = ('a', ('b',('c',('d', 'e'))))  # This is the huffman tree corresponding to the c defined previously
    if bin_to_inter_v2("0111101110100010010", htree, 2**5-1, 2**3-1) != ['e', 'd', [2, 2]]:
        print("Error in Q3c - bin_to_inter_v2")

def my_test():

    # --- Q 1 ---

    # -- b

    rule_dict = {"S": {"AB", "BC"}, "A": {"BA", "a"}, "B": {"CC", "b"}, "C": {"AB", "a"}}
    res = generate_language(rule_dict, "S", 5)
    if ("baaba" not in res) or ("baab" in res) or ("babab" in res):
        print("Error in Q1b - generate_language")

    # --- Q 2 ---

    # -- a

    z_gen = gen1()
    z_list = []
    for i in range(9999):
        z_list.append(next(z_gen))
    if len(z_list) != len(set(z_list)):
        print("gen1 duplicates error")
    if i in range(100):
        for j in range(100):
            if (i, j) not in z_list or (-i, j) not in z_list or (i, -j) not in z_list or (-i, -j) not in z_list:
                print("gen1 error, not in generator:", i, j)

    # -- b
    
    def series():
        i = 1
        while True:
            yield i
            i += 2
    ser1 = series()
    ser1_list = []
    for i in range(100):
        ser1_list.append(next(ser1))
    ser1_sum = gen2(series())
    for i in range(100):
        if next(ser1_sum) != sum(ser1_list[:i + 1]):
            print("gen2 error:", next(ser1_sum), sum(ser1_list[:i + 1]))

    # --- Q 3 ---

    # -- b
    if repetition_threshold(W=2**12-1, L=2**5-1) != 3:
        print("repetition threshold error 1")
    if repetition_threshold(W=2**12, L=2**5-1) != 3:
        print("repetition threshold error 2")
    if repetition_threshold(W=2**19-1, L=2**5-1) != 4:
        print("repetition threshold error 3")

    # -- c

    # - i
    
    c = {'a':'0', 'b':'10', 'c':'110', 'd':'1110', 'e':'1111'}
    if LZW_compress_v2("abcdeabccde", c, 2**5-1, 2**3-1) != ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', [6, 3]]:
        print("LZW_compress_v2 error 1")

    if LZW_compress_v2("ededaaaaa", c, 2**5-1, 2**3-1) != ['e', 'd', [2, 2], 'a', 'a', 'a', 'a', 'a']:
        print("LZW_compress_v2 error 2")

    # - ii

    c = {'a':'0', 'b':'10', 'c':'110', 'd':'1110', 'e':'1111'}
    if inter_to_bin_v2(['e', 'd', [2, 2]], c, 2**5-1, 2**3-1) != "0111101110100010010":
        print("inter_to_bin_v2 error 1")
       
    # - iii

    htree = ('a', ('b',('c',('d', 'e'))))
    if bin_to_inter_v2("0111101110100010010", htree, 2**5-1, 2**3-1) != ['e', 'd', [2, 2]]:
        print("bin_to_inter error 1")

    # - iv

    c = {'b': '1', 'c': '10', 'a': '110'}
    text1 = 'a'
    text2 = 'bc'
    if inter_to_bin_v2(LZW_compress_v2(text1, c), c) ==  inter_to_bin_v2(LZW_compress_v2(text2, c), c):
        print("3 iv claim a' error")

    c = {'b': '10', 'c': '110', 'a': '111'}
    text1 = 'ab'
    text2 = 'cb'
    if inter_to_bin_v2(LZW_compress_v2(text1, c), c) ==  inter_to_bin_v2(LZW_compress_v2(text2, c), c):
        print("3 iv claim b' error")

    # --- Q 5 ---
    
    right_left(img=Image.open("./the-simpsons.jpg")).show()
    what2(img=Image.open("./eiffel-tower.jpg").convert('L')).show()

my_test()
test()
