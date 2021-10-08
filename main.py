import numpy as np
from gridworld_setup import GridWorld
from simulator import Simulator

if __name__ == "__main__":
    grid = GridWorld()
    simulator = Simulator(grid,[2,4])
    transit_p = simulator.transistion_probability()
    print(transit_p.shape)