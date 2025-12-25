import math

def getmax(coords):
    maxrect = 0
    for i, pos in enumerate(coords):
        x = pos[1]
        y = pos[0]
        for other in coords[i:]:
            xo = other[1]
            yo = other[0]
            rect = (abs(x-xo)+1) * (abs(y-yo)+1)
            if rect > maxrect:
                maxrect = rect
    return maxrect            

def main():
    global coordinates
    coordinates = []
    with open("input9.txt") as file:
        for lines in file:
            l = lines.strip()
            coordinates.append(tuple(int(x) for x in l.split(",")))
    coordinates.sort()
    maxrect = getmax(coordinates)
    print(maxrect)

if __name__ == "__main__":
    main()      