from turtle import*

speed(200)
width(8)
color ("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of the square

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of the door
color("red")

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()
#end of the roof
penup()
goto(60,130)
pendown()
right(60)
color("yellow")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
#end of the first window
penup()
goto(135,130)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)





















exitonclick()