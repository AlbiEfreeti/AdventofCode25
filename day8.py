import math

def calcdis(tuples):
    global points
    circuitmatrix = []
    used = []
    min = math.inf
    smallestpair = None
    row = 0

    for tuple in points:
        for other in points:
            if tuple != other and (tuple, other) not in used:
                distance = math.dist(tuple, other)
                if distance < min:
                    min = distance
                    smallestpair = (tuple, other)             
    used.append(smallestpair)
    print(used)
    print(min)

    if smallestpair[0] not in circuitmatrix and smallestpair[1] not in circuitmatrix:
            circuitmatrix.append(smallestpair)
    for tupla in circuitmatrix:
        if smallestpair[0] in tupla and smallestpair[1] not in tupla:
            tupla.append(smallestpair)
            tupla.sort()
        elif smallestpair[0] not in tupla and smallestpair[1] in tupla:
            tupla.append(smallestpair)
            tupla.sort()         
        




    return min


def main():
    global points
    points = []
    with open("input8.txt") as f:
        for line in f:
            listline = line.strip()
            points.append(tuple(int(x) for x in listline.split(",")))
    points.sort()
    matrix = calcdis(points)


if __name__ == "__main__":
    main()
