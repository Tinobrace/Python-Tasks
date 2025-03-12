import requests
API_KEY = "9fa06612c868eb964860008e7cf9ccad"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print("Full API Response:", data)  # Debugging: Print the full response

    if response.status_code == 200:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        print(f"Weather in {city}: Temperature: {temp}°C Condition: {condition} Humidity: {humidity}%")
    else:
        print(f"Could not fetch weather data for {city}. Error: {data.get('message', 'Unknown error')}")

city = input("Enter city name: ")
get_weather(city)

