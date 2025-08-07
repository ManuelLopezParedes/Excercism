def equilateral(sides):
    if not triangle(sides):
        return False
    else:
        if sides[0] == sides[1] and sides[1] == sides[2]:
            return True
        else:
            return False

def isosceles(sides):
    if not triangle(sides):
        return False
    else:
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
        else:
            return False

def scalene(sides):
    if not triangle(sides):
        return False
    else:
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
        else:
            return False

def triangle(sides):
    a,b,c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        return (a + b > c) and (b + c > a) and (a + c > b)