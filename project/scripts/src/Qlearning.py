import time
import flappy_bird_gym
import numpy as np

env = flappy_bird_gym.make("FlappyBird-v0")


### Initialize Q-learning
Q = np.zeros([2,2])
alpha = 0.1
gamma = 0.6
epsilon = 0.1
###

for episode in range(10): 

    obs = env.reset()

    print(obs)

    while True:
        TODO
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(Q[obs]) # Exploit learned values

        next_obs, reward, done, info = env.step(action)
    
        env.render()
        time.sleep(1 / 60)  # FPS

        if done:
            break
    
    print()
    input()


env.close()