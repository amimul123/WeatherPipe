import requests

api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&minutely_15=temperature_2m"

def fetch_data():
    # Function to fetch weather data from an external API
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        lat = data["latitude"]
        long = data["longitude"]
        time = data["minutely_15"]["time"][0]
        temperature = data["minutely_15"]["temperature_2m"][0]
        return {
            "latitude": lat,
            "longitude": long,
            "time": time,
            "temperature": temperature
        }
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
    # print(lat)
    # print(long)
    # print(time)
    # print(temperature)
    


if __name__ == "__main__":
    fetch_data()# Note: This function is not covered by unit tests due to its dependency on an external API.

    