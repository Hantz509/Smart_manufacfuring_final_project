import gymnasium as gym
from gymnasium import spaces
import numpy as np

class ManufacturingEnv(gym.Env):
    def __init__(self):
        super(ManufacturingEnv, self).__init__()
        
        # Action space: 0 = No maintenance, 1 = Perform maintenance
        self.action_space = spaces.Discrete(2)
        
        # Observation space: 3 sensor values (temperature, vibration, pressure)
        self.observation_space = spaces.Box(low=0, high=100, shape=(3,), dtype=np.float32)
        
        # Initial state
        self.state = np.random.uniform(10, 90, size=(3,))
        self.steps = 0
        self.max_steps = 100  # Simulation ends after 100 steps

    def step(self, action):
        # Apply action: perform maintenance (reset state) or do nothing
        if action == 1:  # Perform maintenance
            self.state = np.maximum(self.state - 10, 0)  # Reduce values (reset effect)
            reward = -1  # Maintenance cost
        else:  # No maintenance
            reward = -10 if any(self.state > 80) else 1  # Penalty for failure or small reward
        
import gymnasium as gym
from gymnasium import spaces
import gymnasium as gym
from gymnasium import spaces
import numpy as np

class ManufacturingEnv(gym.Env):
    def __init__(self):
        super(ManufacturingEnv, self).__init__()
        
        # Action space: 0 = No maintenance, 1 = Perform maintenance
        self.action_space = spaces.Discrete(2)
        
        # Observation space: 3 sensor values (temperature, vibration, pressure)
        self.observation_space = spaces.Box(low=0, high=100, shape=(3,), dtype=np.float32)
        
        # Initial state
        self.state = np.random.uniform(10, 90, size=(3,))
        self.steps = 0
        self.max_steps = 100  # Simulation ends after 100 steps

    def step(self, action):
        # Apply action: perform maintenance (reset state) or do nothing
        if action == 1:  # Perform maintenance
            self.state = np.maximum(self.state - 10, 0)  # Reduce values (reset effect)
            reward = -1  # Maintenance cost
        else:  # No maintenance
            reward = -10 if any(self.state > 80) else 1  # Penalty for failure or small reward
        
        # Simulate random sensor increases over time
        self.state += np.random.uniform(0, 5, size=(3,))
        self.steps += 1

        # Check if done
        done = self.steps >= self.max_steps
        truncated = False  # Set truncated to False (no early stopping)

        return self.state, reward, done, truncated, {}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)  # Proper seeding with Gymnasium
        self.state = np.random.uniform(10, 90, size=(3,))
        self.steps = 0
        return self.state, {}

    def render(self, mode="human"):
        print(f"Step: {self.steps}, State: {self.state}")

        
        
        

        



