from turtle import Screen, Turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    turta.speed(35) # setting pen speed to 35.
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) # initial coordinates
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)


"""This function will return the color according to the respective color code, if invalid value entered, it will return nothing."""
def get_color(color_code): 
    if color_code == '0':
        return 'black'
    elif color_code == '1':
        return 'white'
    elif color_code == '2':
        return 'red'
    elif color_code == '3':
        return 'yellow'
    elif color_code == '4':
        return 'orange'
    elif color_code == '5':
        return 'green'
    elif color_code == '6':
        return 'yellowgreen'
    elif color_code == '7':
        return 'sienna'
    elif color_code == '8':
        return 'tan'
    elif color_code == '9':
        return 'gray'
    elif color_code == 'A':
        return 'darkgray'
    else:
        return None


"""this function will take the color name and make a pixel according to that."""
def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string) #choosing the fill color
    turta.begin_fill() 

    for i in range(4): #a for loop is used inorder to create a perfect pixel which has the shape of a square. 4 is because of the number of sides in a square.
        turta.forward(PIXEL_SIZE)
        turta.right(90)
    turta.end_fill()

"""this function will take color code and make a pixel according to that, if invalid color is entered it will give the respective output."""
def draw_pixel(color_string, turta):
    color = get_color(color_string) #storing the return value of the function into the variable in order to print the appropriate color pixel.
    if color:
        draw_color_pixel(color, turta) #the color variable is then sent to the function which creates the pixel.
    else:
        print("Error: Invalid color, Cannot draw pixel.")

"""A color string is given here, the function iterates over each character and draws the pixel with the appropriate color. """
def draw_line_from_string(color_string, turta):
    try:
        for char in color_string:
            color = get_color(char)
            if color is None:
                print("Invalid Color Code on" ,char,  "in the string", color_string)
                return False
            
            draw_pixel(char, turta)
            turta.penup()
            turta.forward(PIXEL_SIZE)
            turta.pendown()

        return True

    except Exception as error:
        print("An error occurred:", error)
        return False

"""This Function draws a grid by creating horizontal and vertical lines, forming a grid of squares.
    The grid size is based on the number of rows and columns given in the initial file.
    The distance between each line is determined by the PIXEL_SIZE constant. """

def draw_grid(turta):
    for row in range(ROWS):
        color_string = ''
        for col in range(COLUMNS):
            if (row + col) % 2 == 0:
                color_string += '0'
            else:
                color_string += '2' 
        
        draw_line_from_string(color_string, turta)
        turta.penup()
        turta.goto(-PIXEL_SIZE * COLUMNS / 2, turta.ycor() - PIXEL_SIZE)
        turta.pendown()



""" This function draws a shape using color data from a file, it reads color strings from the given files
    and uses the turtle object to draw each row of pixels. For each line in the file, it draws a row of 
    pixels corresponding to the color codes. The turtle moves to the start of the next row after drawing each line
    and if an invalid color code is entered, the drawing stops."""
def draw_shape_from_file(turta):
    file_path = input("Please enter the path to the .txt file: ")
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                color_string = line.strip()
                result = draw_line_from_string(color_string, turta)
                if not result:
                    print("Error: Invalid color string in file. Stopping.")
                    return

                turta.penup()
                turta.goto(-PIXEL_SIZE * COLUMNS / 2, turta.ycor() - PIXEL_SIZE)
                turta.pendown()

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as error:
        print("An error occurred", error)