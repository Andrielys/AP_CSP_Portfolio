# Import the CMU Graphics Package:
from cmu_graphics import *

# Change size of the circle
Circle(200,200,150)



# Two ears, add a border, fill in with a gradient
Circle(80,80,65, fill=gradient('darkGreen','mediumSeaGreen', start='left-top'), border='black', borderWidth=7)
Circle(320,80,65, fill=gradient('darkGreen','mediumSeaGreen', start='right-top'), border='black', borderWidth=7)

# Circle overllaping the ears
Circle(200,200,150)


# One eye
Oval(200,150,120,167, fill=gradient('White', 'white', 'gray'))
# A snout

# A nose

# A mouth

# 9 grey stiches 

# Run program:
cmu_graphics.run()
