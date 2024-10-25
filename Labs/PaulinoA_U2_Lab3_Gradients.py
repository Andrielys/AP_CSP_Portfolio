# Import the CMU Graphics package:
from cmu_graphics import *




Rect(0,10,300,50, fill=gradient('deepPink', 'orange', 'yellow', start='center'))
Rect(150,50,250,50, fill=gradient('purple', 'black', start='top'))
Rect(0,100,300,50, fill=gradient('pink', 'purple', 'blue', start='bottom'))
Rect(150,150,250,50, fill=gradient('blue', 'white', 'yellow','black', start='left'))
Rect(0,200,300,50, fill=rgb(220, 20, 60,))



# Run program:
cmu_graphics.run()
