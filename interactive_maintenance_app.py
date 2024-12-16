import os
import streamlit as st
import numpy as np
from stable_baselines3 import PPO
from manufacturing_env import ManufacturingEnv
import gtts
from playsound import playsound

# Function to handle text-to-speech safely
def speak_action(text):
    # Ensure no leftover audio file exists
    if os.path.exists("action.mp3"):
        os.remove("action.mp3")
    
    # Generate speech
    tts = gtts.gTTS(text)
    tts.save("action.mp3")
    
    # Play the sound file
    playsound("action.mp3", block=True)

# Load trained model
model = PPO.load("ppo_maintenance_agent")

# Streamlit UI
st.title("🚀 Interactive Predictive Maintenance Simulator 🚀")

# Sidebar sliders
st.sidebar.header("Adjust Equipment Parameters")
temperature = st.sidebar.slider("Temperature", 10, 100, 50)
vibration = st.sidebar.slider("Vibration", 0, 50, 25)
pressure = st.sidebar.slider("Pressure", 0, 50, 25)

# Current sensor readings
sensor_state = np.array([temperature, vibration, pressure])
st.subheader("Current Sensor Readings")
st.write(f"Temperature: {temperature}, Vibration: {vibration}, Pressure: {pressure}")

# Initialize environment
env = ManufacturingEnv()
obs, _ = env.reset()
obs = sensor_state

# Model decision
action, _ = model.predict(obs)
action_text = "Perform Maintenance" if action == 1 else "No Maintenance Needed"

# Display the model's decision
st.subheader("Model Decision")
st.write(f"**Action:** {action_text}")

# Safely trigger the TTS function
speak_action(action_text)

# Simulate environment step
next_state, reward, done, _, _ = env.step(action)
st.subheader("System Feedback")
st.write(f"**Reward:** {reward}")
st.write(f"**Next State:** {next_state}")

# Visualize state transition
st.line_chart([sensor_state, next_state], use_container_width=True)

