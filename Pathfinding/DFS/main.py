from Pathfinding.Maze.maze import Maze


class DFS():
    def __init__(self):
        self.maze = Maze()
        self.state = "S"
        self.open_list = [self.state]
        self.close_list = []

    def search(self):
        while self.open_list is not None:
            print("Open list", self.open_list)
            print("Close list", self.close_list)
            state = self.open_list.pop(0)
            if state == "G":
                return
            self.close_list.append(state)
            self.open_list += [state for state in self.maze.get_actions(
                state) if state not in self.close_list]


if __name__ == "__main__":
    print("Started")
    dfs = DFS()
    print("Graph", dfs.maze.G)
    dfs.search()
    print("Graph", dfs.maze.G)
    dfs.maze.draw()
