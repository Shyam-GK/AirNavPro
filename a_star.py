import heapq
from kivy.uix.button import Button

# Define color constants
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
        super(Node,self).__init__(**kwargs)
        self.row=row
        self.col=col
        self.color=Node.EMPTY_COLOR  # Default color is empty (white)

    def __lt__(self,other):
        return False

    def on_color(self,instance,color):
        self.background_color=color


class AStar:
    def __init__(self,nodes,start_node,end_node,barrier_nodes):
        self.nodes=nodes
        self.start_node=start_node
        self.end_node=end_node
        self.barrier_nodes=barrier_nodes

        self.open_set=[]
        heapq.heappush(self.open_set,(0,self.start_node))

        self.came_from={}
        self.g_scores={node:float('inf') for row in nodes for node in row}
        self.g_scores[start_node]=0
        self.f_scores={node:float('inf') for row in nodes for node in row}
        self.f_scores[start_node]=self.heuristic(start_node,end_node)

        self.open_set_hash={self.start_node}
        self.finished=False

        # count for search length
        self.search_length=0

    def step(self):
        if not self.open_set:
            self.finished=True
            print("No path found.")
            return

        # Increment search length
        self.search_length+=1

        current_node=heapq.heappop(self.open_set)[1]
        self.open_set_hash.remove(current_node)

        if current_node==self.end_node:
            self.finished=True
            path=self.reconstruct_path()
            path_length=len(path)
            print("A* Path Length:",path_length)
            print("A* Search Length:",self.search_length)
            return

        for neighbor in self.get_neighbors(current_node):
            tentative_g_score=self.g_scores[current_node]+self.distance(current_node,neighbor)
            if tentative_g_score<self.g_scores[neighbor]:
                self.came_from[neighbor]=current_node
                self.g_scores[neighbor]=tentative_g_score
                self.f_scores[neighbor]=tentative_g_score+self.heuristic(neighbor,self.end_node)
                
                if neighbor not in self.open_set_hash:
                    heapq.heappush(self.open_set,(self.f_scores[neighbor],neighbor))
                    self.open_set_hash.add(neighbor)
                    if neighbor!=self.end_node:
                        neighbor.color=Node.OPEN_COLOR
                if current_node!=self.start_node:
                    current_node.color=Node.CLOSED_COLOR

    def reconstruct_path(self):
        path=[]
        node=self.end_node
        while node in self.came_from:
            path.insert(0,node)
            node.color=Node.PATH_COLOR
            node=self.came_from[node]
        path.insert(0,self.start_node)
        return path

    def get_neighbors(self,node):
        neighbors=[]
        if node.row>0:
            top_node=self.nodes[node.row-1][node.col]
            if top_node not in self.barrier_nodes:
                neighbors.append(top_node)
        if node.row<len(self.nodes)-1:
            bottom_node=self.nodes[node.row+1][node.col]
            if bottom_node not in self.barrier_nodes:
                neighbors.append(bottom_node)
        if node.col>0:
            left_node=self.nodes[node.row][node.col-1]
            if left_node not in self.barrier_nodes:
                neighbors.append(left_node)
        if node.col<len(self.nodes[0])-1:
            right_node=self.nodes[node.row][node.col+1]
            if right_node not in self.barrier_nodes:
                neighbors.append(right_node)
        return neighbors

    def heuristic(self,node1,node2):
        return abs(node1.row-node2.row)+abs(node1.col-node2.col)

    def distance(self,node1,node2):
        return 1 if node1.row==node2.row or node1.col==node2.col else 1.4