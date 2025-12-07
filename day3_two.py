def bankvalue(bank, queue):
    result = ""
    start = 0
    n = len(bank)

    for _ in range(queue):
        end = n - (queue - len(result)) + 1
        best_digit = max(bank[start:end])
        best_index = bank.index(best_digit, start, end)
        result += best_digit
        start = best_index + 1

    return int(result)


def main():
    total_joltage = 0
    with open("input3.txt") as f:
        for line in f:
            bank = line.strip()
            total_joltage += bankvalue(bank, 12)

    print("Max joltaje total:", total_joltage)


if __name__ == "__main__":
    main()
