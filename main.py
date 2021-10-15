import numpy as np
from gridworld_setup import GridWorld
from simulator import Simulator

if __name__ == "__main__":
    grid = GridWorld()
    simulator = Simulator(grid)
    path = [grid.current_position]
    count = 0
    while (grid.target == grid.current_position).all(1).any() == False:
        grid.current_position = simulator.new_state
        simulator = Simulator(grid)
        path.append(grid.current_position)
        count += 1
    path = np.array([path])
    print("It takes " , count , " steps to reach the ice-cream shop")
    print(path)
