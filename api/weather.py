import requests
import sys

def get_weather(lat, lon):
    
    # Reutrn an error if latitude or longitude is not a float
    if not isinstance(lat, float) or not isinstance(lon, float):
        return "Error: Latitude and longitude must be floats."  

    # Check if latitude and longitude are within valid range
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        return "Error: Latitude must be between -90 and 90 and longitude must be between -180 and 180."

 
    try:
        # Send a GET request to the Open-Meteo API
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

    # Parse the JSON response
    data = response.json()

    # Extract the current temperature and time
    temperature = data['current']['temperature_2m']
    time = data['current']['time']

    return temperature, time

    
# Unit test run with pytest to check if the function works properly
def test_get_weather_pytest():
    #assert get_weather(0, 0) == (2.3, 1614864000)
    assert get_weather(1000, 1000) == "Error: Latitude and longitude must be floats."
    assert get_weather("a", "b") == "Error: Latitude and longitude must be floats."
    assert get_weather(0, "b") == "Error: Latitude and longitude must be floats."

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python weather.py [latitude] [longitude]")
        sys.exit()

    # Check that the latitude and longitude are floats and also not null
    try:
        float(sys.argv[1])
        float(sys.argv[2])
    except ValueError:
        print("Error: Latitude and longitude must be floats.")
        sys.exit()

    # Check that the latitude and longitude are within valid range
    if not (-90 <= float(sys.argv[1]) <= 90) or not (-180 <= float(sys.argv[2]) <= 180):
        print("Error: Latitude must be between -90 and 90 and longitude must be between -180 and 180.")
        sys.exit()

    lat = float(sys.argv[1])
    lon = float(sys.argv[2])
    temperature, time = get_weather(lat, lon)
    print(f"Temperature: {temperature}, Time: {time}")

    