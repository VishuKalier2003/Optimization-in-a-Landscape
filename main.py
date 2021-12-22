"""
The Problem: A landscape is provided having Houses and Hospitals in the landscape arranged randomly. The environment
             formed is partially observable static environment with time and the AI agent is dynamic and episodic in
             nature.
Artificial Intelligence : The AI agent now moves in the landscape and passes through each and every House and Hospital
                          formed in the landscape.
Task of the AI :
1st. The AI Agent first covers and checks all the Houses and Hospitals placed in the landscape.
2nd. The AI Agent now optimises the path to connect all the Houses with the nearest Hospital possible.
"""
import pygame  # class pygame imported
import random  # class random imported
import matplotlib.pyplot as plt  # class imported for drawing graph

"""   Problem or the Landscape formation as a Grid     """
WHITE = (255, 255, 255)  # tuple assigned for white colour
length = 900  # length of the pygame screen
breadth = 870  # breadth of the pygame screen
pygame.init()  # pygame module initialised
pygame.mixer.init()
screen = pygame.display.set_mode((length, breadth))  # screen formed with breadth and height as dimensions
pygame.display.set_caption("Optimisation in a landscape")  # caption of the pygame window
grid = []  # list created for grid or matrix


def build_grid(x, y, w):  # function formed for grid matrix or basic landscape
    for i in range(1, 18):  # The grid will contain 18 columns
        x = 30  # The grid starts at x coordinate from 30
        y = y + 30  # The grid starts at y coordinate from 120
        for j in range(1, 28):  # The grid will contain 28 rows
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y], 1)  # Top line is drawn with width w
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w], 1)  # Right line is drawn with width w
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w], 1)  # Bottom line is drawn with width w
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y], 1)  # Left line is drawn with width w
            grid.append((x, y))  # for every block the grid elements are added to the list
            pygame.display.update()  # the update is displayed in the pygame window
            x = x + 30


build_grid(30, 120, 30)  # x coordinate = 30, y coordinate = 120, width = 30
w1 = 30  # width 1 equated to 30
x11 = 30  # variable for x coordinate for houses
y11 = 30  # variable for y coordinate for houses
x111 = 0  # variable for x coordinate for hospitals
y111 = 0  # variable for y coordinate for hospitals
list_x = [0] * 50  # list of x coordinates of all houses
list_y = [0] * 50  # list of y coordinates of all houses
hos_x = [0] * 10  # list of x coordinates of all hospitals
hos_y = [0] * 10  # list of y coordinate of all hospitals
visited_x = []  # list of all x coordinates visited by the AI agent
visited_y = []  # list of all y coordinates visited by the AI agent
path = 0  # path cost is stored in this variable
borders_hos_x = [0] * 50  # borders of all x coordinate of all houses in the landscape
borders_hos_y = [0] * 50  # borders of all y coordinate of all houses in the landscape
borders_list_x = [0] * 10  # borders of all x coordinate of all hospitals in the landscape
borders_list_y = [0] * 10  # borders of all y coordinate of all hospitals in the landscape


# AI agent is represented in Green colour and it moves really fast such that it appears blinking
def draw_cursor(x1, y1):  # function cursor takes in two parameters of x and y coordinates as input
    pygame.draw.rect(screen, (0, 100, 0), [x1, y1, w1, w1])  # method for drawing rectangles
    pygame.display.update()  # The display is thereby updated


# The AI agent leaves behind a track of light blue colour showing the places visited and left to be visited
def draw_rectangles(x1, y1):  # The function takes two parameters as input
    pygame.draw.rect(screen, (0, 191, 255), [x1, y1, w1, w1])  # Method for drawing rectangles
    pygame.display.update()  # The display is now updated


# AI agent now moves right
def move_right(x1, y1):  # Parameters as current x and y coordinates
    for i in range(x1, x1 + 31):  # The loop begins and be updated 30 times
        draw_rectangles(i, y1)  # The loop defines a transition as the AI agent moves
    draw_cursor(x1 + 30, y1)  # The cursor function is called to display the position of Agent
    draw_rectangles(x1 + 30, y1)  # Called to show the visited places


# AI agent now moves left
def move_left(x1, y1):  # Coordinate parameters as input
    for i in range(x1, x1 - 31):  # The loop begins
        draw_rectangles(i, y1)  # The loop defines the transition of the AI agent moving
    draw_cursor(x1 - 30, y1)  # Position of the AI agent displayed
    draw_rectangles(x1 - 30, y1)  # Called to show the visited places


# AI agent now moves up
def move_up(x1, y1):  # The coordinate parameters taken as input
    for i in range(y1, y1 - 31):  # Loop begins
        draw_rectangles(x1, i)  # The transition of AI agent defined
    draw_cursor(x1, y1 - 30)  # Position of the AI agent displayed
    draw_rectangles(x1, y1 - 30)  # Called to show the visited places


# AI agent now moves down
def move_down(x1, y1):  # The coordinate taken as input
    for i in range(y1, y1 + 31):  # Loop begins
        draw_rectangles(x1, i)  # The transition of AI agent defined
    draw_cursor(x1, y1 + 30)  # Position displayed
    draw_rectangles(x1, y1 + 30)  # Called forth to show the visited places


# Function to draw houses at the given places
def draw_houses(zx11, zy11):  # x and y coordinate as input
    pygame.draw.rect(screen, (220, 20, 60), [zx11, zy11, w1, w1])  # Rectangle drawn
    pygame.display.update()  # Display updated


for term1 in range(0, 50):  # Loop for drawing 50 houses
    x11 = (random.randint(1, 27) * 30)  # Choosing random x coordinate
    y11 = (random.randint(5, 21) * 30)  # Choosing random y coordinate
    list_x[term1] = x11  # X coordinate stored
    borders_hos_x[term1] = x11  # X coordinate stored as border
    list_y[term1] = y11  # Y coordinate stored
    borders_hos_y[term1] = y11  # Y coordinate stored as border
    draw_houses(x11, y11)  # House function called to be drawn


def draw_hospital(hx, hy):  # Hospital function for drawing Hospital
    pygame.draw.rect(screen, (255, 255, 0), [hx, hy, w1, w1])  # Rectangle function called
    pygame.display.update()  # Display updated


for term in range(0, 10):  # Loop for drawing 10 Hospitals
    x111 = (random.randint(1, 26) * 30)  # Random location
    y111 = (random.randint(5, 20) * 30)  # Random location
    hos_x[term] = x111  # X coordinate stored
    borders_list_x[term] = x111  # Y coordinate stored
    hos_y[term] = y111  # X coordinate stored as border
    borders_list_y[term] = y111  # Y coordinate stored
    draw_hospital(x111, y111)  # Y coordinate stored as border

"""    1st. Task of Artificial Intelligence Agent: To Explore the Landscape    """

ne = [0] * 60  # List created for stored the check condition of both houses and hospitals collectively
r = 0  # variable initialised


def check_nearby_right(xx1, yy1):  # Checks if there is hospital or house at next right turn
    global ne  # variable globalised for the function
    for k in range(0, 50):  # Loop begins
        if xx1 + 30 == borders_hos_x[k] and yy1 == borders_hos_y[k]:  # Condition for check
            net = 1  # If true then value changed to 1
            ne[k] = net  # stored in list
        else:
            net = 0  # Else value 0
            ne[k] = net  # still stored in list

    for k2 in range(0, 10):  # Loop begins
        if xx1 + 30 == borders_list_x[k2] and yy1 == borders_list_y[k2]:  # Condition for check
            net = 1  # If true
            ne[50 + k2] = net
        else:
            net = 0  # If false
            ne[50 + k2] = net  # Value stored


def check_nearby_left(xx1, yy1):  # Checks if there is a Hospital or House at the next left turn
    global ne  # variable globalised
    for k in range(0, 50):  # Loop begins
        if xx1 - 30 == borders_hos_x[k] and yy1 == borders_hos_y[k]:  # Condition check
            net = 1  # If true
            ne[k] = net
        else:
            net = 0  # If false
            ne[k] = net

    for k2 in range(0, 10):  # Loop begins
        if xx1 - 30 == borders_list_x[k2] and yy1 == borders_list_y[k2]:  # Condition check
            net = 1
            ne[50 + k2] = net
        else:  # else block
            net = 0
            ne[50 + k2] = net  # value stored


def check_nearby_up(xx1, yy1):  # checks if there is any house or hospital at next up turn
    global ne  # variable globalised
    for k in range(0, 50):  # loop begins
        if xx1 == borders_hos_x[k] and yy1 - 30 == borders_hos_y[k]:  # Condition check
            net = 1  # If true
            ne[k] = net
        else:  # Else block begins
            net = 0
            ne[k] = net  # value stored

    for k2 in range(0, 10):  # Loop begins
        if xx1 == borders_list_x[k2] and yy1 - 30 == borders_list_y[k2]:  # Condition check
            net = 1  # value changed to 1
            ne[50 + k2] = net  # value stored
        else:  # Else block begins
            net = 0
            ne[50 + k2] = net  # value stored


def check_nearby_down(xx1, yy1):  # checks if there is any hospital or house at next down turn
    global ne  # variable globalised
    for k in range(0, 50):  # Loop begins
        if xx1 == borders_hos_x[k] and yy1 + 30 == borders_hos_y[k]:  # Condition check
            net = 1
            ne[k] = net  # Variable still stored
        else:
            net = 0
            ne[k] = net  # Variable stored

    for k2 in range(0, 10):  # Loop begins
        if xx1 == borders_list_x[k2] and yy1 + 30 == borders_list_y[k2]:  # Condition check
            net = 1
            ne[50 + k2] = net  # variable stored
        else:  # Else block begins
            net = 0
            ne[50 + k2] = net  # Variable stored


'''   -----Formation of the Depth First Search (DFS) Algorithm-----   '''


def travel(x1, y1):  # AI agent now begins travelling
    n = 0  # counter variable
    while n <= 9000:  # Since we use Depth-First-Search we take the value of n large to ensure all house are connected
        ran = random.randint(1, 4)  # random numbers created form 1 to 4
        if ran == 1 and x1 <= 780:  # If ran equals 1 and within boundary
            check_nearby_right(x1, y1)  # function called
            if ne[0:60] == [0] * 60:  # nearby check
                move_right(x1, y1)  # AI agent moves right
                x1 = x1 + 30
                y1 = y1
                visited_x.append(x1)  # Added
                visited_y.append(y1)  # Added

        if ran == 2 and x1 >= 60:  # If ran equals 2 and within boundary
            check_nearby_left(x1, y1)  # function called
            if ne[0:60] == [0] * 60:  # nearby check
                move_left(x1, y1)  # AI agent moves left
                x1 = x1 - 30
                y1 = y1
                visited_x.append(x1)  # Added
                visited_y.append(y1)  # Added

        if ran == 3 and y1 >= 180:  # If ran equals 3 and within boundary
            check_nearby_up(x1, y1)  # function called
            if ne[0:60] == [0] * 60:  # nearby check
                move_up(x1, y1)  # AI agent moves up
                x1 = x1
                y1 = y1 - 30
                visited_x.append(x1)  # Added
                visited_y.append(y1)  # Added

        if ran == 4 and y1 <= 600:  # If ran equals 4 and within boundary
            check_nearby_down(x1, y1)  # function called
            if ne[0:60] == [0] * 60:  # nearby check
                move_down(x1, y1)  # Ai agent moves down
                x1 = x1
                y1 = y1 + 30
                visited_x.append(x1)  # Added
                visited_y.append(y1)  # Added

        n = n + 1  # counter variable incremented by 1


travel(30, 150)  # travel function called and now AI Agent starts moving

"""     2nd Task of AI agent : Optimisation of path of every House to the nearest hospital possible    """


# AI agent is represented in Violet colour and it moves really fast such that it appears blinking
def draw_pointer(ax1, ay1):  # function cursor takes in two parameters of x and y coordinates as input
    pygame.draw.rect(screen, (255, 0, 0), [ax1, ay1, w1, w1])  # method for drawing rectangles
    pygame.display.update()  # The display is thereby updated


# The AI agent leaves behind a track of deep blue colour showing the places visited and left to be visited
def draw_path(ax1, ay1):  # The function takes two parameters as input
    pygame.draw.rect(screen, (0, 0, 255), [ax1, ay1, w1, w1])  # Method for drawing rectangles
    pygame.display.update()  # The display is now updated


# AI agent now moves right for optimisation purposes
def trace_right(ax1, ay1):  # Parameters as current x and y coordinates
    for i in range(ax1, ax1 + 31):  # The loop begins
        draw_path(i, ay1)  # The loop defines a transition as the AI agent moves
    draw_pointer(ax1 + 30, ay1)  # The cursor function is called to display the position of Agent
    draw_path(ax1 + 30, ay1)  # Called to show the visited places


# AI agent now moves left for optimisation purposes
def trace_left(ax1, ay1):  # Coordinate parameters as input
    for i in range(ax1, ax1 - 31):  # The loop begins
        draw_path(i, ay1)  # The loop defines the transition of the AI agent moving
    draw_pointer(ax1 - 30, ay1)  # Position of the AI agent displayed
    draw_path(ax1 - 30, ay1)  # Called to show the visited places


# AI agent now moves up for optimisation purposes
def trace_up(ax1, ay1):  # The coordinate parameters taken as input
    for i in range(ay1, ay1 - 31):  # Loop begins
        draw_path(ax1, i)  # The transition of AI agent defined
    draw_pointer(ax1, ay1 - 30)  # Position of the AI agent displayed
    draw_path(ax1, ay1 - 30)  # Called to show the visited places


# AI agent now moves down for optimisation purposes
def trace_down(ax1, ay1):  # The coordinate taken as input
    for i in range(ay1, ay1 + 31):  # Loop begins
        draw_path(ax1, i)  # The transition of AI agent defined
    draw_pointer(ax1, ay1 + 30)  # Position displayed
    draw_path(ax1, ay1 + 30)  # Called forth to show the visited places


optimise_x = []  # Storing the x coordinates of optimised path
optimise_y = []  # Storing the y coordinates of optimised path


def drawing_borders():   # The AI agent races out the borders of the Landscape
    x = 30   # x coordinate initialised
    y = 150  # y coordinate initialised
    while x < 810:  # Covering the upper boundary
        trace_right(x, y)  # Tracing rightwards
        x = x + 30  # value incremented consequently

    while y < 630:   # Covering the right boundary
        trace_down(x, y)  # Tracing downwards
        y = y + 30  # value incremented consequently

    while x > 30:   # Covering the lower boundary
        trace_left(x, y)  # Tracing leftwards
        x = x - 30  # Value decremented consequently

    while y > 150:  # Covering the left boundary
        trace_up(x, y)  # Tracing upwards
        y = y - 30  # Value decremented consequently


for run in range(0, 2):  # Iteration till 2 times
    drawing_borders()  # Function called

'''  -----Beginning of the A* Algorithm and evaluation of the Heuristics-----  '''

placed_down_x = []  # List created for storing x coordinates of places visited when AI Agent travel downwards
placed_down_y = []  # List created for storing y coordinates of places visited when AI Agent travel downwards
for t in range(0, 50):  # Loop begins for Houses
    if borders_hos_y[t] <= 450:  # Divided into Quadrants which intermingle with each other
        placed_down_x.append(borders_hos_x[t])  # List appended
        placed_down_y.append(borders_hos_y[t])  # List appended

for t1 in range(0, 10):  # Loop begins for Hospitals
    if borders_list_y[t1] <= 450:  # Divided into Quadrant which intermingle to some extent with each other
        placed_down_x.append(borders_list_x[t1])  # List appended
        placed_down_y.append(borders_list_y[t1])  # List appended

num = len(placed_down_y)  # Length of list evaluated since both coordinates will have same number
for t in range(0, num):  # Loop begins
    sx = placed_down_x[t - 1]  # start of x coordinate evaluated
    sy = 150  # start of y coordinate evaluated
    ey = placed_down_y[t - 1]  # end of y evaluated
    s = int(ey / 30) - 5  # distance evaluated
    for m in range(0, s):  # Ranging from zero to the distance available
        trace_down(sx, sy)  # AI agent moves down
        sy = sy + 30  # start of y consequently evaluated

placed_right_x = []  # List created for storing x coordinates when AI moves rightwards
placed_right_y = []  # List created for storing y coordinates when AI moves rightwards
for t in range(0, 50):  # Loop begins for Houses
    if borders_hos_x[t] <= 420:  # Divided into Quadrant which intermingle to some extent with each other
        placed_right_x.append(borders_hos_x[t])  # List appended
        placed_right_y.append(borders_hos_y[t])  # List appended

for t1 in range(0, 10):  # Loop begins for Hospitals
    if borders_list_y[t1] <= 420:  # Divided into Quadrant which intermingle to some extent with each other
        placed_right_x.append(borders_list_x[t1])  # List appended
        placed_right_y.append(borders_list_y[t1])  # List appended

num = len(placed_right_y)  # Length of the list evaluated
for t in range(0, num):  # For the entire list above the loop will run
    sx = 30  # start of x initialised
    sy = placed_right_y[t - 1]  # start of y initialised
    ex = placed_right_x[t - 1]  # end of x initialised
    s = int(ex / 30) - 1  # Distance evaluated
    for m in range(0, s):  # Ranging from zero to distance to be moved
        trace_right(sx, sy)  # AI Agent moves right
        sx = sx + 30  # start of x consequently evaluated

placed_up_x = []  # List created for storing x coordinates when AI Agent moves upwards
placed_up_y = []  # List created for storing y coordinates when AI Agent moves upwards
for t in range(0, 50):  # Loop begins for Houses
    if borders_hos_y[t] >= 330:  # Divided into Quadrants which intermingle with each other to some extent
        placed_up_x.append(borders_hos_x[t])  # List appended
        placed_up_y.append(borders_hos_y[t])  # List appended

for t1 in range(0, 10):  # Loop begins for Hospitals
    if borders_list_y[t1] >= 330:  # Divided into Quadrants which intermingle with each other to some extent
        placed_up_x.append(borders_list_x[t1])  # List appended
        placed_up_y.append(borders_list_y[t1])  # List appended

num = len(placed_up_y)  # Length of the list calculated
for t in range(0, num):  # Ranging for the entire list the loop runs
    sx = placed_up_x[t - 1]  # Start of x evaluated
    sy = 630  # Start of y evaluated
    ey = placed_up_y[t - 1]  # End of y evaluated
    s = int(ey / 30) - 8  # distance calculated
    for m in range(0, s):  # Ranging for th entire distance
        trace_up(sx, sy)  # AI Agent moves upwards
        sy = sy - 30  # start of y changes consequently

placed_left_x = []  # List created to store x coordinates of places visited when AI Agent moves downwards
placed_left_y = []  # List created to store y coordinates of places visited when AI Agent moves downwards
for t in range(0, 50):  # Iterating for every Houses available
    if borders_hos_x[t] >= 420:  # Divided into Quadrants which intermingle to some extent with one another
        placed_left_x.append(borders_hos_x[t])  # List appended
        placed_left_y.append(borders_hos_y[t])  # List appended

for t1 in range(0, 10):  # Iterating for every Hospital available
    if borders_list_y[t1] >= 420:  # Divided into Quadrants which intermingle to some extent with one another
        placed_left_x.append(borders_list_x[t1])  # List appended
        placed_left_y.append(borders_list_y[t1])  # List appended

num = len(placed_left_y)  # Length of the list evaluated
for t in range(0, num):  # Ranging for the entire list the loop executes itself
    sx = 810  # Start of x initialised
    sy = placed_left_y[t - 1]  # Start of y calculated
    ex = placed_left_x[t - 1]  # End of x initialised
    s = int(ex / 30) - 14  # Distance evaluated
    for m in range(0, s):  # Ranging from zero to the distance evaluated each turn
        trace_left(sx, sy)  # AI Agent moves leftwards
        sx = sx - 30  # start of x calculated consequently

for i3 in range(0, 50):  # Ranging for all Houses available
    draw_houses(borders_hos_x[i3], borders_hos_y[i3])  # Houses drawn again

for i4 in range(0, 10):  # Ranging for all Hospitals available
    draw_hospital(borders_list_x[i4], borders_list_y[i4])  # Hospitals drawn again


# AI agent is represented in Violet colour and it moves really fast such that it appears blinking
def draw_optimised_pointer(ax1, ay1):  # function cursor takes in two parameters of x and y coordinates as input
    pygame.draw.rect(screen, (148, 0, 211), [ax1, ay1, w1, w1])  # method for drawing rectangles
    pygame.display.update()  # The display is thereby updated


# The AI agent leaves behind a track of deep blue colour showing the places visited and left to be visited
def drawing_path(ax1, ay1):  # The function takes two parameters as input
    pygame.draw.rect(screen, (25, 25, 112), [ax1, ay1, w1, w1])  # Method for drawing rectangles
    pygame.display.update()  # The display is now updated


# AI agent now moves right for optimisation purposes
def tracing_right(ax1, ay1):  # Parameters as current x and y coordinates
    for i in range(ax1, ax1 + 31):  # The loop begins
        drawing_path(i, ay1)  # The loop defines a transition as the AI agent moves
    draw_optimised_pointer(ax1 + 30, ay1)  # The cursor function is called to display the position of Agent
    drawing_path(ax1 + 30, ay1)  # Called to show the visited places


# AI agent now moves left for optimisation purposes
def tracing_left(ax1, ay1):  # Coordinate parameters as input
    for i in range(ax1, ax1 - 31):  # The loop begins
        drawing_path(i, ay1)  # The loop defines the transition of the AI agent moving
    draw_optimised_pointer(ax1 - 30, ay1)  # Position of the AI agent displayed
    drawing_path(ax1 - 30, ay1)  # Called to show the visited places


# AI agent now moves up for optimisation purposes
def tracing_up(ax1, ay1):  # The coordinate parameters taken as input
    for i in range(ay1, ay1 - 31):  # Loop begins
        drawing_path(ax1, i)  # The transition of AI agent defined
    draw_optimised_pointer(ax1, ay1 - 30)  # Position of the AI agent displayed
    drawing_path(ax1, ay1 - 30)  # Called to show the visited places


# AI agent now moves down for optimisation purposes
def tracing_down(ax1, ay1):  # The coordinate taken as input
    for i in range(ay1, ay1 + 31):  # Loop begins
        drawing_path(ax1, i)  # The transition of AI agent defined
    draw_optimised_pointer(ax1, ay1 + 30)  # Position displayed
    drawing_path(ax1, ay1 + 30)  # Called forth to show the visited places


# It a method of Searching for linear set of data in which a bubble is formed and it moves across the set of data
def bubble_sorting(list1, list2):  # Two list are taken as parameters
    for k in range(0, len(list1)):  # Length of list1
        for j in range(0, len(list2)):  # Length of list 2
            if list1[k] > list1[j]:  # If an element in list1 is larger than its succeeding element
                p3 = list1[j]  # Temporary change of variable
                u = list2[j]  # Temporary change of variables
                list1[j] = list1[k]  # Bubbles of List values interchanged
                list2[j] = list2[k]  # Bubbles of list values
                list1[k] = p3  # Change of variables
                list2[k] = u   # Change of variables


bubble_sorting(placed_down_x, placed_down_y)  # Function called
bubble_sorting(placed_up_x, placed_up_y)  # Function called

'''  -----Formation of the final path by the A* Algorithm-----   '''


def tracing_placed_down(n):  # Function for connecting all nearby Houses and Hospitals when traced downwards
    global path  # path variable globalised
    s_x = placed_down_x[n]  # start of x coordinate determined
    s_y = placed_down_y[n]  # start of y coordinate determined
    e_x = placed_down_x[n + 1]  # end of x coordinate determined
    e_y = placed_down_y[n + 1]  # end of y coordinate determined
    d = int((s_x - e_x)/30)  # distance calculated
    e = int((s_y - e_y)/30)  # distance calculated
    if e < 0:  # if y distance is negative
        f = -e  # temporary variable assignment
        for mark in range(0, d):  # Loop begins
            if 30 < s_x < 830:  # Boundary conditions checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_left(s_x, s_y)  # AI agent races leftwards
                s_x = s_x - 30  # start of x changes after every iteration

        for mark in range(0, f):  # Loop begins
            if 150 < s_y <= 450:  # Boundary conditions checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_down(s_x, s_y)  # AI Agent moves downwards
                s_y = s_y + 30  # start of y changed continuously

    if e > 0:  # if y distance is positive
        for mark in range(0, d):  # Loop begins
            if 30 < s_x < 830:   # Boundary condition checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_left(s_x, s_y)  # AI Agent moves leftwards
                s_x = s_x - 30  # start of x calculated iteratively

        for mark in range(0, e):  # Loop begins
            if 150 < s_y <= 450:  # Boundary condition checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_up(s_x, s_y)  # AI Agent moves upwards
                s_y = s_y - 30  # start of y calculated

    if e == 0:  # If both points lie on same Y plane
        for mark in range(0, d):  # Loop begins
            if 30 < s_x < 830:  # Boundary condition check
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_left(s_x, s_y)  # AI Agent moves leftwards
                s_x = s_x - 30  # start of y calculated iteratively

    if d == 0:  # If both points lie on same X plane
        if e < 0:  # If y distance is negative
            f = -e  # Temporary variable
            for mark in range(0, f):  # Loop begins
                if 150 < s_y <= 450:  # Boundary check
                    optimise_x.append(s_x)  # List appended
                    optimise_y.append(s_y)  # List appended
                    tracing_down(s_x, s_y)  # AI Agent moves downwards
                    s_y = s_y + 30  # Start of y changed per iteration

        if e > 0:  # If y distance is negative
            for mark in range(0, e):  # Loop begins
                if 150 < s_y <= 450:  # Boundary conditions checked
                    optimise_x.append(s_x)  # List appended
                    optimise_y.append(s_y)  # List appended
                    tracing_up(s_x, s_y)  # AI Agent moves upwards
                    s_y = s_y - 30  # start of y changes continuously


for z in range(0, 1):  # Outer loop
    for m in range(0, len(placed_down_x) - 1):  # Inner loop
        tracing_placed_down(m)  # Function called


def tracing_placed_up(n):  # Function for connecting all Houses and Hospitals when traced upwards
    global path  # variable globalised
    s_x = placed_up_x[n]  # start of x coordinate initiated
    s_y = placed_up_y[n]  # start of y coordinate initiated
    e_x = placed_up_x[n + 1]  # end of x coordinate initialised
    e_y = placed_up_y[n + 1]  # end of y coordinate initialised
    d = int((s_x - e_x)/30)  # distance for x coordinates calculated
    e = int((s_y - e_y)/30)  # distance for y coordinates calculated
    if e < 0:  # If distance of y is negative
        f = -e  # Temporary variable assignment
        for mark in range(0, d):  # Loop begins
            if 30 < s_x < 830:  # Boundary checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_left(s_x, s_y)  # AI Agent moves leftwards
                s_x = s_x - 30  # start of x changed

        for mark in range(0, f):  # Loop begins
            if 330 <= s_y <= 600:  # Boundary checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_down(s_x, s_y)  # AI Agent moves downwards
                s_y = s_y + 30  # start of y changes consequently

    if e > 0:  # If y distance is positive
        for mark in range(0, d):  # Loop begins
            if 30 < s_x < 830:   # Boundary conditions checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_left(s_x, s_y)  # AI Agent moves leftwards
                s_x = s_x - 30  # start of x coordinates changing frequently

        for mark in range(0, e):  # Loop begins
            if 330 <= s_y <= 600:  # Boundary conditions checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_up(s_x, s_y)  # AI Agent moves upwards
                s_y = s_y - 30  # start of y coordinates changing frequently

    if e == 0:  # If both points lie on same Y planes
        for mark in range(0, d):  # Loop begins
            if 30 < s_x < 830:  # Boundary conditions checked
                optimise_x.append(s_x)  # List appended
                optimise_y.append(s_y)  # List appended
                tracing_left(s_x, s_y)  # AI Agent moves leftwards
                s_x = s_x - 30  # start of x coordinates changing frequently

    if d == 0:  # If both points lie on same X planes
        if e < 0:  # If y distance is negative
            f = -e  # Temporary variable assignment
            for mark in range(0, f):  # Loop  begins
                if 330 <= s_y <= 600:  # Boundary conditions checked
                    optimise_x.append(s_x)  # List appended
                    optimise_y.append(s_y)  # List appended
                    tracing_up(s_x, s_y)  # AI Agent moves upwards
                    s_y = s_y - 30  # Start of x changes per iteration

        if e > 0:  # If y distance is positive
            for mark in range(0, e):  # Loop begins
                if 330 <= s_y <= 600:  # Boundary checked
                    optimise_x.append(s_x)  # List appended
                    optimise_y.append(s_y)  # List appended
                    tracing_down(s_x, s_y)  # AI Agent moves downwards
                    s_y = s_y + 30  # Start of y changes frequently


for z in range(0, 1):  # Outer loop begins
    for m in range(0, len(placed_up_x) - 1):  # Inner loop begins
        tracing_placed_up(m)  # Function called

check_points = placed_down_x + placed_up_x  # check point list created of all Houses and Hospitals traced
for p in range(0, 50):  # Loop for Houses
    draw_houses(borders_hos_x[p], borders_hos_y[p])  # Houses drawn again

for q in range(0, 10):  # Loop for Hospitals
    draw_hospital(borders_list_x[q], borders_list_y[q])  # Hospitals drawn again

for run in range(0, 10000):  # Loop for making the screen visible for longer time ( Loop of Delay )
    o = random.randint(0, 49)  # Random House selected
    draw_houses(borders_hos_x[o], borders_hos_y[o])  # House continuously drawn

'''   -----Plotting of the Data in the form of Nodes and Edges on the Graph-----   '''

bubble_sorting(borders_hos_x, borders_hos_y)  # Function called
bubble_sorting(borders_list_x, borders_list_y)  # Function called
xx = []  # Empty list
yy = []  # Empty list
xxx1 = []  # Empty list
yyy1 = []  # Empty list
x_path = []  # Empty list
y_path = []  # Empty list
ne[0:60] = [0] * 60  # List of zeroes initialised


def sorting(m1, n1):  # Function created for sorting the elements if they are adjacent to the optimised path
    for z1 in range(len(optimise_x)):
        check_nearby_right(optimise_x[z1], optimise_y[z1])
        if ne[0:60] != [0] * 60:  # If any landmark is at the right
            m1.append(optimise_x[z1] + 30)  # List appended
            n1.append(optimise_y[z1])  # List appended
        check_nearby_left(optimise_x[z1], optimise_y[z1])
        if ne[0:60] != [0] * 60:  # If any landmark is at the left
            m1.append(optimise_x[z1] - 30)  # List appended
            n1.append(optimise_y[z1])  # List appended
        check_nearby_up(optimise_x[z1], optimise_y[z1])
        if ne[0:60] != [0] * 60:  # If any landmark is at the upwards
            m1.append(optimise_x[z1])  # List appended
            n1.append(optimise_y[z1] - 30)  # List appended
        check_nearby_down(optimise_x[z1], optimise_y[z1])
        if ne[0:60] != [0] * 60:  # If any landmark is at the downwards
            m1.append(optimise_x[z1])  # List appended
            n1.append(optimise_y[z1] + 30)  # List appended


sorting(x_path, y_path)  # Function called
bubble_sorting(x_path, y_path)  # Function called
t2 = [0] * 50  # assigned for Houses
t3 = [0] * 10  # assigned for Hospitals
plt.title("Houses and Hospitals in the form of nodes and edges")  # Plot title


def check_house(xx1):  # Checking if all Houses are connected
    for r1 in range(0, len(optimise_x) - 1):  # Loop begins
        if borders_hos_x[xx1] == optimise_x[r1] and borders_hos_y[xx1] == optimise_y[r1]:  # Condition checked
            t2[xx1] = 1  # Value changed


def check_hospital(xx1):  # Checking if all Hospitals are connected
    for r1 in range(0, len(optimise_x) - 1):  # Loop begins
        if borders_list_x[xx1] == optimise_x[r1] and borders_list_y[xx1] == optimise_y[r1]:  # Condition checked
            t3[xx1] = 1  # Value changed


for h in range(0, 50):  # Loop begins
    check_house(h)  # Function called
    if t2[0:50] != [0] * 50:  # Condition checked
        xx.append(borders_hos_x[h])  # Graph list of Houses appended
        yy.append(borders_hos_y[h])  # Graph list of Houses appended

for h1 in range(0, 10):  # Loop begins
    check_hospital(h1)  # Function called
    if t3[0:10] != [0] * 10:  # Condition checked
        xxx1.append(borders_list_x[h1])  # Graph list of Hospitals appended
        yyy1.append(borders_list_y[h1])  # Graph list of Hospitals appended

plt.scatter(xx, yy, color='r', marker='*')  # Red color for connecting Houses
plt.plot(xx, yy, color='r', marker='*')  # Plotting the Coordinates
plt.scatter(xxx1, yyy1, color='y', marker='x')  # Yellow color for connecting Hospitals
plt.plot(xxx1, yyy1, color='y', marker='x')
plt.scatter(x_path, y_path, color='b', linestyle='dashed')  # Dashed Blue line for representing the Optimised path
plt.plot(x_path, y_path, color='b', linestyle='dashed')

''' ----- Evaluation of the Performance of the Algorithm and its Complexities ----- '''

check_x = []  # Empty list
check_y = []  # Empty list
for i1 in range(0, len(borders_hos_x)):
    for j1 in range(0, len(x_path)):
        if borders_hos_x[i1] == x_path[j1]:  # Condition check
            check_x.append(borders_hos_x[i1])  # List appended
            check_y.append(borders_hos_y[i1])  # List appended

for i1 in range(0, len(borders_list_x)):
    for j1 in range(0, len(x_path)):
        if borders_list_x[i1] == x_path[j1]:  # Condition check
            check_x.append(borders_list_x[i1])  # List appended
            check_y.append(borders_list_y[i1])  # List appended

for k1 in range(0, len(check_x) - 1):  # Eliminating the same valued elements
    if check_x[k1] == check_x[k1 + 1] and check_y[k1] == check_y[k1 + 1]:  # Condition foe elimination
        check_x[k1] = 0  # Reduced value to zero
        check_y[k1] = 0  # Reduced value to zero

count = 0  # Count variable
for k1 in range(0, len(check_x)):  # Loop begins
    if check_x[k1] != 0:  # Checking how many are correctly connected
        count = count + 1  # Count variable increased

performance = (count/60) * 100  # Performance of the Algorithm evaluated
print("The performance of the Algorithm optimising the Landscape correctly:", performance)  # Performance printed
print("The Space Complexity is number of rows of grid multiplied by the number of columns....")
print("The Space complexity is : O ( 28 x 18 )")
print("The Time Complexity is the time taken by the Algorithm....")
print("The Time Complexity is : O ( n )")
print("Thus, the time and Space Complexities are constant with Time in Best case or Linear in Worst case....")

plt.show()  # Showing the graph
