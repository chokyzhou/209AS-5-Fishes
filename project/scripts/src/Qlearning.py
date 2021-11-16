import time
import flappy_bird_gym
import numpy as np
import collections
import math

### Initialize Q-learning
discount_factor = 0.6
epsilon = 0.2
num_episodes = 10**6

lr = .7
gamma = .95
eps = 0.02
###

def obs2state(x, y, multiplier=100):
    return (int(math.floor(multiplier*x)), int(math.floor(multiplier*y))) 

def main():
    
    env = flappy_bird_gym.make("FlappyBird-v0")
    Q = collections.defaultdict(lambda: np.zeros(env.action_space.n))
    total_reward = 0
    
    for episode in range(num_episodes): 

        obs = env.reset()
        state = obs2state(*obs)
        
        while True:
            if np.random.uniform(0, 1) < epsilon:
                action = env.action_space.sample() # Explore action space
            else:
                action = np.argmax(Q[state]) # Exploit learned values

            next_obs, reward, done, info = env.step(action)
            total_reward += reward
            
            next_state = obs2state(*next_obs)
            Q[state][action] += lr * (reward + gamma *  np.max(Q[next_state]) - Q[state][action])
            
            env.render()
            time.sleep(1 / 100000)  # FPS

            if done:
                break
            
            state = next_state
        
        print(episode, info)
        
    env.close()

if __name__ == "__main__":
    main()