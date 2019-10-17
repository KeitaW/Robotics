from Pathfinding.Maze.maze import Maze


class DFS(Maze):
    def __init__(self):
        self.state = "S"
        self.open_list = [self.state]
        self.close_list = []

    def dfs(self):
        while self.open_list is not None:
            print("Open list", self.open_list)
            print("Close list", self.close_list)
            state = self.open_list.pop(0)
            if state == "G":
                return
            self.close_list.append(state)
