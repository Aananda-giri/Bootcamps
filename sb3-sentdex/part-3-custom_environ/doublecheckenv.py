from stable_baselines3.common.env_checker import check_env
from snakeenv import SnakeEnv

env = SnakeEnv()
episodes = 50

for episode in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        random_action = env.action_space.sample()
        print(f"action: ", random_action)
        obs, reward, done, info = env.step(random_action)
        print(f'reward: {reward}')
        env.render()
env.close()
