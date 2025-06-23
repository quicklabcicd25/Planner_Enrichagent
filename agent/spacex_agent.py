import requests

class SpaceXAgent:
    def get_next_launch(self):
        url = "https://api.spacexdata.com/v4/launches/next"
        response = requests.get(url)
        data = response.json()
        return {
            "name": data.get("name"),
            "date": data.get("date_utc"),
            "launchpad": self.get_launchpad_location(data.get("launchpad"))
        }

    def get_launchpad_location(self, launchpad_id):
        url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
        response = requests.get(url)
        data = response.json()
        return {
            "name": data.get("name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude")
        }
