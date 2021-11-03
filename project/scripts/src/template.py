"""
Template file for building learning algo.
"""

import time
import flappy_bird_gym
import numpy as np

env = flappy_bird_gym.make("FlappyBird-v0")

for episode in range(10): 

    obs = env.reset()

    while True:
        action = env.action_space.sample()  # or given a custom model, action = policy(observation)
        nobs, reward, done, info = env.step(action)
    
        env.render()
        time.sleep(1 / 60)  # FPS

        if done:
            break
    

env.close()