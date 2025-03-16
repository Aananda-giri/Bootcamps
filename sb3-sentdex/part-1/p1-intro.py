import gymnasium as gym
from stable_baselines3 import A2C, PPO

env = gym.make("LunarLander-v3")
env.reset()

# Initialize the model (with MlpPolicy = Multi Layer Perceptron)
# model = A2C("MlpPolicy", env, verbose=1)    # A2C is an Actor-Critic algorithm
model = PPO("MlpPolicy", env, verbose=1)    # A2C is an Actor-Critic algorithm

# Train the model for 2000 steps
model.learn(total_timesteps=2000)   
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


'''
* docs: https://stable-baselines3.readthedocs.io/en/master/

* There is discrete and multi discrete
  * dicrete: one step choice per step
  * multi-step: 8 individual servos (which is multi discrete problem because theere are multiple servos)
'''