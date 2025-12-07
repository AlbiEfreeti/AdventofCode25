def fallsID(id):
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            return True
    return False



def main():
    ids = []
    global ranges
    ranges = []

    with open("input5.txt") as f:
        while True:
            line = f.readline()
            if line == "\n":
                break
            parts = line.strip().split('-')
            min = int(parts[0])
            max = int(parts[1])
            ranges.append((min, max))
            #gonna do that ranges always is a pair of start - end range value
        print(ranges)

        while True:
            line = f.readline()
            if not line:
                break
            id = int(line.strip())
            valid = False
            ids.append(id)    
        print(ids)

        fresh = 0
        for id in ids:
            if(fallsID(id) == True):
                fresh += 1

        print("Number productos fresh: ", fresh)        
            
if __name__ == "__main__":
    main()