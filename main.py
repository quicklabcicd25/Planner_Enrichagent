
from agents.planner import PlannerAgent
from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.summary_agent import SummaryAgent
from agents.llm_agent import LLMAgent

def main(goal):
    llm = LLMAgent()
    plan = llm.generate_plan(user_goal)

    data = {}
    for step in plan:
        if step == "fetch_spacex":
            spacex = SpaceXAgent()
            data["spacex"] = spacex.get_next_launch()
        elif step == "check_weather":
            weather = WeatherAgent()
            location = data["spacex"]["launchpad"]
            data["weather"] = weather.get_weather(location)
        elif step == "summarize":
            summary = SummaryAgent()
            data["summary"] = summary.evaluate_delay(data["spacex"], data["weather"])

    print("Final Output:\n", data["summary"])

if __name__ == "__main__":
    user_goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."
    main(user_goal)
