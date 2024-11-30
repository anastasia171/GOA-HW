from turtle import*

setup(width=1.0, height=1.0)
bgcolor("darkblue")
width(9)
speed(5)

#border
penup()
goto(0,300)
pendown()
forward(200)
right(90)
forward(400)
right(90)
forward(400)
right(90)
forward(400)
right(90)
forward(400)


penup()
goto(0,100)
pendown()
left(45)
forward(200)
right(180)
forward(400)

#name
#L
penup()
goto(-125,-150)
pendown()

left(45)
forward(100)
left(90)
forward(50)

#P
penup()
goto(-25,-250)
pendown()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

#B
penup()
goto(75,-150)
pendown()
left(90)
forward(100)
left(90)
forward(15)
circle(25 , extent=180)
forward(15)
left(180)
forward(15)
circle(25 , extent=180)
forward(15)


#middle L
color("blue")
penup()
goto(50,50)
pendown()
left(90)
forward(100)
left(90)
forward(50)

#lari
penup()
goto(-150,150)
pendown()
forward(150)
left(90)
forward(75)
left(90)
forward(150)
left(90)
forward(75)


exitonclick()
