from turtle import Screen, Turtle
from pixart import initialization, draw_shape_from_file

def main():
    screen = Screen()
    turta = Turtle()

    initialization(turta)
    draw_shape_from_file(turta)

    screen.mainloop()

if __name__ == "__main__":
    main()
