# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing, draw_vertical_gradient

import math
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    def draw_sky(canvas, x):
        draw_vertical_gradient(canvas, x,0, [255, 215, 0], 800, 500, [255, 174, 250])
        return

    def draw_ground(canvas, x):
        draw_rectangle(canvas, x,0, 800, 50, outline='#458B74', fill='#458B74')
        return 

    def draw_sun(canvas, x):
        draw_oval(canvas, x, 150, 300,250, outline='#FFD700', fill='#FFD700')
        return 

    def draw_cloud(x, y, size=1, color='white'):

        draw_oval(canvas, size * (x + 0) , size * (y + 0), size * (x + 30), size * (y + 30), outline=color, fill=color)
        draw_oval(canvas, size * (x + 60), size * (y + 0), size * (x + 90), size * (y + 30), outline=color, fill=color)
        draw_oval(canvas, size * (x + 15), size * (y + 15), size * (x + 45), size * (y + 45), outline=color, fill=color)
        draw_oval(canvas, size * (x + 45), size * (y + 15), size * (x + 75), size * (y + 45), outline=color, fill=color)
        draw_oval(canvas, size * (x + 30), size * (y + 25), size * (x + 60), size * (y + 55), outline=color, fill=color)
        draw_oval(canvas, size * (x + 10), size * (y + 10), size * (x + 70), size * (y + 40), outline=color, fill=color)

        draw_line(canvas, size * ((x) + 15), size * (y + (30 / 4)), size * (x + 75), size * (y + (30 / 4)), width= size * 15, fill=color)
        return

    def draw_mountain(x, y, z, w, color0= '#66CDAA'):
        draw_oval(canvas, x, y, z, w, outline=color0, fill=color0)

        return

    def draw_tree(x1, x2, y1, y2, z, x0, y0, x01, y01, x02, y02, color1, color3):

        draw_line(canvas, x1, x2, y1, y2, width=z, fill=color1)
        draw_polygon(canvas, x0, y0, x01, y01, x02, y02, outline=color3, fill=color3)

        return 
    
    draw_sky(canvas, 0)
    draw_sun(canvas, 200)

    draw_cloud(400, 430, 1,'#F7F7F7')
    draw_mountain(100, -300, 1100, 250, color0='#7FFFD4')
    draw_mountain(-1100, -200, 500, 250, color0='#76EEC6')
    draw_mountain(300, -200, 1200, 150,color0='#66CDAA')
    draw_ground(canvas, 0)

    draw_cloud(220, 440, 1,'#F7F7F7')
    for i in range(33, 780, 46):
        draw_tree(i, 70, i, 30, 8, i - 20, 45, i + 20, 45, i, 100, color1='#CDC0B0', color3='#228B22')

    for i in range(10, 800, 46):
        draw_tree(i, 70, i, 20, 10, i - 20, 35, i + 20, 35, i, 120, color1='#CDAA7D', color3='#006400')

    draw_cloud(-30, 225, (7/5))

    draw_tree(830, 10, 830, -50, 70, 730, -1, 930, -1, 830, 370, '#76EE00', '#3D9140')
    draw_tree(-50, 10, -50, -10, 70, -200, 10, 70, 10, 10, 470, '#76EE00', '#3D9140')

    
    draw_cloud(130,400, 1,'#F7F7F7')
    draw_cloud(1500, 840, (1/2), '#F0F0F0')
    draw_cloud(1100, 860, (1/2), '#F0F0F0')
    draw_cloud(1100, 860, (1/2), 'pink')

    draw_cloud(550,365, 1, '#F7F7F7')

    draw_cloud(300, 220, (3/2))
    draw_cloud(50, 250, (3/2))

    # Call your drawing functions such
    # as draw_sky and draw_ground here.



    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.



# Call the main function so that
# this program will start executing.
main()