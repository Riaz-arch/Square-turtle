import turtle

def draw_square(side_length):
    
    t = turtle.Turtle()

    for _ in range(4):
        t.forward(side_length)  
        t.right(90)             

    t.hideturtle()
    turtle.done()


side_length = 100  
draw_square(side_length)