def beams():
    global datamatrix, beamstart
    pos = beamstart
    rows = len(datamatrix)
    col = len(datamatrix[0])
    splits = 0
    nomodif = 0
    for i in range(rows):
        if i == rows - 1:
            break
        for j in range(col):
            if datamatrix[i][j] == '^' and datamatrix[i-1][j] == '|':
                datamatrix[i][j-1] = '|' 
                datamatrix[i][j+1] = '|'
                splits += 1
            elif datamatrix[i-1][j] == '|':
                datamatrix[i][j] = '|'   
            elif datamatrix[i][j] == '.':
                nomodif += 1
    print(nomodif)            
    return splits                 


        


def main():
    global datamatrix, beamstart
    datamatrix = []
    with open("input7.txt") as f:
        for lines in f:
            datamatrix.append(list(lines.strip()))
        beamstart = datamatrix[0].index('S')    
        datamatrix[1][beamstart] = '|'
    total = beams()
    print(total)



if __name__ == "__main__":
    main()    