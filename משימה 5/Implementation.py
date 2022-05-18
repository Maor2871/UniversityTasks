# Skeleton file for HW5 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw5_ID.py).


import random
import math


##############
# QUESTION 1 #
##############


class LLLNode:
    def __init__(self, val):
        self.next_list = []
        self.val = val
    def __repr__(self):
        st = "Value: "+str(self.val)+"\n"
        st += "Neighbors:"+"\n"
        for p in self.next_list:
            st += " - Node with value: "+str(p.val)+"\n"
        return st[:-1]


class LogarithmicLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len
    
    def add(self, val):
        node = LLLNode(val)
        if len(self) == 0:
            self.head = node
            self.len = 1
            return None

        node.next_list.append(self.head)
        p = self.head
        i = 0
        while len(p.next_list) > i:
            node.next_list.append(p.next_list[i])
            p = p.next_list[i]
            i += 1
            
        self.head = node
        self.len += 1
        return None


class LogarithmicLinkedList(LogarithmicLinkedList):
    
    def __contains__(self, val):
        
        p = self.head
        k = 1
        while k!= 0:

            # Great, the value is in the linked list.
            if p.val == val:
                return True

            # Binary search p.next_list, and find the furthest node wich val is greater than.
            left = 0
            right = len(p.next_list) - 1

            # Sector not found yet.
            while left < right:

                # Get the middle.
                m = len(p.next_list) / 2

                # Cut the right edge, val is lower.
                if  p.next_list[m].val <= val:
                    right = m
                
                # Cut the left edge, val is greater.
                else:
                    left = m

            # The value is not in the linked list.
            if m == 0 and val != p.next_list[0]:
                return False

            # val is greater than or equal to p.next_list[m].
            p = p.next_list[m]
        return False


##############
# QUESTION 2 #
##############


def is_sorted(lst):
    """ returns True if lst is sorted, and False otherwise """
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

def modpower(a, b, c):
    """ computes a**b modulo c, using iterated squaring """
    result = 1
    while b > 0:  # while b is nonzero
        if b % 2 == 1:  # b is odd
            result = (result * a) % c
        a = (a * a) % c
        b = b // 2
    return result

def is_prime(m):
    """ probabilistic test for m's compositeness """''
    for i in range(0, 100):
        a = random.randint(1, m - 1)  # a is a random integer in [1...m-1]
        if modpower(a, m - 1, m) != 1:
            return False
    return True


class FactoredInteger:

    def __init__(self, factors, verify=True):
        """ Represents an integer by its prime factorization """
        if verify:
            assert is_sorted(factors)
        number = 1
        for p in factors:
            if verify:
                assert (is_prime(p))
            number *= p
        self.number = number
        self.factors = factors

    # 2b
    def __repr__(self):
        """
            The function returns a string of the object.
        """
        
        return '<' + str(self.number) + ":" + '*'.join([str(prime_num) for prime_num in self.factors]) + '>'

    def __eq__(self, other):
        if self.number == other.number:
            return True
        return False

    def __mul__(self, other):

        # The factors list of the multiplication.
        mul_fact = []
        
        # Index for the self list and index for the other list.
        i, j = 0, 0

        # Insert by order until one list was inserted completly.
        while i < len(self.factors) and j < len(other.factors):

            # Append the lower factor.
            if self.factors[i] <= other.factors[j]:
                mul_fact.append(self.factors[i])
                i += 1
            else:
                mul_fact.append(other.factors[j])
                j += 1

        # Add the rest.
        if i == len(self.factors):
            mul_fact += other.factors[j:]
        else:
            mul_fact += self.factors[i:]

        # Create and return the multiplication.
        return FactoredInteger(factors=mul_fact)
                

    def __pow__(self, other):

        # The factors list of the pow.
        factors = []

        # Iterate over the factors of the base.
        for factor in self.factors:

            # Add other.number instances of the current factor to the pow factors list.
            for i in range(other.number):
                factors.append(factor)

        # Create and return the pow.
        return FactoredInteger(factors=factors)

    # 2c
    def gcd(self, other):

        # Simply Look for common factors in the two numbers factors list.

        # The final list with the factors of the gcd.
        gcd_factors = []
        
        # The index on the other factors list.
        j = 0

        # Iterate over the factors of the current number.
        for i in range(len(self.factors)):

            # No more common factors available.
            if j >= len(other.factors) - 1:
                break
            
            # Greate, append this factor to the gcd factors and make one step further in both lists.
            if self.factors[i] == other.factors[j]:

                gcd_factors.append(self.factors[i])
                j += 1

            # They are different, if the current factor in other is less, move the j index to match the factor of self.
            while j < len(other.factors) and other.factors[j] < self.factors[i]:
                j += 1

        # Now we have the gcd, lets create and return it.
        return FactoredInteger(factors=gcd_factors)

    # 2d
    def lcm(self, others):
        my_set = set()

        # A list of all the factors lists.
        lists = [self.factors] + [x.factors for x in others]
        
        # A list of dictionaries. Each dict is a counter for the factors of a specific factor (it's a dict so key for each factor).
        f_i_d = [{f: 0 for f in x} for x in lists]

        # For each factors dict counter, update the counters to indicate on how many apearences the current factor has in the current factors list.
        for i in range(len(lists)):

            # Iterate over factors in the counter dict.
            for f in lists[i]:

                # Make sure the factor is in the set.
                my_set.add(f)

                # Add one more to the counter.
                f_i_d[i][f] += 1
                
        # A dictionary of the form: {factor: counter}.
        f_m_d = {x: 0 for x in my_set}

        # Iterate again on the counter dicts.
        for f_d in f_i_d:

            # iterate over the factors in the current dict.
            for f in f_d.keys():

                # Update the counter in my set to match the maximum counter of the current factor in all the factors lists. 
                if f_d[f] > f_m_d[f]:
                    f_m_d[f] = f_d[f]

        # Unpack the factors dict to a proper factors list and create and return the lcm.
        result = []
        for k, v in f_m_d.items():
            result += [k] * v
        return FactoredInteger(result, verify=False)


##############
# QUESTION 3 #
##############

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.sqrt(x ** 2 + y ** 2)
        self.theta = math.atan2(y, x)
        if self.theta < 0:
            self.theta += 2 * math.pi

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # 3a_i
    def angle_between_points(self, other):
        pass # replace this with your code


# 3a_ii
def find_optimal_angle(trees, alpha):
    pass  # replace this with your code


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        # return str(self.value)
        # This shows pointers as well for educational purposes:
        return "(" + str(self.value) + ", next: " + str(id(self.next)) + ")"


class Linked_list:
    def __init__(self, seq=None):
        self.head = None
        self.len = 0
        if seq != None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.head
        while p != None:
            out += str(p) + ", "  # str(p) invokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"

    def __len__(self):
        ''' called when using Python's len() '''
        return self.len

    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        self.len += 1

    def find(self, val):
        ''' find (first) node with value val in list '''
        p = self.head
        # loc = 0     # in case we want to return the location
        while p != None:
            if p.value == val:
                return p
            else:
                p = p.next
                # loc=loc+1   # in case we want to return the location
        return None

    def __getitem__(self, loc):
        ''' called when using L[i] for reading
            return node at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self.head
        for i in range(0, loc):
            p = p.next
        return p

    def __setitem__(self, loc, val):
        ''' called when using L[loc]=val for writing
            assigns val to node at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self.head
        for i in range(0, loc):
            p = p.next
        p.value = val
        return None

    def insert(self, loc, val):
        ''' add node with value val after location 0<=loc<len of the list '''
        assert 0 <= loc <= len(self)
        if loc == 0:
            self.add_at_start(val)
        else:
            p = self.head
            for i in range(0, loc - 1):
                p = p.next
            tmp = p.next
            p.next = Node(val)
            p.next.next = tmp
            self.len += 1

    def delete(self, loc):
        ''' delete element at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        if loc == 0:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(0, loc - 1):
                p = p.next
            # p is the element BEFORE loc
            p.next = p.next.next
        self.len -= 1


# for 3b_ii
def calculate_angle(p1, p2, p3):
    ang = math.degrees(math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x))
    return ang + 360 if ang < 0 else ang


class Polygon:
    def __init__(self, llist):
        self.points_list = llist
        self.point_head = llist.head

    # 3b_ii
    def edges(self):
        pass # replace this with your code

    # 3b_iii
    def is_convex(self):
        pass # replace this with your code


##############
# QUESTION 4 #
##############


def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree():

    def __init__(self):
        self.root = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def inorder(self):
        result = []

        def inorder_rec(root):
            if root:
                inorder_rec(root.left)
                result.append((root.key, root.val))
                inorder_rec(root.right)

        inorder_rec(self.root)
        return result

    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    # 4
    def is_q_balanced(self, q):
        pass  # replace this with your code


############
# QUESTION 5
############

# 5a
def prefix_suffix_overlap(lst, k):
    pass  # replace this with your code


# 5c
class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        pass  # replace this with your code


# 5d
def prefix_suffix_overlap_hash1(lst, k):
    pass  # replace this with your code


##########
# TESTER #
##########

def test():
    ##############
    # QUESTION 2 #
    #   TESTER   #
    ##############

    # 2b
    n1 = FactoredInteger([2, 3])  # n1.number = 6
    n2 = FactoredInteger([2, 5])  # n2.number = 10
    n3 = FactoredInteger([2, 2, 3, 5])  # n3.number = 60
    if str(n3) != "<60:2*2*3*5>":
        print("2b - error in __repr__")
    if n1 != FactoredInteger([2, 3]):
        print("2b - error in __eq__")
    if n1 * n2 != n3:
        print("2b - error in __mult__")
    if n1 ** n2 != FactoredInteger([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]):
        print("2b - error in __pow__")

    # 2c
    n4 = FactoredInteger([2, 2, 3])  # n4.number = 12
    n5 = FactoredInteger([2, 2, 2])  # n5.number = 8
    n6 = FactoredInteger([2, 2])  # n6.number = 4
    if n4.gcd(n5) != n6:
        print("2c - error in gcd")

    n7 = FactoredInteger([2, 3])  # n7.number = 6
    n8 = FactoredInteger([5, 7])  # n8.number = 35
    n9 = FactoredInteger([])  # represents 1
    if n7.gcd(n8) != n9:
        print("2c - error in gcd")

    ##############
    # QUESTION 3 #
    #   TESTER   #
    ##############

    # 3a
    p1 = Point(1, 1)  # theta = pi / 4
    p2 = Point(0, 3)  # theta = pi / 2
    if Point.angle_between_points(p1, p2) != 0.25 * math.pi or \
            Point.angle_between_points(p2, p1) != 1.75 * math.pi:
        print("3a_i - error in angle_between_points")

    trees = [Point(2, 1), Point(-1, 1), Point(-1, -1), Point(0, 3), Point(0, -5), Point(-1, 3)]
    if find_optimal_angle(trees, 0.25 * math.pi) != 0.5 * math.pi:
        print("3a_ii - error in find_optimal_angle")

    # 3b
    def test_angles(target, output):
        if len(target) != len(output):
            print("3b_i - error in Polygon.edges")
        for i in range(len(target)):
            if abs(target[i] - output[i]) >= 0.1:  # dealing with floats
                print("3b_i - error in Polygon.edges")

    parallelogram = Polygon(Linked_list([Point(1, 1), Point(4, 4), Point(8, 4),Point(5, 1)]))
    test_angles(parallelogram.edges(), [45.0, 135.0, 45.0, 135.0])
    other_poly = Polygon(Linked_list([Point(1, 1), Point(1, 3), Point(2, 3), Point(3, 1)]))
    test_angles(other_poly.edges(), [90.0, 90.0, 116.5, 63.4])

    not_convex = Polygon(Linked_list([Point(1, 1),Point(8, 1),Point(7, 2),Point(8, 4)]))
    yes_convex = Polygon(Linked_list([Point(1, 1),Point(8, 1),Point(9, 2),Point(8, 4)]))

    if not_convex.is_convex() == True:
        print("3b_ii - error in Polygon.is_convex")
    if yes_convex.is_convex() == False:
        print("3b_ii - error in Polygon.is_convex")


    ##############
    # QUESTION 4 #
    #   TESTER   #
    ##############

    # t1 is balanced for some q
    t1 = Binary_search_tree()
    t1.insert('c', 10)
    t1.insert('b', 10)
    t1.insert('a', 10)
    t1.insert('g', 10)
    t1.insert('e', 10)
    t1.insert('f', 10)
    t1.insert('i', 10)
    t1.insert('h', 10)
    t1.insert('j', 10)
    if t1.is_q_balanced(0.25) != (True, 9):
        print("4 - error in is_q_balanced")
    if t1.is_q_balanced(0.3) != (False, -1):
        print("4 - error in is_q_balanced")

    # t2 is not balanced for any q
    t2 = Binary_search_tree()
    t2.insert('f', 13)
    t2.insert('e', 13)
    t2.insert('c', 13)
    t2.insert('b', 13)
    t2.insert('a', 13)
    t2.insert('g', 13)
    t2.insert('h', 13)
    t2.insert('i', 13)
    t2.insert('j', 13)
    if t2.is_q_balanced(0.1) != (False, -1):
        print("4 - error in is_q_balanced")

    ##############
    # QUESTION 5 #
    #   TESTER   #
    ##############
    # 5a
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap")

    # 5c
    d = Dict(3)
    d.insert("a", 56)
    d.insert("a", 34)
    if sorted(d.find("a")) != sorted([56, 34]) or d.find("b") != []:
        print("error in Dict.find")

    # 5d
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap_hash1(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap_hash1")


class MyTest:
    """
        My tester.
    """

    def __init__(self):

        self.test_2()

    def test_2(self):

        # reper
        num1 = FactoredInteger(factors=[2, 3, 7, 11])
        num2 = FactoredInteger(factors=[])

        if num1.__repr__() != "<462:2*3*7*11>":
            print("reper error 1")

        if num2.__repr__() != "<1:>":
            print("reper error 2")

        # equ
        num1 = FactoredInteger(factors=[2,2,7])
        num2 = FactoredInteger(factors=[2,2,7])
        num3 = FactoredInteger(factors=[])

        if not num1 == num2:
            print("equ error 1")

        if num3 == num1:
            print("equ error 2")

        # mul
        num1 = FactoredInteger(factors=[2, 3, 7])
        num2 = FactoredInteger(factors=[2,3,3])
        num3 = FactoredInteger(factors=[])

        if (num1 * num2).number != 756:
            print("mul error 1")
        if (num3 * num1).number != 42:
            print("mul error 2")
        if (num3 * num3).number != 1:
            print("mul error 3")


        # pow
        num1 = FactoredInteger(factors=[2,3])
        num2 = FactoredInteger(factors=[2,3])
        num3 = FactoredInteger(factors=[])
        num4 = FactoredInteger(factors=[2,2,3])
        num5 = FactoredInteger(factors=[5])

        if (num1 ** num2).number != 46656:
            print("pow error 1")
        if (num1 ** num3).number != 6:
            print("pow error 2")
        if (num4 ** num5).number != 248832:
            print("pow error 3")
        if (num3 ** num3).number != 1:
            print("pow error 4")

        # gcd
        num1 = FactoredInteger(factors=[2,2,2])
        num2 = FactoredInteger(factors=[2,2,3])
        num3 = FactoredInteger(factors=[])
        num4 = FactoredInteger(factors=[2,2,5,5,7,11,11,11])
        num5 = FactoredInteger(factors=[3,3,3,3,7,7,7,11,11,17])

        if num1.gcd(num2).number != 4:
            print("gcd error 1")
        if num2.gcd(num1).number != 4:
            print("gcd error 2")
        if num3.gcd(num4).number != 1:
            print("gcd error 3")
        if num4.gcd(num3).number != 1:
            print("gcd error 4")
        if num3.gcd(num4).number != 1:
            print("gcd error 5")
        if num4.gcd(num5).number != 847:
            print("gcd error 6")

        num1.lcm(others=[num2, num3, num4, num5])


my_test = MyTest()
