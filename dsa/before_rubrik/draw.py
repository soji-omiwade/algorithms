import turtle
turtle.setup(500,500)
board = turtle.Turtle()
 
# draws a rectangle given top left position of a rectangle
def draw_filled_rectangle(board,x,y,width,height,size,color,fill):
  board.fillcolor(fill)
  board.pencolor(color)
  board.pensize(size)
  board.setheading(0)
 
  board.begin_fill()
  board.up()
  board.goto(x,y)
  board.down()
  # draw top
  board.forward(width)
  # draw right
  board.right(90)
  board.forward(height)
  # draw bottom
  board.right(90)
  board.forward(width)
  # draw left
  board.right(90)
  board.forward(height)
  board.end_fill()
 
 
# in turtle, the centre of the canvas is 0,0
# hence we position the rectangle in the center
# note that we need to pass the top left co-ordinates of rectangle
# draws rectangle with 200 pixels in width and 100 pixels in height
# also specifies the rectangle color and the fill color
draw_filled_rectangle(board,-100,50,200,100,5,"blue","green")
turtle.done() 