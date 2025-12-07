
def main():
    ranges = []
    fresh = 0

    with open("input5.txt") as f:
        while True:
            line = f.readline()
            if line == '\n':
                break
            parts = line.strip().split('-')
            min = int(parts[0])
            max = int(parts[1])
            ranges.append((min, max))
            #gonna do that ranges always is a pair of start - end range value
        ranges.sort()
        fresh += ranges[0][1] - ranges[0][0] + 1

        for i in range(1, len(ranges)):
            if(ranges[i][0] > ranges[i-1][1]):
                fresh += ranges[i][1] - ranges[i][0] + 1
            elif(ranges[i][1] > ranges[i-1][1]):
                fresh += ranges[i][1] - ranges[i-1][1]
            print(fresh)

        print(fresh)      


                


            
            
if __name__ == "__main__":
    main()