def calc():
    global datamatrix
    final = 0
    rows = len(datamatrix) - 1
    cols = len(datamatrix[0]) 
    u = len(datamatrix) - 1

    for j in range(cols):
        totalmul = 1
        totalsum = 0
        op = datamatrix[u][j]

        for i in range(rows):
            if (op == '*'):
                totalmul *= datamatrix[i][j]
            elif (op == '+'):
                totalsum += datamatrix[i][j]
        if (op == '*'):
            final += totalmul
        elif (op == '+'):
            final += totalsum    
    return final

def main():
    global datamatrix
    datamatrix = []
    with open("input6.txt") as f:
        lines = f.read().splitlines()
     
    for line in lines[:-1]:
        datamatrix.append(list(line.split(' ')))
    datamatrix.append(list(lines[-1].split(' ')))
    cephalopod = calc()
    print(cephalopod)


if __name__ == "__main__":
    main()    