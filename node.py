from kivy.uix.button import Button

# Define some color constants for different types of nodes
class Node(Button):
    EMPTY_COLOR=(1,1,1,1)  # white
    BARRIER_COLOR=(0,0,0,1)  # black
    START_COLOR=(0,1,0,1)  # green
    END_COLOR=(1,0,0,1)  # red
    PATH_COLOR=(0.75,0,0.75,1)  # purple
    OPEN_COLOR=(0,0.5,1,1)  # blue
    CLOSED_COLOR=(0,0.75,1,1)  # light blue
    WEATHER_BARRIER_COLOR=(1,0.5,0,1)  # orange

    def __init__(self,row,col,**kwargs):
        # Initialize the Node with its row and column coordinates
        super(Node,self).__init__(**kwargs)
        self.row=row
        self.col=col
        self.color=Node.EMPTY_COLOR  # Default color is empty (white)

    def __lt__(self,other):
        # Override the less-than operator to return False
        # (this is needed for A* algorithm implementation)
        return False

    def on_color(self,instance,color):
        # When the color property is set, update the button's background color
        self.background_color=color