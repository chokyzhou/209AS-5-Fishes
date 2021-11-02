import time
import flappy_bird_gym
env = flappy_bird_gym.make("FlappyBird-v0")

obs = env.reset()
while True:
    # Next action:
    # (feed the observation to your agent here)
    action = env.action_space.sample()
    print(action)

    # Processing:
    obs, reward, done, info = env.step(action)
    
    # Rendering the game:
    # (remove this two lines during training)
    env.render()
    time.sleep(1 / 30)  # FPS
    
    # Checking if the player is still alive
    if done:
        break

env.close()