# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
from draw2d import start_drawing, draw_oval, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)


    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas,0,100,scene_width,scene_height)

    draw_ground(canvas,0,0,scene_width,100)

    draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas,left,bottom,right,top):
    draw_rectangle(canvas,left,bottom,right,top,width=0,fill="dodgerBlue3")
    draw_cloud(canvas,400,350,500,400)
    draw_sun(canvas,700,300,750,350)
    for x in range(0,800,50):
        draw_cloud(canvas,x,550,10,300)
    draw_rain(canvas,0,200,10,200)

def draw_ground(canvas,left,bottom,right,top):
    draw_rectangle(canvas,left,bottom,right,top,width=0,fill="green")
    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    draw_rock(canvas,0,50,50,100)

def draw_cloud(canvas,x0,y0,x1,y1):
    draw_oval(canvas,x0,y0,x1,y1,fill="ivory4")

def draw_sun(canvas,x0,y0,x1,y1):
    draw_oval(canvas,x0,y0,x1,y1,fill="gold1")

def draw_rain(canvas,x0,y0,x1,y1):
    draw_oval(canvas,x0,y0,x1,y1)
    scene_width = 799
    scene_height = 650
    
    diameter = 15
    space = 5
    interval = diameter + space

    # Draw a row of circles with
    # some of the circles missing.
    x = 100
    y = 75
    for i in range(20):
        number = random.randint(1, 5)
        if number > 1:
            draw_oval(canvas, x, y,
                    x + diameter, y + diameter, fill="yellow2")
        x += interval

    half_height = round(scene_height / 2)
    min_diam = 5
    max_diam = 10

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(100):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="royalBlue4")

   


def draw_rock(canvas,x0,y0,x1,y1):
    draw_oval(canvas,x0,y0,x1,y1,fill="seashell3")
    scene_width = 799
    scene_height = 100
    
    diameter = 15
    space = 5
    interval = diameter + space

    # Draw a row of circles with
    # some of the circles missing.
    x = 100
    y = 75
    for i in range(5):
        number = random.randint(1, 5)
        if number > 1:
            draw_oval(canvas, x, y,
                    x + diameter, y + diameter, fill="red3")
        x += interval

    half_height = round(scene_height / 2)
    min_diam = 15
    max_diam = 20

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(50):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="seashell4")

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)



# Call the main function so that
# this program will start executing.
main()