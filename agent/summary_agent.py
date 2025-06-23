class SummaryAgent:
    def evaluate_delay(self, launch_data, weather_data):
        delay_possible = "rain" in weather_data["description"].lower() or weather_data["temp"] < -10
        return f"Launch '{launch_data['name']}' on {launch_data['date']} at {launch_data['launchpad']['name']} — Weather: {weather_data['description']}. " + \
               ("Delay likely." if delay_possible else "No delay expected.")
