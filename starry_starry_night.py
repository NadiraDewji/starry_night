"""
Nadira Dewji
Sunday Novemever 15, 2015
starry_starry_night.py (15 points)
=====
Draw some stars! 

Requirements
-----

### Part 1

* customize the colors of your drawing (choose whatever colors you like)
    * change the background color
    * set the pen color
* turn animation off (we're going to be drawing a lot of stars)
* set the width and height to 800 width and 600 height
* create a function called __draw star__
    * you can draw whatever star you like
    * the examples show a typical 5 pointed star
    * parameters: x, y and size
    * processing: it will draw a star at the x and y location specified, and the size of the star; you can take that to mean the size of a side (easier), or the entire star 
    * return: does not return anything
    * don't forget to call update at the end of it
* call your function once to draw a star in the middle of the screen

![star middle](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_1.png)

### Part 2

* comment out your function call for drawing a single star from the previous part
* now, instead of drawing a single star, draw several stars using a for loop
* they can be drawn in a straight line horizontally or vertically
* or... if you want to get fancy, draw them in a curve
* see the examples below:

![stars in a row](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_2.png)

![stars curved](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_3.png)

### Part 3

* again, comment out your code for drawing several stars from the previous part
* now, create another function called __generate_star_data__
    * this function will generate a list of lists that represents star data:
        * the first element in the sub list will represent an x value, the second represents a y value, and the last represents size
        * for example, [[0, 0, 10], [200, 200, 80]] represents 2 stars, one at the origin... and a larger star on the upper right hand corner
    * parameters: an int that represents the number of elements in the list (the number stars / sub lists)
    * processing: 
        * it will randomly generate x, y, and size values, put these values into a list... 
        * and add this three element list to the star list (the list of lists)
        * the bounds of the random numbers that you generate can be hard coded based on the width and height of the window
    * return: the list of lists representing stars
* example usage below:

<pre>
star_data = generate_star_data(2)
print(star_data)
# prints out: [[-250, 121, 49], [100, 0, 20]] 
</pre>

### Part 4

* use the function from the previous part to generate a list of 40 stars (a list of 40 sub lists)
* save the result of this into a global variable (that is, it should be a variable defined outside of all of your functions)
* create a function called draw_sky:
    * within it, iterate through the global list you created 
    * draw a star based on the data in the sub list (x, y and size)
* call you draw_sky function once...
* it should look something like this:

![lots of stars](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_4.png)

Extra Credit
-----
5 points

* within your draw sky function, increment the x value of every sub list by 1 as you iterate through the sub lists to draw stars
* instead of calling your draw_sky function once, use ontimer to have you draw_sky function call itself again in 30 ms
    * call ontimer at the end of your draw_sky function
    * with draw_sky as the first argument (no quotes), and 30 as the second
* you should see an animation!
* now... change your generate_star_data function so that the sub list that creates also contains a 4th value
    * this value represents a velocity
    * it should be small (maybe between 1 and 5)
* in your draw_sky function, as you iterate through your list of star data, add the generated velocity (the value at index 3) to the x value (the value at index 0) rather than just increment by 1

![animation](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_ec.gif)
"""
#import the turtle module and set up a variable for the turtle
#and then also set a variable for turtle.Turtle()
#make the window size what is required.
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
wn.setup(800, 600)
t.color("yellow")
wn.bgcolor("black")
t.pensize(2)
t.hideturtle()
wn.tracer(0)

#to make the star use two triangles and allow them to over lap the opposite direction

def triangle(side_length):
    a = 360/3
    for num in range(3):
        t.forward(side_length)
        t.right(a)
#to draw the star you have to change the size so that's it poportional each time.
#to do this set up a ratio so that is poportional.
#the ratio is size/45 * 30

def draw_star(x, y, size):
    t.setheading(0)
    t.up()
    t.goto(x,y)
    t.down()
    triangle(size)
    t.up()
    t.right(90)
    t.forward(size/45 * 30)
    t.right(210)
    t.down()
    triangle(size)

#part 2 is commented out so that the extra credit can work without overlap, but it works!
"""
#part 2

for i in range(1,10):
    draw_star(-250+30*i,-250+30*i,15*i)
"""  

#to make the star you need to make a list of lists that are made up of random coordinates
#the random is to generate random values for the coordinates.
#i made the size between 15, 100 i did not want them to bee too large
#there is a fourth value that is used to increment the x coordinate each time so it moves

#part 3
import random
def star_data(number_of_elements):
    main_list = []
    for i in range(number_of_elements):
        sub_list =[]
        x = random.randint(-370, 370)
        sub_list.append(x)
        y = random. randint(-270,270)
        sub_list.append(y)
        size = random.randint(15, 100)
        sub_list.append(size)
        four = random.randint(1,5)
        sub_list.append(four)
        main_list.append(sub_list)
    return main_list

#part 4 is commented out so that the extra credit can function without overlap but works
#the draw star requires 3 values, and it is repeated 40 times because of star data.
#it goes through each sublist within the list and prints out the values to make the star

#part 4


the_stars = star_data(40)
"""
def draw_sky(the_stars):
    for sub_list in the_stars:
        draw_star(sub_list[0], sub_list[1], sub_list[2])
    

draw_sky(the_stars)
"""

#EXTRA CREDIT!!!!!!
#so the extra credit requires motion
#move each star a certain length to the right using the x coordinate
#then clear the previous star using t.clear
#the motion time will be 30*i and will be a for loop so it can continue and move.

def draw_sky():
    t.clear()
    for sub_list in the_stars:
        sub_list[0] = sub_list[0]+sub_list[3]
        draw_star(sub_list[0], sub_list[1], sub_list[2])
    
for i in range(99):
    wn.ontimer(draw_sky,30*i)
    t.clear()

wn.mainloop()
