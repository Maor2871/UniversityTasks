from hw5_318879608 import *
from random import randint

def main():
    test()
    print('Passed naive tester')
    Q2_test()
    Q3_test()
    print("All is well")
    print("i didn't have any ideas for Q4 and Q5, if you do please tell me and i will add them!")

def Q2_test():
    one = FactoredInteger([])

    assert str(one) == "<1:>"

    seven = FactoredInteger([7])
    assert one * seven == seven
    assert seven ** one == seven

    four = FactoredInteger([2, 2])
    two = FactoredInteger([2])
    assert two ** two == four

    ##gcd
    assert four.gcd(seven) == one
    assert four.gcd(two) == two
    assert four.gcd(four) == four


    print("Made it through Q2!")

def Q3_test():
            
    def make_polygon(small, big, clockwize=False):
        """makes a polygon with one point from each quarter, so that it is simple"""
        ## i dont like (0,0)
        assert small != 0 and big != 0
        polygon_points = []
        num = [] 
        for i in range (8):
            num.append(randint(small, big))
        num.sort()
        p = 0
        for i in [1, -1]:
            for j in [-1, 1]:
                z = i*num[2*p]
                z2 = j*num[2*p+1]
                polygon_points.append(Point(z,z2))
                p = p + 1
        
        ## making it simple
        polygon_points[2], polygon_points[3] = polygon_points[3], polygon_points[2]

        if clockwize:
            polygon_points[1], polygon_points[3] = polygon_points[3], polygon_points[1]
        return Polygon(Linked_list(polygon_points))
            
            
            

    top_left = Point(1, 1)
    lower_left = Point(1, -1)
    y = Point(0, 3)
    x = Point(3, 0)
    ## aleph i
    assert abs(x.angle_between_points(y) - 0.5 *math.pi) < 0.001
    assert abs(lower_left.angle_between_points(top_left) - 0.5 * math.pi) < 0.001
    assert abs(top_left.angle_between_points(lower_left) - 1.5 * math.pi) < 0.001
    assert y.angle_between_points(y) == 0


    ## aleph ii
    assert find_optimal_angle([top_left, lower_left], 0.5 * math.pi) == lower_left.theta

    top_right = Point(-1, 1)
    assert find_optimal_angle([top_right, top_left], 0.5 * math.pi) == top_left.theta

    ## beit ii
    square1 = Polygon(Linked_list([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)]))
    assert square1.edges() == [90.0]*4

    square2 = Polygon(Linked_list([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]))
    assert square2.edges() == [90.0]*4

    for _ in range(50):
        counter_poly = make_polygon(1, 10)
        with_poly = make_polygon(1, 10, True)
        ## the sum of the angles og every polygon is 180*(n-2)
        assert abs(sum(counter_poly.edges()) - 360) < 0.1
        assert abs(sum(with_poly.edges()) - 360) < 0.1

    print("Made it through Q3!")


def Q4_test():
    pass

def Q5_test():
    pass

if __name__ == '__main__':
    main()
