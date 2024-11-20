# Import the CMU Graphics package:
from cmu_graphics import *

small_orange_triangle = Polygon(200,150,150,250,250,250, fill='orange')


def onMousePress(centerX,centerY):
    small_orange_triangle.visible= True

def onMouseRelease(centerX,centerY):
    small_orange_triangle.visible= False



# Run program:
cmu_graphics.run()







