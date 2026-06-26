import turtle as t
t.speed(0)
t.width(3)
screen = t.Screen()
t.title("Tic Tac Toe")

all_coord_x_and_y = [[-150,150],[-50,150],[50,150],[-150,50],[-50,50],[50,50],[-150,-50],[-50,-50],[50,-50]]
busy_coord_x_and_y = [0,0,0,0,0,0,0,0,0]
coordinates_y= [150,50,-50]
coordinates_x= [-150,-50,50]
turn = 1

victory_variants = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

game_over = False
draw = True

def draw_line(start_index: int,end_index: int):
    t.color("green")
    t.pensize("5")
    if end_index - start_index == 2:
        start_x = all_coord_x_and_y[start_index][0]
        start_y = all_coord_x_and_y[start_index][1]-50
        end_x = all_coord_x_and_y[end_index][0]+100
        end_y = all_coord_x_and_y[end_index][1]-50
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)
    elif end_index - start_index == 6:
        start_x = all_coord_x_and_y[start_index][0]+50
        start_y = all_coord_x_and_y[start_index][1]
        end_x = all_coord_x_and_y[end_index][0]+50
        end_y = all_coord_x_and_y[end_index][1]-100
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)
    elif end_index - start_index == 8:
        start_x = all_coord_x_and_y[start_index][0]
        start_y = all_coord_x_and_y[start_index][1]
        end_x = all_coord_x_and_y[end_index][0]+100
        end_y = all_coord_x_and_y[end_index][1]-100
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)
    elif end_index - start_index == 4:
        start_x = all_coord_x_and_y[start_index][0]+100
        start_y = all_coord_x_and_y[start_index][1]
        end_x = all_coord_x_and_y[end_index][0]
        end_y = all_coord_x_and_y[end_index][1]-100
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)

def check_victory():
    t.color("orange")
    global game_over
    for win in victory_variants:
        victory = win
        if busy_coord_x_and_y[victory[0]] == busy_coord_x_and_y[victory[1]] == busy_coord_x_and_y[victory[2]]:
            if busy_coord_x_and_y[victory[0]] != 0:
                game_over = True
                draw_line(start_index = victory[0], end_index = victory[2])
                t.penup()
                t.goto(0,-200)
                t.pendown()
                t.write(arg = (f"Гравець №{turn} переможець!"),align = "center",font = ["Arial",32,"normal"])
    if game_over == False:
        check_draw()

def check_draw():
    t.color("blue")
    global game_over
    draw = True
    for numbers in busy_coord_x_and_y:
        if numbers == 0:
            draw = False
    if draw == True:
        t.penup()
        t.goto(0,-200)
        t.pendown()
        t.write(arg = "Нічия",align = "center",font = ["Arial",24,"normal"])
        game_over = True


def circle(x: float, y: float):
    t.pencolor("blue")
    t.penup()
    t.goto(x = x+50, y = y-100)
    t.pendown()
    t.circle(50)

def cross(x: float, y: float):
    t.speed()
    t.pencolor("red")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+100,y-100)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.goto(x,y-100)


def paint_square(length: int = 100) -> None:
    bb = 0
    t.fillcolor("white")
    t.begin_fill()
    while bb < 4:
        t.forward(length)
        t.left(90)
        bb += 1
    t.end_fill()

def circle_coords(x: float,y: float ):
    global turn
    count = 0
    if game_over == False:
        for element_y in coordinates_y:
            if element_y > y > element_y - 100:
                for element_x in coordinates_x:
                    if element_x < x < element_x + 100:
                        for element in all_coord_x_and_y:
                            if element[0] == element_x:
                                if element[1] == element_y:
                                    if busy_coord_x_and_y[count] == 0:
                                        if turn == 1:
                                            cross(element_x,element_y)
                                            busy_coord_x_and_y[count] = 1
                                            check_victory()
                                            turn = 2
                                        elif turn == 2:
                                            circle(element_x,element_y)
                                            busy_coord_x_and_y[count] = 2
                                            check_victory()
                                            turn = 1
                            count = count + 1

i = 0
x = -150
y = -150
while i < 3:
    d = 0
    while d < 3:
        t.penup()
        t.goto(x, y)
        t.pendown()
        paint_square()
        x += 100
        d += 1
    x = -150 
    y += 100
    i += 1


screen.onscreenclick(fun = circle_coords,btn=1)
t.hideturtle()
screen.mainloop()