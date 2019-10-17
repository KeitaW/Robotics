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
        self.G.add_edge('A', 'B', cost=6)
        self.G.add_edge('A', 'C', cost=1)
        self.G.add_edge('A', 'S', cost=2)
        self.G.add_edge('B', 'S', cost=5)
        self.G.add_edge('C', 'S', cost=5)
        self.G.add_edge('B', 'E', cost=4)
        self.G.add_edge('C', 'E', cost=2)
        self.G.add_edge('C', 'D', cost=5)
        self.G.add_edge('D', 'E', cost=1)
        self.G.add_edge('G', 'D', cost=1)
        self.G.add_edge('G', 'E', cost=5)

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
