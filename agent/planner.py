class PlannerAgent:
    def create_plan(self, goal: str):
        steps = []
        if "spacex" in goal.lower():
            steps.append("fetch_spacex")
        if "weather" in goal.lower():
            steps.append("check_weather")
        if "summarize" in goal.lower() or "delay" in goal.lower():
            steps.append("summarize")
        return steps
