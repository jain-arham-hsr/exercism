def equilateral(sides):
    return 0 not in sides and len(set(sides)) == 1


def isosceles(sides):
    return 0 not in sides and len(set(sides)) <= 2 and sorted(sides)[0] + sorted(sides)[1] > sorted(sides)[2]


def scalene(sides):
    return 0 not in sides and len(set(sides)) == 3 and sorted(sides)[0] + sorted(sides)[1] > sorted(sides)[2]
