import turtle

# shapes project
# draw different shapes 
# shapes to choose from
# traiangle
# circle
# star
# drawing the shapes needs to be done with functions
# user also needs to input the length of the sides
# user needs to specify the color of the shape

turtle = turtle.Turtle()
shape = input("choose triangle,circle,or square")
if shape == "triangle":
  def triangle(length,color):
    turtle.speed(1)
    turtle.color(color)
    turtle.forward(50)
    turtle.left(90)
    turtle.left(25)
    turtle.forward(50)
    turtle.left(90)
    turtle.left(30)
    turtle.forward(55)
  c = input("what color black or red")
  l = input("choose a length for the triangle, 100 or 50")
  triangle(c,l)

elif shape == "square":
  def square(length,color):
    turtle.speed(1)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
  c= input("what color black or red")
  l= input("choose a length for the triangle, 100 or 50")
  square(c,l)










