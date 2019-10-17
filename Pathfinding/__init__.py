from Pathfinding.Maze.maze import Maze


class BFS(Maze):
    def __init__(self):
        self.state = "S"
        self.open_list = self.S
        self.close_list = []

    def bfs(self):
        pass
