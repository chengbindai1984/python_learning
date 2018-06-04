import turtle

def draws_sqaure():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.forward(100)
    brad.right (90)
    brad.forward(100)
    brad.right (90)
    brad.forward(100)
    brad.right (90)
    brad.forward(100)
    brad.right (90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)


    window.exitonclick()

draws_sqaure()