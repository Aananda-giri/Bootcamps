# pip install gymnasium[box2d]

import gymnasium as gym
from stable_baselines3 import A2C, PPO
import os

models_dir = "models/PPO"
logs_dir = "logs"

model_path = f"{models_dir}/10000.zip"

model = PPO.load(model_path, env=env)

episodes = 10

for ep in range(episodes):
    obs = env.reset()
    done=False
    while not done:
        env.render()
        action, _ = model.predict(obs)
        # obs, reward, done, info = env.step(env.action_space.sample()) # random action
        obs, reward, done, info = env.step(action)
        print(reward)
        if done:
            break
env.close()
