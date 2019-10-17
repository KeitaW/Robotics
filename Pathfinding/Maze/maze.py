import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class Maze():
    def __init__(self):
        # state set
        self.S = ['S', 'A', 'B', 'C', 'D', 'E', 'G']
        # action set
        self.A = [
            ('A', 'B'),
            ('A', 'C'),
            ('A', 'S'),
            ('B', 'S'),
            ('C', 'S'),
            ('B', 'E'),
            ('C', 'E'),
            ('C', 'D'),
            ('D', 'E'),
            ('G', 'D'),
            ('G', 'E'),
        ]
        self.G = nx.Graph()
        self.G.add_edge('A', 'B', weight=6)
        self.G.add_edge('A', 'C', weight=1)
        self.G.add_edge('A', 'S', weight=2)
        self.G.add_edge('B', 'S', weight=5)
        self.G.add_edge('C', 'S', weight=5)
        self.G.add_edge('B', 'E', weight=4)
        self.G.add_edge('C', 'E', weight=2)
        self.G.add_edge('C', 'D', weight=5)
        self.G.add_edge('D', 'E', weight=1)
        self.G.add_edge('G', 'D', weight=1)
        self.G.add_edge('G', 'E', weight=5)

    def draw(self):
        pos = nx.spring_layout(G)
        nx.draw(self.G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(self.G, pos)


if __name__ == "__main__":
    graph = Maze()
    graph.draw()
