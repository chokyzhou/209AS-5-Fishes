import numpy as np
from gridworld_setup import GridWorld
from simulator import Simulator

if __name__ == "__main__":
    grid = GridWorld()
    print(grid.transition_probability.shape)
    print(grid.transition_probability[4][0])