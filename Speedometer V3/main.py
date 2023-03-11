import turtle
import random
import time as time
import csv
sc = turtle.Screen()
sc.setup(1.0, 1.0)
marker_number_y = 1
marker_number_x = 0
speed = 0
seconds = 0
test_number = 1

f = open('timestamps.csv','r')
reader = csv.reader(f)
times = []
for line in reader:
    times.append(int(line[0]))


#Constants
WHEEL_DIAMETER = 20 
PI = 3.14159265359
INCHES_IN_MILE = 63360
MILLISECONDS_PER_HOUR = 3600000

#Width and Length of the graph
WIDTH = 1150
LENGTH = 670

#How many seconds between time running the for loop
TIME_BETWEEN_RUNNING = 1

#Sets the Minimum and Maximum Bars for the graph
MINIMAL_BAR = 10
MAXIMUM_BAR = 25

#Sets up wheel circumference
wheel_circumference = WHEEL_DIAMETER * PI


#Sets up the separate Turtles
mph_txt_turtle = turtle.Turtle()
mph_turtle = turtle.Turtle()
graph_plotter = turtle.Turtle()
sheet_drawler = turtle.Turtle()
number_drawler = turtle.Turtle()
extras_turtle = turtle.Turtle()
eraser_turtle = turtle.Turtle()


old_times_list = []
old_mph_list = []
number_bookmark = 0
eraser_turtle.color('white')
always_on = False

#Setting up eraser and buffer
current_list = []
eraser_num = -1

#Erase point
def erase_point(old_x, old_y):

    #This places the dot
    eraser_turtle.forward(old_x)
    eraser_turtle.left(90)
    eraser_turtle.forward(old_y)
    eraser_turtle.right(90)
    eraser_turtle.dot(10) #This has a Slightly Wider radius to avoid clipping

    #This resets the point for the next dot
    eraser_turtle.back(old_x)
    eraser_turtle.left(90)
    eraser_turtle.back(old_y)
    eraser_turtle.right(90)

#Sets up Program
def set_up_program(marker_number_x, marker_number_y):
    #Sets up the eraser turtle
    eraser_turtle.penup()
    eraser_turtle.right(180)
    eraser_turtle.forward(450)
    eraser_turtle.left(90)
    eraser_turtle.forward(260)
    eraser_turtle.left(90)

    #Sets up the dot maker
    graph_plotter.penup()
    graph_plotter.hideturtle()
    graph_plotter.right(180)
    graph_plotter.forward(450)
    graph_plotter.left(90)
    graph_plotter.forward(260)
    graph_plotter.left(90)

    #Sets all of the speeds to fastest
    mph_txt_turtle.speed('fastest')
    sheet_drawler.speed('fastest')
    graph_plotter.speed('fastest')
    mph_turtle.speed('fastest')
    number_drawler.speed('fastest')
    extras_turtle.speed('fastest')
    eraser_turtle.speed('fastest')

    #Number Drawling
    number_drawler.penup()
    number_drawler.right(180)
    number_drawler.forward(462)
    number_drawler.left(90)
    number_drawler.forward(255)
    number_drawler.right(180)

    #Y - Axis Number Plotter
    for _ in range(0, 33):
        number_drawler.write(marker_number_y, font=("Arial", 10, "normal"))
        number_drawler.forward(20)
        marker_number_y = marker_number_y + 1

    #X - Axis Number Plotter
    number_drawler.right(180)
    number_drawler.forward(678)
    number_drawler.left(90)
    for _ in range(0, 58):
        number_drawler.write(marker_number_x, font=("Arial", 10, "normal"))
        number_drawler.forward(20)
        marker_number_x = marker_number_x + 1

    #Write the Minimum bar name
    extras_turtle.penup()
    extras_turtle.forward(100)
    extras_turtle.right(90)
    extras_turtle.forward(90)
    extras_turtle.write("Minimum", font=("Arial", 16, "normal"))

    #Write the Maximum bar name
    extras_turtle.right(180)
    extras_turtle.forward(305)
    extras_turtle.write("Maximum", font=("Arial", 16, "normal"))

    #Sets up the Runner Turtle
    extras_turtle.right(180)
    extras_turtle.forward(620)
    extras_turtle.right(90)
    extras_turtle.forward(830) #810
    extras_turtle.right(90)
    extras_turtle.write("Running", font=("Arial", 16, "normal"))
    extras_turtle.forward(30)
    extras_turtle.right(90)
    extras_turtle.forward(28)
    extras_turtle.right(270)
    extras_turtle.shape('turtle')

    #Writes the Minimum Lines
    number_drawler.left(90)
    number_drawler.forward(200)
    number_drawler.left(90)
    number_drawler.pendown()
    number_drawler.color('blue')
    number_drawler.forward(1150)
    number_drawler.penup()

    #Writes the Maximum Lines
    number_drawler.right(90)
    number_drawler.forward(305)
    number_drawler.right(90)
    number_drawler.color('red')
    number_drawler.pendown()
    number_drawler.forward(1150)
    number_drawler.right(90)
    number_drawler.hideturtle()

    #MPH Text Turtle
    mph_txt_turtle.penup()
    mph_txt_turtle.right(180)
    mph_txt_turtle.forward(600)
    mph_txt_turtle.right(90)
    mph_txt_turtle.forward(400)
    mph_txt_turtle.right(90)
    mph_txt_turtle.forward(50)
    mph_txt_turtle.hideturtle()
    mph_txt_turtle.write("MPH", font=("Arial", 16, "normal"))

    #MPH Display Turtle
    mph_turtle.hideturtle()
    mph_turtle.penup()
    mph_turtle.left(180)
    mph_turtle.forward(545)
    mph_turtle.right(90)
    mph_turtle.forward(360)

#This graphs the new points
def graph_new_point(x, y):

    #This places the dot
    graph_plotter.forward(x)
    graph_plotter.left(90)
    graph_plotter.forward(y)
    graph_plotter.right(90)
    graph_plotter.dot()

    #This resets the point for the next dot
    graph_plotter.back(x)
    graph_plotter.left(90)
    graph_plotter.back(y)
    graph_plotter.right(90)

#Makes the Graph 
def set_up_graph():
    sheet_drawler.penup()
    sheet_drawler.right(180)
    sheet_drawler.forward(450)
    sheet_drawler.right(90)
    sheet_drawler.back(260)
    sheet_drawler.pendown()
    sheet_drawler.forward(LENGTH)
    sheet_drawler.right(90)
    sheet_drawler.forward(WIDTH)
    sheet_drawler.right(90)
    sheet_drawler.forward(LENGTH)
    sheet_drawler.right(90)
    sheet_drawler.forward(WIDTH)

    #Makes the X Marks
    for _ in range(57):
        sheet_drawler.back(20)
        sheet_drawler.right(90)
        sheet_drawler.forward(8)
        sheet_drawler.back(8)
        sheet_drawler.left(90)

    #Makes the Y Marks
    sheet_drawler.penup()
    sheet_drawler.forward(1140)
    sheet_drawler.right(90)
    sheet_drawler.pendown()
    
    for _ in range(33):
        sheet_drawler.forward(20)
        sheet_drawler.right(90)
        sheet_drawler.forward(8)
        sheet_drawler.back(8)
        sheet_drawler.left(90)

    sheet_drawler.hideturtle()

#This graphs the new points
def graph_new_point(x, y):

    #This places the dot
    graph_plotter.forward(x)
    graph_plotter.left(90)
    graph_plotter.forward(y)
    graph_plotter.right(90)
    graph_plotter.dot()

    #This resets the point for the next dot
    graph_plotter.back(x)
    graph_plotter.left(90)
    graph_plotter.back(y)
    graph_plotter.right(90)

#This sets up the program and graph
set_up_program(marker_number_x, marker_number_y)
set_up_graph()

#Runs the Main Program
while True:
    #Sets and Add seconds 
    seconds = seconds + TIME_BETWEEN_RUNNING 

    #Calculates the speed using wheel circumference and timestamps 
    for num in range(len(times) - test_number):
        milliseconds = times[num+1] - times[num]
        if speed == 0:
            break
        speed = wheel_circumference / milliseconds
        speed = speed * MILLISECONDS_PER_HOUR / INCHES_IN_MILE
    test_number = test_number + 1


    #Append speed to current list for the eraser dot
    current_list.append(speed)

    #Sets the X & Y cords and Graphs it
    x = seconds * 30 
    y = speed * 19
    graph_new_point(x, y)

    if seconds >= 40:
        seconds = 0
        always_on = True

    #This sleeps the Program set at TIME_BETWEEEN_RUNNING
    time.sleep(TIME_BETWEEN_RUNNING / 2)
    extras_turtle.color('blue')
    time.sleep(TIME_BETWEEN_RUNNING / 2)
    extras_turtle.color('red')

    #Displays and Updates the mph_turtle
    old_times_list.append(y)
    old_mph_list.append(x)
    if seconds > 35 or always_on == True:
        old_x = old_mph_list[number_bookmark]
        old_y = old_times_list[number_bookmark]
        erase_point(old_x, old_y)
        number_bookmark = number_bookmark + 1
    
    #Displays and Updates the mph_turtle
    mph_turtle.clear()
    mph_turtle.write(speed, font=("Arial", 16, "normal"))