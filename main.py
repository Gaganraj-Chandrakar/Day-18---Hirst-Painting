# import colorgram
import turtle as t
import random
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

rgb_colors = [
        (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
        (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
        (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
        (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
        (168, 99, 102)
    ]


tim = t.Turtle()
tim.hideturtle()
tim.speed(0)
t.colormode(255)
tim.teleport(-325, -310)
for _ in range(33):
    for _ in range(33):
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        tim.forward(20)
        tim.pendown()
    tim.teleport(-325, tim.ycor() + 20)
my_screen = t.Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)
my_screen.exitonclick()
