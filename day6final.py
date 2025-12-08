def calc():
    global datamatrix, opmatrix
    final = 0
    rows = len(datamatrix) 
    cols = len(datamatrix[0]) 

    cO = len(oplist)-1

    totalmul = 1
    totalsum = 0
    staffstring =''

    for j in range(cols-1, -1, -1):
        if staffstring == '' and (j != (cols-1)):       #means were at next block of calc
            if(oplist[cO] == '*'):
                final += totalmul
            elif(oplist[cO] == '+'):    
                final += totalsum
            totalmul = 1             #reset mul or sum for block
            totalsum = 0
            cO -= 1                  #next operator mul/sum
        staffstring = ''

        for i in range(rows):
            number = datamatrix[i][j]
            if(number != ' '):
                staffstring += number

        if(staffstring != ''):    
            if (oplist[cO] == '*'):
                totalmul *= int(staffstring)
            elif (oplist[cO] == '+'):
                totalsum += int(staffstring)

    return final            

def main():
    global datamatrix, oplist
    datamatrix = []
    oplist = []
    with open("input6.txt") as f:
        lines = f.read().splitlines()
     
    for line in lines[:-1]:
        datamatrix.append(list(line))
    oplist = (list(filter(None, lines[-1].split(' '))))    
    cephalopod = calc()
    print(cephalopod)


if __name__ == "__main__":
    main()    