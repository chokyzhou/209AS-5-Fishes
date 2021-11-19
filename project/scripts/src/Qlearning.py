import time
import flappy_bird_gym
import numpy as np
import collections
import math

### Initialize Q-learning
epsilon = 0.1
num_episodes = 10**10

lr = .8
gamma = .95
eps = 0.02
###

def create_bins_and_q_table(env):
	# env.observation_space.high
	# [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38]
	# env.observation_space.low
	# [-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38]

	# remove hard coded Values when I know how to

	numBins = 20
	obsSpaceSize = len(env.observation_space.high)

	# Get the size of each bucket
	bins = [
		np.linspace(-4.8, 4.8, numBins),
		np.linspace(-4, 4, numBins),
		np.linspace(-.418, .418, numBins),
		np.linspace(-4, 4, numBins)
	]

	qTable = np.random.uniform(low=-2, high=0, size=([numBins] * obsSpaceSize + [env.action_space.n]))
	return bins, obsSpaceSize, qTable


# Given a state of the enviroment, return its descreteState index in qTable
def get_discrete_state(state, bins, obsSpaceSize):
	stateIndex = []
	for i in range(obsSpaceSize):
		stateIndex.append(np.digitize(state[i], bins[i]) - 1) # -1 will turn bin into index
	return tuple(stateIndex)

def obs2state(a, b, multiplier=10000):
    return (int(math.ceil(a*multiplier)), int(math.ceil(b*multiplier)))


def main():
    """
    Obs: horizontal distance to the next pipe;
         difference between the player's y position and the next hole's y position.
    """
    
    env = flappy_bird_gym.make("FlappyBird-v0")
    bins, obsSpaceSize, qTable = create_bins_and_q_table(env)
    
    Q = collections.defaultdict(lambda: np.zeros(env.action_space.n))
    
    for episode in range(num_episodes): 

        obs = env.reset()
        #state = get_discrete_state(obs, bins, obsSpaceSize)
        state = obs2state(*obs)
        done = False
        
        cnt = 0
        old_score = 0
        while not done:
            cnt += 1
            if np.random.uniform(0, 1) < epsilon:
                action = env.action_space.sample() # Explore action space
            else:
                action = np.argmax(Q[state]) # Exploit learned values

            next_obs, reward, done, info = env.step(action)
            
            #next_state = get_discrete_state(next_obs, bins, obsSpaceSize)
            next_state = obs2state(*next_obs)
            
            if done or not -10 < next_state[1] < 10:
                reward = -10000
            
            if info['score'] > old_score:
                old_score = info['score']
                reward = 100
            else:
                reward = 0
                
            Q[state][action] = (1 - lr) * Q[state][action] + lr * (reward + gamma * np.max(Q[next_state]))
            
            if episode % 5000 == 0:
                env.render()
                time.sleep(1 / 60)  # FPS
            
            state = next_state
            
        print(episode, info)
        
    env.close()

if __name__ == "__main__":
    main()