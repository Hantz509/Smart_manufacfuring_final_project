from manufacturing_env import ManufacturingEnv

# Initialize the environment
env = ManufacturingEnv()

# Reset the environment to start
state = env.reset()
print("Initial State:", state)

# Test the environment for a few steps
for step in range(10):
    action = env.action_space.sample()  # Randomly choose an action (0 or 1)
    next_state, reward, done, _ = env.step(action)
    print(f"Step {step+1}, Action: {action}, Next State: {next_state}, Reward: {reward}")
    if done:
        print("Episode finished!")
        break

