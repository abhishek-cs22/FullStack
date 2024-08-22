

import json
with open("country.json") as file:
    resume=json.load(file)
    # for key, value in resume.items():
    #     print(key, value)
    for state in afghan_states:
        name = state["name"]
        state_code = state["state_code"]
        latitude = state["latitude"]
        longitude = state["longitude"]
        print(f"State: {name}, State Code: {state_code}, Latitude: {latitude}, Longitude: {longitude}")