import gymnasium as gym
from stable_baselines3 import PPO
from manufacturing_env import ManufacturingEnv

# Load the trained environment
env = ManufacturingEnv()

# Load the trained PPO model
model = PPO.load("ppo_maintenance_agent.zip")

# Run a few test episodes
obs, _ = env.reset()
done = False
import gymnasium as gym
from stable_baselines3 import PPO
from manufacturing_env import ManufacturingEnv

# Load the trained environment
env = ManufacturingEnv()

# Load the trained PPO model
model = PPO.load("ppo_maintenance_agent.zip")

# Run a few test episodes
obs, _ = env.reset()
done = False
total_reward = 0
steps = 0

print("Testing the trained PPO agent...")

while not done:
    action, _ = model.predict(obs)
    obs, reward, done, truncated, _ = env.step(action)
    total_reward += reward
    steps += 1
    env.render()

print(f"Test completed in {steps} steps with a total reward: {total_reward}")




