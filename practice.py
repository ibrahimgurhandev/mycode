import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()

wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
init_side = 20
num_of_times_to_draw = 5
for i in range(num_of_times_to_draw):
    drawSquare(alex, init_side)
    init_side = init_side + 20

#print (drawSquare._doc_)    # can access docstring as function attribute
# print (doc(drawSquare))
wn.exitonclick()