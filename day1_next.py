import math

pos = 50
password = 0

def next_turn(side, num):
    global pos, password

    if side == "R":
        password += (pos + num) // 100
        pos = (pos + num) % 100
        print(pos, password,side, num)
    elif side == "L":
        if(pos - num) < 0 & pos - num < -100:
            password += (((pos - num)*-1) // 100)
        elif (pos - num) < 0 & pos - num > -100:
             password += 1
        pos = (pos - num) % 100
        print(pos, password,side, num)

    if pos == 0:
        password += 1


def main():
    global pos, password
    with open("inputtest.txt") as f:
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
