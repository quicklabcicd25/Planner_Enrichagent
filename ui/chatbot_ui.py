import streamlit as st
import sys
import os

# ✅ Add agents/ to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.llm_agent import LLMAgent
from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.summary_agent import SummaryAgent

st.set_page_config(page_title="🚀 Multi-Agent AI Chatbot", layout="centered")
st.title("🧠 Multi-Agent AI Chatbot (LLM Enhanced)")

user_goal = st.text_input("🎯 Enter your goal (e.g., Find next SpaceX launch and if weather may delay it)")

if st.button("Run Agents") and user_goal:
    with st.spinner("Planning with LLM..."):
        llm = LLMAgent()
        plan_steps = llm.generate_plan(user_goal)

        data = {}
        messages = []

        for step in plan_steps:
            step = step.lower()
            if "spacex" in step or "launch" in step:
                spacex = SpaceXAgent()
                data["spacex"] = spacex.get_next_launch()
                messages.append(f"🛰️ Launch: **{data['spacex']['name']}** at **{data['spacex']['launchpad']['name']}**")
            elif "weather" in step:
                weather = WeatherAgent()
                location = data.get("spacex", {}).get("launchpad", None)
                if location:
                    data["weather"] = weather.get_weather(location)
                    messages.append(f"🌤️ Weather: {data['weather']['description']} ({data['weather']['temp']}°C)")
            elif "summary" in step or "delay" in step:
                summary = SummaryAgent()
                if "spacex" in data and "weather" in data:
                    result = summary.evaluate_delay(data["spacex"], data["weather"])
                    data["summary"] = result
                    messages.append(f"📋 Summary: {result}")

    st.markdown("## 🧾 Results")
    for msg in messages:
        st.success(msg)

if __name__ == "__main__":
    pass  # Streamlit doesn't need a main() here; it's handled by the CLI
