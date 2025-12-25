#backtracking with DFS 
def drawcamino():
    global datamatrix, numcaminos, beamstart
    for i in range(rows):
        if i == rows - 1:
            numcaminos += 1
        for j in range(col):
            if datamatrix[i][j] == '^' and datamatrix[i-1][j] == '|' and datamatrix[i][j-1] == '.':
                datamatrix[i][j-1] = '|' 
                break
            elif datamatrix[i][j] == '^' and datamatrix[i-1][j] == '|' and datamatrix[i][j+1] == '.':
                datamatrix[i][j+1] = '|'
                break
            elif datamatrix[i-1][j] == '|' and datamatrix[i][j] == '.':
                datamatrix[i][j] = '|'
                if i == rows - 2:
                    datamatrix[i+1][j] = '|'
                break 
               


        


def main():
    global datamatrix, beamstart, numcaminos, rows, col
    datamatrix = []
    with open("test7.txt") as f:
        for lines in f:
            datamatrix.append(list(lines.strip()))
        beamstart = datamatrix[0].index('S')    
        datamatrix[1][beamstart] = '|'

    rows = len(datamatrix)
    col = len(datamatrix[0])
    numcaminos = 0
    while(True):
        for k in range(col):
            if datamatrix[rows-1][k] == '|':
                for back in range(rows, -1, -1):
                    
                    
    drawcamino()





if __name__ == "__main__":
    main()    