import gymnasium as gym
from stable_baselines3 import A2C, PPO
import os

from snakeenv import SnakeEnv

models_dir = "models/PPO"
logs_dir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# env = gym.make("LunarLander-v3")
env = SnakeEnv()
env.reset()

# Initialize the model (with MlpPolicy = Multi Layer Perceptron)
# model = A2C("MlpPolicy", env, verbose=1, tensorboard_log=logs_dir)    # A2C is an Actor-Critic algorithm
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logs_dir)    # PPO is an policy gradient algorithm


TIMESTEPS = 10_000

for i in range(1, 30):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS * i}")
    print(f"Saved model to {models_dir}/{TIMESTEPS * i}")


env.close()

'''
!tensorboard --logdirs=logs # to see tensorboard graphs while training.
'''