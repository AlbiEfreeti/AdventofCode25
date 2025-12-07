def canforklift(line, i):
    global forklift
    total = 0
    width = len(line)
    height = len(forklift)

    for k in range(width):
        adjacent = 0
        if line[k] != '@':
            continue

        if k + 1 < width and line[k+1] == '@':
            adjacent += 1
        if k - 1 >= 0 and line[k-1] == '@':
            adjacent += 1
        if i - 1 >= 0 and forklift[i-1][k] == '@':
            adjacent += 1
        if i + 1 < height and forklift[i+1][k] == '@':
            adjacent += 1
        if adjacent >= 4:
            continue

        if i - 1 >= 0 and k - 1 >= 0 and forklift[i-1][k-1] == '@':
            adjacent += 1
            if adjacent >= 4:
                continue
        if i - 1 >= 0 and k + 1 < width and forklift[i-1][k+1] == '@':
            adjacent += 1
            if adjacent >= 4:
                continue
        if i + 1 < height and k - 1 >= 0 and forklift[i+1][k-1] == '@':
            adjacent += 1
            if adjacent >= 4:
                continue
        if i + 1 < height and k + 1 < width and forklift[i+1][k+1] == '@':
            adjacent += 1
            if adjacent >= 4:
                continue

        if adjacent < 4:
            forklift[i][k] = '.'
            total += 1

    return total


def main():
    global forklift
    forklift = []
    rolls = 0

    with open("input4.txt") as f:
        for line in f:
            row = list(line.strip())
            forklift.append(row)
            
    finalrolls = 0
    while True:
        for i, l in enumerate(forklift):
            rolls += canforklift(l, i)
        print(rolls)
        finalrolls += rolls  
         
        if rolls == 0:
            print("No more paper rolls can be removed. " + str(finalrolls))
            break
        rolls = 0
    #new forklift matrix updated so Im gonna do from the start
    

if __name__ == "__main__":
    main()
