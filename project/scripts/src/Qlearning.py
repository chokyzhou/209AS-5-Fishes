import time
import flappy_bird_gym
import numpy as np
import collections
import math

class QLearning:
    

    def __init__(self) -> None:
        self.main()
    
    def obs2state(self,a, b, multiplier=100):
        return (int(math.ceil(a*multiplier)), int(math.ceil(b*multiplier)))

    def act(self, env, cur_epsilon, Q, state):
        if np.random.uniform(0, 1) < cur_epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(Q[state]) # Exploit learned values
        return action
    
    def main(self,):
        """
        Obs: horizontal distance to the next pipe;
            difference between the player's y position and the next hole's y position.
        """
        ### Initialize Q-learning
        initialEpsilon = 0.1
        num_episodes = 10**10

        lr = .9
        gamma = .95
        ###
        
        env = flappy_bird_gym.make("FlappyBird-v0")
        
        env.observation_space.sample
        
        Q = collections.defaultdict(lambda: np.zeros(env.action_space.n))
        
        for episode in range(num_episodes): 

            obs = env.reset()
            #state = get_discrete_state(obs, bins, obsSpaceSize)
            state = self.obs2state(*obs)
            done = False
            gameIter = []

            epsilon = initialEpsilon / (episode + 1) 
            #epsilon = initialEpsilon
                           
            while not done:
                
                action = self.act(env, epsilon, Q, state)

                next_obs, reward, done, info = env.step(action)
                
                #next_state = get_discrete_state(next_obs, bins, obsSpaceSize)
                next_state = self.obs2state(*next_obs)
                
                if done:
                    reward = -10000
                
                if info['score']:
                    reward = 100 * info['score']
                
                gameIter.append((state, action, reward, next_state))
                
                if episode % 5000 == 0:
                    env.render()
                    time.sleep(1 / 60)  # FPS
                
                state = next_state
            
            for (state, action, reward, next_state) in gameIter:
                Q[state][action] = (1 - lr) * Q[state][action] + lr * (reward + gamma * np.max(Q[next_state]))

            #lr *= (episode+1) / (episode+2)
            print(episode, info)
            
        env.close()

if __name__ == "__main__":
    agent = QLearning()
    agent.main()