import turtle as t
screen = t.Screen()
def draw_grid():
    for i in range(4):
        t.penup()
        t.goto(-100, 100 - i * 100)
        t.pendown()
        t.forward(300)
    
    t.right(90)
    for i in range(4):
        t.penup()
        t.goto(-100 + i * 100, 100)
        t.pendown()
        t.forward(300)
    t.right(90)

def draw_x(x, y):
    t.pu()
    t.goto(x - 30, y - 30)
    t.pendown()
    t.goto(x + 30, y + 30)
    t.penup()
    t.goto(x + 30, y - 30)
    t.pendown()
    t.goto(x - 30, y + 30)

def draw_o(x, y):
    t.penup()
    t.goto(x, y - 30)
    t.pendown()
    t.circle(30)

def check_winner():
    w = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, c, d in w:
        if b[a] == b[c] == b[d] != ' ':
            return True
    return False

def click_handler(x, y):
    global t
    
    coords = [(-50, 50), (50, 50), (150, 50), (-50, -50), (50, -50), (150, -50), (-50, -150), (50, -150), (150, -150)]
    
    index = int(((y + 100) // 100) * 3 + ((x + 100) // 100))
    if index < 0 or index > 8 or b[index] != ' ':
        return
    
    x_coord, y_coord = coords[index]
    
    if p[t] == 'X':
        draw_x(x_coord, y_coord)
    else:
        draw_o(x_coord, y_coord)
    
    b[index] = p[t]
    if check_winner():
        print(f"Player {p[t]} wins!")
        t.done()
        return
    
    if ' ' not in b:
        print("It's a draw!")
        return
    
    t = 1 - t

t.speed(0)
draw_grid()

b = [' '] * 9
p = ['X', 'O']
t = 0
screen.onclick(fun=click_handler, btn=1)
screen.mainloop()
