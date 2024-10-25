# Import the CMU Graphics package:
from cmu_graphics import *

# Top left, orange color theme with a border width of 2
Rect(130,100,50,50,fill='lightSalmon', border='lemonChiffon', borderWidth=2)
# Top right, gray color theme with a border width of 4
Rect(230,100,50,50,fill='dimGray', border='lightSlateGray', borderWidth=4)
# Bottom left, purple color theme with a border width of 6
Rect(130,200,50,50,fill='darkMagenta', border='orchid', borderWidth=6)
# Center, green color theme with a border width of 8
Rect(230,200,50,50,fill='tan', border='rosyBrown', borderWidth=8)
# Bottom right, brown color theme with a border width of 10
Rect(179,148,50,50,fill='mediumAquamarine', border='lightSeaGreen', borderWidth=10)

# Run program:
cmu_graphics.run()
