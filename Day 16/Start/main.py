from turtle import *
import prettytable


'''
class
 has attributes
 does methods 
object    
'''

'''
my_turtle = Turtle()
my_turtle.shape("turtle")
my_screen = Screen()
print(my_screen.canvheight)


for steps in range(100):
    for c in ('blue', 'red', 'green'):
        my_turtle.color(c)
        my_turtle.forward(steps)
        my_turtle.right(30)

my_screen.exitonclick()
'''

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squitle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
table.valign = "t"
print(table)
