pos = 50
password = 0



def next_turn(side, num):
    global pos, password

    for _ in range(num):
        if side == "R":
            pos = (pos + 1) % 100
        else:  
            pos = (pos - 1) % 100

        if pos == 0:
            password += 1
           

def main():
    global pos, password
    with open("input.txt") as f:
        for step in f:
            step = step.strip()
            if not step:
                continue

            side = step[0]
            num = int(step[1:])
            next_turn(side, num)

    print(pos)
    print(password)


if __name__ == "__main__":
    main()
