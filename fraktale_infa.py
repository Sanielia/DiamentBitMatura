from turtle import Turtle

def fractal_1_step(number: int, turtle: Turtle, increment: int=100):
    if number == 0:
        turtle.forward(increment)
        return
    turtle.forward(increment//3)
    turtle.left(90)
    for _ in range(2):
        fractal_1_step(number - 1, turtle, increment//3)
        turtle.right(90)
    fractal_1_step(number - 1, turtle, increment//3)
    turtle.left(90)
    turtle.forward(increment//3)


def step(number: int, turtle: Turtle, increment: int=100, angle=90):
    if number == 0:
        for _ in range(4):
            turtle.forward(increment)
            turtle.right(angle)
        return
    turtle.forward(increment)
    step(number - 1, turtle, increment // 3, -angle)
    turtle.right(angle)
    turtle.forward(increment)
    step(number - 1, turtle, increment // 3, -angle)
    turtle.right(angle)
    turtle.forward(increment)
    step(number - 1, turtle, increment // 3, -angle)
    turtle.right(angle)
    turtle.forward(increment)
    step(number - 1, turtle, increment // 3, -angle)
    turtle.right(angle)



if __name__ == "__main__":
    rzuf = Turtle()
    fractal_1_step(3, rzuf)
    rzuf.clear()
    rzuf.setpos(0, 0)
    step(3, rzuf)
