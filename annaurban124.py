import turtle as trtl
import random

maze = trtl.Turtle()
maze.speed(0)
player = trtl.Turtle()
player.pencolor("blue")
door_width = 15
wall_width = 10
maze.ht()
dis = 5
maze.left(90)

def drawDoor():
    maze.penup()
    maze.forward(door_width)
    maze.pendown()

def drawBarrier():
    maze.right(90)
    maze.forward(wall_width*2)
    maze.backward(wall_width*2)
    maze.left(90)


for i in range(50):
    if i > 4:
        door = random.randint(door_width, dis - 2 * door_width)
        barrier = random.randint(wall_width, dis - 2 * door_width)
        if (door < barrier): 
            maze.forward(door)
            drawDoor()
            maze.forward(barrier - door -door_width)
            drawBarrier()
            maze.forward(dis - barrier)
        else:
            maze.forward(barrier)
            drawBarrier()
            maze.forward(door - barrier)
            drawDoor()
            maze.forward(dis - door - door_width)
    maze.left(90)
    dis += wall_width

def Up():
    player.setheading(90)
    player.forward(5)

def Right():
    player.setheading(0)
    player.forward(5)

def Left():
    player.setheading(180)
    player.forward(5)

def Down():
    player.setheading(270)
    player.forward(5)





wn = trtl.Screen()
wn.onkeypress(Up,"Up")
wn.onkeypress(Right,"Right")
wn.onkeypress(Left,"Left")
wn.onkeypress(Down,"Down")
wn.listen()
wn.mainloop()