import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class Maze():
    def __init__(self):
        self.G = nx.Graph()
        self.G.add_node("S", pred_score=8)
        self.G.add_node("A", pred_score=4)
        self.G.add_node("B", pred_score=2)
        self.G.add_node("C", pred_score=3)
        self.G.add_node("D", pred_score=1)
        self.G.add_node("E", pred_score=1)
        self.G.add_node("G", pred_score=0)
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

    def get_actions(self, state):
        return list(self.G.neighbors(state))

    def draw(self):
        pos = nx.spring_layout(self.G)
        labels = nx.get_node_attributes(self.G, 'pred_score')
        labels = {name: f"{name}({pred_score})" for name,
                  pred_score in labels.items()}
        nx.draw(self.G, pos, labels=labels, with_labels=True, node_size=900)
        nx.draw_networkx_edge_labels(self.G, pos)


if __name__ == "__main__":
    graph = Maze()
    graph.draw()
    print(list(graph.get_actions('S')))
