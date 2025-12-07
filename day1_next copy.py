import turtle 
import time

t = turtle.Turtle()
t.hideturtle()
t.penup()

radius = 150

pos = 50
password = 0

def draw_dial():
    for i in range(100):
        angle = (i / 100) * 360
        t.setheading(angle)
        t.goto(0, 0)
        t.forward(radius + 20)
        t.write(str(i), align="center", font=("Arial", 6, "normal"))

    t.goto(0, -radius - 50)
    

draw_dial()

arrow = turtle.Turtle()
arrow.color("blue")
arrow.shape("triangle")
arrow.penup()

def update_arrow(pos):
    angle = (pos / 100) * 360
    arrow.setheading(angle)
    arrow.goto(0, 0)
    arrow.forward(radius)
    time.sleep(0.02)

def next_turn(side, num):
    global pos, password

    for _ in range(num):
        if side == "R":
            pos = (pos + 1) % 100
        else:  
            pos = (pos - 1) % 100

        if pos == 0:
            password += 1
            arrow.color("red")
        else: 
            arrow.color("blue")

        update_arrow(pos)

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
