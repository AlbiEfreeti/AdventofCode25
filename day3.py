def bankvalue(bank):
    best = 0
    n = len(bank)
    for i in range(n):
        for j in range(i + 1, n):
            val = int(bank[i] + bank[j])
            if val > best:
                best = val
    return best


def main():
    maxjol = 0
    with open("input3.txt") as f:
        for line in f:
            bank = line.strip()
            maxjol += bankvalue(bank)
    print("Max joltaje total:", maxjol)


if __name__ == "__main__":
    main()
