from answers import *
from itertools import combinations_with_replacement as cwr
from itertools import permutations
import random

def main():
    test_it()
    

def test_it():
    test_Q2()
    test_Q3()
    test_Q4()
    test_Q5()
    print('All rights preserved for JY.inc')
    

def test_Q2():
    def get_oct_num(length):
        return ''.join([str(random.randint(0, 7)) for _ in range(length)])
    ## vav
    assert oct_to_fraction('000000000000') == 0
    assert oct_to_fraction('200000000000') == 1/4
    assert abs(oct_to_fraction('202207000000') - 0.254421234130859) <= 0.00000001
    assert abs(oct_to_fraction('202207060050') - 0.254421592) <= 0.000001
    for _ in range(50):
        assert 0 <= oct_to_fraction(get_oct_num(12)) <= 1
    
    ## zain
    assert oct_to_float('0000000000000000') == 0
    assert abs(oct_to_float('0400621000000000') -  51.859375) <= 0.00001
    for _ in range(50):
        the_checker = str(random.randint(0,1)) + get_oct_num(15)
        assert type(oct_to_float(the_checker)) is float


    ## heit
    assert is_greater_equal('0400621000000000','0400621000000000')
    assert is_greater_equal('1400621000000000','1400621000000000')
    assert not is_greater_equal('1400621000000000','0400621000000000')
    assert is_greater_equal('0400621000000000', '0000621777700000')
    assert not is_greater_equal('1400621000000000', '1000621777700000')

    print('you passed Q2')

def test_Q3():
    ##aleph
    for num in range(1, 100):
        seq, sqrt_num = approx_root(num, 0.01)
        assert abs(sqrt_num - math.sqrt(num)) <= 0.01

    assert [approx_root(num, 0.01) for num in range(1, 100)] == roots

    ##beit
    if abs(approx_e(1000000) - math.e) > 0.01:
        print("MOST LIKELY there's an error in approx_e (this is a probabilistic test)")
    
    print("you passed Q3")

def test_Q4():
    def make_almost(sorted_lst):
        almost_sorted_lst = []
        switch = True
        for i in range(len(sorted_lst)):
            if switch:
                almost_sorted_lst.append(sorted_lst[i+1])
                switch = False
            else:
                almost_sorted_lst.append(sorted_lst[i-1])
                switch = True
        return almost_sorted_lst

    # Q4 - C
    def the_real_test():
        L = [0, 0, 0, 1, 1, 1, 1]
        
        def q_g(m):
            size = 0
            for i in range(n): 
                if L[i]>m: size +=1
            return size
        
        def q_l(m):
            size = 0
            for i in range(n): 
                if L[i]<m: size +=1
            return size

        return q_l, q_g
        
    ##part 1
    ##aleph
    the_tricks = [[1, 3, 2, 4, 9, 6, 22], [2, 1, 4, 3, 6, 5, 8, 7]]
    for the_trick in the_tricks:
        for i, num in enumerate(the_trick):
            assert find(the_trick, num) == i
        assert find(the_trick, 10) is None
        assert find(the_trick, -1) is None

    ## beit
    sorted_lst = list(range(100))
    almost_sorted_lst = make_almost(sorted_lst)
    assert sort_from_almost(almost_sorted_lst) == sorted_lst

    almost_sorted_lst = [1, 2, 3, 4, 7, 6]
    assert sort_from_almost(almost_sorted_lst) == sorted(almost_sorted_lst)

    ##part 2
    ## you might get into an infinite loop
    n = 7
    q_l, q_g = the_real_test()
    M = compute_median(q_l, q_g, 2, n)
    assert (q_l(M) <= math.ceil(n/2)) and (q_g(M) <= math.ceil(n/2))
    assert type(M) is int
    
    for k in range(1, 10):
        for n in range(50, 150):
            q_l, q_g = generate_queries(k, n)
            M = compute_median(q_l, q_g, k, n)
            assert (q_l(M) <= math.ceil(n/2)) and (q_g(M) <= math.ceil(n/2))
            assert type(M) is int

    print("you passed Q4")

def test_Q5():
    ## aleph
    def set_combis(k):
        letters = ['a', 'b', 'c', 'd', 'e']
        combis = cwr(letters, k)
        words = []
        for comb in combis:
            pers = permutations(comb)
            for per in pers:
                words.append(''.join(per))
        words = set(words)
        return sorted(list(set(words)))

    ## gimmel
    for k in range(4):
        for n, comb in enumerate(set_combis(k)):
            assert string_to_int(comb) == n
            assert int_to_string(k, n) == comb
            

    ## hei
    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    assert sort_strings1(lst1, 4) == sorted(lst1)
    
    for k in range(1, 4):
        combis = set_combis(k)
        shuffled = combis[:]
        random.shuffle(shuffled)
        assert sort_strings1(shuffled, k) == combis
        assert sort_strings2(shuffled, k) == combis
    
    
    print("you passed Q5")
        



roots = [([1], 1.0), ([1, 3, 5, 5], 1.4133333333333333), ([1, 2, 3, 3], 1.7222222222222223), ([1, 1], 2.0), ([1, 1, 5, 6], 2.2333333333333334), ([1, 1, 3, 3], 2.4444444444444446), ([1, 1, 2, 4, 7], 2.642857142857143), ([1, 1, 2, 2, 4, 4], 2.828125), ([1, 1, 1], 3.0), ([1, 1, 1, 7, 8], 3.1607142857142856), ([1, 1, 1, 4, 4], 3.3125), ([1, 1, 1, 3, 3, 6], 3.4629629629629632), ([1, 1, 1, 2, 5], 3.6), ([1, 1, 1, 2, 3, 3, 3], 3.7407407407407405), ([1, 1, 1, 2, 2, 3, 3, 3], 3.8703703703703702), ([1, 1, 1, 1], 4.0), ([1, 1, 1, 1, 9, 10], 4.122222222222222), ([1, 1, 1, 1, 5, 5], 4.24), ([1, 1, 1, 1, 3, 14], 4.357142857142857), ([1, 1, 1, 1, 3, 3, 5], 4.466666666666666), ([1, 1, 1, 1, 2, 7, 7], 4.581632653061225), ([1, 1, 1, 1, 2, 3, 8], 4.6875), ([1, 1, 1, 1, 2, 2, 6], 4.791666666666667), ([1, 1, 1, 1, 2, 2, 2, 6], 4.895833333333333), ([1, 1, 1, 1, 1], 5.0), ([1, 1, 1, 1, 1, 11], 5.090909090909091), ([1, 1, 1, 1, 1, 6, 6], 5.194444444444445), ([1, 1, 1, 1, 1, 4, 7], 5.285714285714286), ([1, 1, 1, 1, 1, 3, 7], 5.3809523809523805), ([1, 1, 1, 1, 1, 3, 3, 4], 5.472222222222221), ([1, 1, 1, 1, 1, 2, 8], 5.5625), ([1, 1, 1, 1, 1, 2, 4, 4], 5.65625), ([1, 1, 1, 1, 1, 2, 3, 3, 3], 5.7407407407407405), ([1, 1, 1, 1, 1, 2, 2, 4, 4], 5.828125), ([1, 1, 1, 1, 1, 2, 2, 2, 4], 5.90625), ([1, 1, 1, 1, 1, 1], 6.0), ([1, 1, 1, 1, 1, 1, 13], 6.076923076923077), ([1, 1, 1, 1, 1, 1, 7, 7], 6.163265306122449), ([1, 1, 1, 1, 1, 1, 5, 5], 6.24), ([1, 1, 1, 1, 1, 1, 4, 4, 6], 6.322916666666667), ([1, 1, 1, 1, 1, 1, 3, 5], 6.3999999999999995), ([1, 1, 1, 1, 1, 1, 3, 3, 4], 6.472222222222221), ([1, 1, 1, 1, 1, 1, 2, 9], 6.555555555555555), ([1, 1, 1, 1, 1, 1, 2, 4], 6.625), ([1, 1, 1, 1, 1, 1, 2, 3, 5], 6.7), ([1, 1, 1, 1, 1, 1, 2, 2, 8], 6.78125), ([1, 1, 1, 1, 1, 1, 2, 2, 3, 4], 6.854166666666666), ([1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4], 6.927083333333334), ([1, 1, 1, 1, 1, 1, 1], 7.0), ([1, 1, 1, 1, 1, 1, 1, 15], 7.066666666666666), ([1, 1, 1, 1, 1, 1, 1, 8, 8], 7.140625), ([1, 1, 1, 1, 1, 1, 1, 5, 19], 7.2105263157894735), ([1, 1, 1, 1, 1, 1, 1, 4, 9], 7.277777777777778), ([1, 1, 1, 1, 1, 1, 1, 3, 23], 7.3478260869565215), ([1, 1, 1, 1, 1, 1, 1, 3, 5, 5], 7.413333333333333), ([1, 1, 1, 1, 1, 1, 1, 3, 3, 3], 7.481481481481481), ([1, 1, 1, 1, 1, 1, 1, 2, 11], 7.545454545454546), ([1, 1, 1, 1, 1, 1, 1, 2, 5, 7], 7.614285714285714), ([1, 1, 1, 1, 1, 1, 1, 2, 3, 12], 7.680555555555556), ([1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3], 7.7407407407407405), ([1, 1, 1, 1, 1, 1, 1, 2, 2, 5, 5], 7.81), ([1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3], 7.87037037037037), ([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3], 7.930555555555556), ([1, 1, 1, 1, 1, 1, 1, 1], 8.0), ([1, 1, 1, 1, 1, 1, 1, 1, 17], 8.058823529411764), ([1, 1, 1, 1, 1, 1, 1, 1, 9, 9], 8.123456790123456), ([1, 1, 1, 1, 1, 1, 1, 1, 6, 9], 8.185185185185185), ([1, 1, 1, 1, 1, 1, 1, 1, 5, 5], 8.239999999999998), ([1, 1, 1, 1, 1, 1, 1, 1, 4, 5], 8.3), ([1, 1, 1, 1, 1, 1, 1, 1, 3, 11], 8.363636363636365), ([1, 1, 1, 1, 1, 1, 1, 1, 3, 4], 8.416666666666668), ([1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3], 8.481481481481481), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 12], 8.541666666666666), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 5], 8.6), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 4], 8.65625), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4], 8.708333333333332), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 11], 8.772727272727273), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 4, 4], 8.828125), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 10], 8.8875), ([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2], 8.9375), ([1, 1, 1, 1, 1, 1, 1, 1, 1], 9.0), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 19], 9.052631578947368), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10], 9.11), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7], 9.16326530612245), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 11], 9.218181818181817), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 11], 9.272727272727273), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 5], 9.325), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 8], 9.375), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 5], 9.433333333333335), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3], 9.481481481481481), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 13], 9.538461538461538), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6], 9.583333333333334), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 7], 9.642857142857142), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 6], 9.694444444444445), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3], 9.74074074074074), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 6], 9.791666666666666), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 6], 9.847222222222223), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 6], 9.895833333333334), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 6], 9.947916666666666)]

    
        
            
        

    

    
    
    












if __name__ == '__main__':
    main()
