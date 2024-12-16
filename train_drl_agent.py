import gym
from stable_baselines3 import PPO
from manufacturing_env import ManufacturingEnv

# Initialize your custom manufacturing environment
env = ManufacturingEnv()

# Instantiate the PPO model
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
print("Training the DRL agent...")
model.learn(total_timesteps=10000)  # Adjust the number of timesteps if needed
print("Training complete!")

# Save the trained model
model.save("ppo_maintenance_agent")
print("Model saved as 'ppo_maintenance_agent'.")

