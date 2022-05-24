# Skeleton file for HW5 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw5_ID.py).


import random
import math


# --- Semi functions ---


def points_quicksort(lst):
    """
        The function receives a list of points and returns the list ordered with quicksot, by average time complexity of O(nlogn).
    """
    
    if len(lst) <= 1: 
        return lst
    else:
        pivot = random.choice(lst)
        smaller = [point for point in lst if point.theta < pivot.theta] 
        equal = [point for point in lst if point.theta == pivot.theta]      
        greater = [point for point in lst if point.theta > pivot.theta]

        return points_quicksort(smaller) + equal + points_quicksort(greater)


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
            if j > len(other.factors) - 1:
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
        if self.theta > other.theta:
            return 2 * math.pi - self.theta + other.theta
        return other.theta - self.theta

# 3a_ii
def find_optimal_angle(trees, alpha):

    # If no trees in the forest, my dear bear look were ever you want.
    if not trees:
        return 0

    # If only one tree, return its angle. If the angle is more than 360, no reason to even calculate.
    if len(trees) == 1 or alpha >= 2 * math.pi or alpha == 0:
        return trees[0].theta
    
    # Order the list of trees with quicksort, O(nlogn).
    ordered_trees = points_quicksort(trees)

    # head >= tail.
    head = 1

    # The current max trees combo in alpha angle.
    max_trees_combo = 0
    theta_of_max_combo = trees[0].theta

    # The current combo we are at.
    current_combo = 0

    # Explore new tree each iteration O(n).
    for tail in range(len(ordered_trees)):

        # Add all the trees in the current range.
        while ordered_trees[tail].angle_between_points(ordered_trees[head]) <= alpha:

            # Another valid tree is in range.
            current_combo += 1
            
            # Return to the start of the list (tails hasn't finished yet, the last tree can see the first, second, etc. keep checking).
            if head + 1 >= len(ordered_trees):
                head = 0
        
            # Move to head to the next tree.
            else:
                head += 1

            # Iterated over all the relevant trees.
            if head == tail:
                break

        # Check if the new combo is the max one.
        if current_combo > max_trees_combo:
            max_trees_combo = current_combo
            theta_of_max_combo = ordered_trees[tail].theta

        # The loop will update the tail by one, don't forget to decrease the combo by 1.
        current_combo = max(0, current_combo - 1)

    return theta_of_max_combo


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
        """
            IMPORTANT NOTE: As it is stated in the question, it is not clear if the order of the points of the polygons is clockwise.
                            To get the actulat size of the angles, the order of the points in the linked list should be clockwise.
                            We handle that case at the end of the method with O(n).
        """
        # Maybe im a polygon by defenition, but my points does not have angles.
        if len(self.points_list) <= 2:
            return [0] * len(self.points_list)
        
        # The final list with the edges. The first edge will be calculated at the end of the loop.
        edges = [None]
        
        # current is the edge of the current point we are calculating.
        prev = self.point_head
        current = prev.next
        to = current.next

        # Save the edge of the current point.
        edges.append(calculate_angle(prev.value, current.value, to.value))

        # Keep iteratig as long as there are more vertices, O(n).
        while to.next:           

            # Move to the next point.
            prev = current
            current = to
            to = to.next

            # Save the edge of the current point.
            edges.append(calculate_angle(prev.value, current.value, to.value))

        # Calculate the angle of the last point.
        edges.append(calculate_angle(current.value, to.value, self.point_head.value))

        # Update the angle of the first point.
        edges[0] = calculate_angle(to.value, self.point_head.value, self.point_head.next.value)

        # Make sure that the points of the received polygon are ordered clockwise, O(n).
        if sum(edges) > (len(self.points_list) - 2) * 180 + 0.0001:

            # Update the angles.
            edges = [360 - edge for edge in edges]


        # We have calculated the edges of all the points by order.
        return edges

    # 3b_iii
    def is_convex(self):
        """
            A convex polygon is a polygon which all its interial angles are less than 180, and a concave polygon is one that has at least one interior angle greater than 180.
        """

        # Edges calculates the interior angles of the polygon. Check if one of them is greater than 180.
        for interior_angle in self.edges():

            # That is a concave polygon, not convex.
            if interior_angle > 180:

                return False

        # All interior angles are less than 180, it's a convex polygon.
        return True


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

    def is_q_balanced_count(self, q, count=0):
        
        # --- Initial conditions ---

        # A leaf.
        if not self.left and not self.right:
            return True, count + 1

        # If the right node exists and the left does not:
        if not self.left and self.right:

            # It's a leaf, it's ok.
            if not self.right.right and not self.right.left:
                return True, count + 2

            # Does not match the requirments of a q balanced tree.
            else:
                return False, -1

        # If the left node exists and the right does not.
        if self.left and not self.right:

            # It's a leaf, it's ok.
            if not self.left.left and not self.left.right:
                return True, count + 2

            # Does not match the requirements of a q balanced tree.
            else:
                return False, -1

        # --- Recursive calculations ---
        
        # Calculate the right and left nodes.
        is_left_q_balanced, left_nodes = self.left.is_q_balanced_count(q, count)
        is_right_q_balanced, right_nodes = self.right.is_q_balanced_count(q, count)

        # One of them is not q balanced, therefore the current tree is not q balanced.
        if not is_left_q_balanced or not is_right_q_balanced:
            return False, -1

        # Update the counters calculations.
        left_nodes -= count
        right_nodes -= count
        total_nodes = right_nodes + left_nodes
        
        # The right and left nodes are q balanced each, but the current tree is not balanced on q.
        if not min(left_nodes / total_nodes, right_nodes / total_nodes) >= q:
            return False, -1

        # The current Tree is q balanced indeed.
        return True, total_nodes + 1


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
        """
            O(n), each node is visited once, and the inner calculations are O(1).
        """

        # This "Tree" is not even a tree, it's literally does not exist.
        if not self.root:
            return False, -1
        
        return self.root.is_q_balanced_count(q)
        


############
# QUESTION 5
############

# 5a
def prefix_suffix_overlap(lst, k):

    k_matched = []
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i][:k] == lst[j][-k:]:
                k_matched.append((i, j))

    return k_matched


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

        # Get the index of the current key in the hashtable.
        i = self.hash_mod(key)

        # The same index can match to multiple keys. Therefore we must iterate the list of the current index and extract only the items with the received key.
        return [item[1] for item in self.table[i] if item[0] == key]


# 5d
def prefix_suffix_overlap_hash1(lst, k):

    k_match = []
    
    # We define m to be n because the strings already exist in the memory, it means that their size is handled fine in the current machine.
    d = Dict(len(lst))

    # Let's insert each string to it's right place in the dictionary.
    for i in range(len(lst)):
        d.insert(lst[i][:k], i)

    # Now let's create the list to return.
    for j in range(len(lst)):
        share_key = d.find(lst[j][-k:])
        for i in share_key:
            if i != j:
                k_match.append((i, j))

    return k_match
    


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
        self.test_3()
        self.test_4()
        self.test_5()

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
        num6 = FactoredInteger(factors=[2, 2])
        num7 = FactoredInteger(factors=[2])

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
        if num6.gcd(num7).number != 2:
            print("gcd error 7")

        num1.lcm(others=[num2, num3, num4, num5])

    def test_3(self):

        # --- Points ---
        
        p1 = Point(1, 0.5)
        p2 = Point(1, 1)
        p3 = Point(0, 1)
        p4 = Point(1, 0)
        p5 = Point(-1, -1)
        p6 = Point(1, -1)

        if not (p1.angle_between_points(p2) > 0 and p1.angle_between_points(p2) < 45):
            print("angle_between_points error 1")
        if not (p2.angle_between_points(p1) > 1.5*math.pi and p2.angle_between_points(p1) < 2*math.pi):
            print("angle_between_points error 2")
        if not (p3.angle_between_points(p1) > 0 and p3.angle_between_points(p1) < 45):
            print("angle_between_points error 3")
        if not (p4.angle_between_points(p3) - (math.pi / 2) < 0.001):
            print("angle_between_points error 4")
        if not (p3.angle_between_points(p4) - 1.5 * math.pi < 0.001):
            print("angle_between_points error 5")
        if not (p5.angle_between_points(p6) - math.pi / 2 < 0.001):
            print("angle_between_points error 6")
        if not (p6.angle_between_points(p5) - 1.5 * math.pi < 0.001):
            print("angle_between_points error 7")
        if not (p6.angle_between_points(p6) == 0):
            print("angle_between_points error 8")

        # --- Bear and Trees ---
        trees = [Point(2, 1), Point(-1, 1), Point(-1, -1), Point(0, 3), Point(0, -5), Point(-1, 3)]
        random.shuffle(trees)

        if not find_optimal_angle(trees, 0.25 * math.pi) - 1.5707 < 0.001:
            print("find_optimal_angle error 1")

        trees = [Point(1,1)]
        if not find_optimal_angle(trees, 0.2) - math.pi / 4 < 0.001:
            print("find_optimal_angle error 2")

        trees = []
        if not find_optimal_angle(trees, 0.2) == 0:
            print("find_optimal_angle error 3")

        trees = [Point(2,1),Point(0,3),Point(-1,3), Point(-1,1),Point(-1,-1),Point(0,-5)]

        if not find_optimal_angle(trees, 0) - 0.463 < 0.01:
            print("find_optimal_angle error 4")

        # --- Polygons Party ---

        parallelogram = Polygon(Linked_list([Point(1,1),Point(4,4),Point(8,4),Point(5,1)]))
        parallelogram_rev = Polygon(Linked_list([Point(1,1),Point(4,4),Point(8,4),Point(5,1)][::-1]))

        triangle = Polygon(Linked_list([Point(1,1),Point(4,4),Point(8,4)]))
        triangle_rev = Polygon(Linked_list([Point(1,1),Point(4,4),Point(8,4)][::-1]))

        rectangle = Polygon(Linked_list([Point(1,1),Point(1,-1),Point(-1,-1),Point(-1, 1)]))
        line = Polygon(Linked_list([Point(-10,0),Point(10,0)]))

        not_convex = Polygon(Linked_list([Point(1,1),Point(8,1),Point(7,2),Point(8,4)]))
        not_convex_rev = Polygon(Linked_list([Point(1,1),Point(8,1),Point(7,2),Point(8,4)][::-1]))

        if parallelogram.edges() != [45.0, 135.0, 45.0, 135.0] or parallelogram_rev.edges() != [45.0, 135.0, 45.0, 135.0][::-1]:
            print("edges error 1")
        if triangle.edges() != [21.80140948635181, 135.0, 23.198590513648185] or triangle_rev.edges() != [21.801409486351815, 135.0, 23.198590513648185][::-1]:
            print("edges error 2")
        if rectangle.edges() != [90, 90, 90, 90]:
            print("edges error 3")
        if line.edges() != [0, 0]:
            print("edges error 4")
        if not_convex.edges() != [23.198590513648185, 45.0, 251.56505117707798, 40.23635830927384] or not_convex_rev.edges() != [40.23635830927382, 251.56505117707798, 45.0, 23.19859051364819]:
            print("edges error 5")

        if not parallelogram.is_convex() or not parallelogram_rev.is_convex():
            print("is_convex error 1")
        if not_convex.is_convex() or not_convex_rev.is_convex():
            print("is_convex error 2")
        if not triangle.is_convex or not triangle_rev.is_convex():
            print("is_convex error 3")

    def test_4(self):
        
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
            print("is_q_balanced error 1")
        if t1.is_q_balanced(0.3) != (False, -1):
            print("is_q_balanced error 2")

        t1 = Binary_search_tree()
        if t1.is_q_balanced(0.25) != (False, -1):
            print("is_q_balanced error 3")

    def test_5(self):

        result = prefix_suffix_overlap(["a"*10, "b"*4 + "a"*6, "c"*5 + "b"*4 + "a"], 5)
        expected = [(0, 1), (1, 2)]
        self.prefix_check(result, expected, 1)

        result = prefix_suffix_overlap(["a"*10, "b"*4 + "a"*6, "c"*5 + "b"*4 + "a"], 8)
        expected = []
        self.prefix_check(result, expected, 1)

        d = Dict(5)
        d.insert("abcd", 3)
        d.insert("dead", 5)
        for i in range(4): d.insert("degc", 12 + i * 3)

        if d.find("qwer"):
            print("find error 1")

        self.prefix_check(result=d.find("degc"), expected=[12, 15, 18, 21], error_num=2)

        if d.find("abcd") != [3]:
            print("find error 3")

        result = prefix_suffix_overlap_hash1(["a"*10, "b"*4 + "a"*6, "c"*5 + "b"*4 + "a"], 5)
        expected = [(0, 1), (1, 2)]
        self.prefix_check(result, expected, 1)

        result = prefix_suffix_overlap_hash1(["a"*10, "b"*4 + "a"*6, "c"*5 + "b"*4 + "a"], 8)
        expected = []
        self.prefix_check(result, expected, 1)

    def prefix_check(self, result, expected, error_num):

        for pair in expected:
            if pair not in result:
                print("prefix_check not in result error " + str(error_num) + ":", pair)
                break
        for pair in result:
            if pair not in expected:
                print("prefix_check not in expected error " + str(error_num) + ":", pair)
                break
