import requests
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock
#from node import Node
from a_star import AStar

from kivy.uix.button import Button

# Define some color constants
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
        # Initialize the Node 
        super(Node,self).__init__(**kwargs)
        self.row=row
        self.col=col
        self.color=Node.EMPTY_COLOR

    # Override the less-than
    def __lt__(self,other):
        return False

    def on_color(self,instance,color):
        # update the button's background color
        self.background_color=color


def get_weather_data(city_name,api_key):
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    complete_url=f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}'
    response=requests.get(complete_url)
    if response.status_code==200:
        return response.json()
    else:
        print("Failed to fetch weather data")
        return None

class Grid(GridLayout):
    rows=50
    cols=50
    speed=NumericProperty(0.001)
    running=BooleanProperty(False)
    api_key="20da5dc6c03388baf951dcaeeeb97d02"  

    def __init__(self,**kwargs):
        super(Grid,self).__init__(**kwargs)
        self.nodes=[]
        for row in range(self.rows):
            self.nodes.append([])
            for col in range(self.cols):
                node=Node(row,col)
                node.bind(on_release=self.node_clicked)
                self.add_widget(node)
                self.nodes[row].append(node)
        self.start_node=None
        self.end_node=None
        self.barrier_nodes=set()
        self.weather_barrier_nodes=set()
        self.algorithm=None
        self.path=None
        self._keyboard=Window.request_keyboard(self.keyboard_closed,self)
        self._keyboard.bind(on_key_up=self.on_keyboard_up)
        self.place_weather_barriers("New York")  #city name
    def place_weather_barriers(self,city_name):
        weather_data=get_weather_data(city_name,self.api_key)
        if weather_data:
            print("Weather data fetched successfully:",weather_data)
            # Place barriers if it's raining
            if "rain" in weather_data["weather"][0]["main"].lower():
                print("Placing barriers due to rain")
                for row in range(self.rows):
                    for col in range(self.cols):
                        if row%3==0 and col%3==0:
                            node=self.nodes[row][col]
                            node.color=Node.WEATHER_BARRIER_COLOR
                            self.weather_barrier_nodes.add(node)
                            self.barrier_nodes.add(node)

    def node_clicked(self,node):
        if not self.start_node:
            self.start_node=node
            self.start_node.color=Node.START_COLOR
        elif not self.end_node:
            self.end_node=node
            self.end_node.color=Node.END_COLOR
        else:
            if node in self.barrier_nodes:
                self.barrier_nodes.remove(node)
                node.color=Node.WEATHER_BARRIER_COLOR
            elif node==self.start_node or node==self.end_node:
                pass
            else:
                self.barrier_nodes.add(node)
                node.color=Node.BARRIER_COLOR

    def start_algorithm(self):
        if self.running:
            return
        self.algorithm=AStar(self.nodes,self.start_node,self.end_node,self.barrier_nodes)
        self.running=True
        Clock.schedule_interval(self.step_algorithm,self.speed)

    def step_algorithm(self,dt):
        if self.algorithm.finished:
            self.path=self.algorithm.reconstruct_path()
            self.draw_path()
            self.running=False
            return False
        else:
            self.algorithm.step()
            return True

    def draw_path(self):
        if not self.path:
            return
        for node in self.path:
            if node!=self.start_node and node!=self.end_node:
                node.color=Node.PATH_COLOR

    def reset(self):
        for row in range(self.rows):
            for col in range(self.cols):
                node=self.nodes[row][col]
                node.color=Node.EMPTY_COLOR
        self.start_node=None
        self.end_node=None
        self.barrier_nodes=set()
        self.weather_barrier_nodes=set()
        self.algorithm=None
        self.path=None
        self.running=False
        self.place_weather_barriers("New York") 

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard=None

    def on_keyboard_up(self,keyboard,keycode):
        if keycode[1]=='spacebar':
            self.start_algorithm()
        elif keycode[1]=='enter':
            self.reset()
        return True

class AStarApp(App):
    def build(self):
        return Grid()

if __name__=='__main__':
    AStarApp().run()