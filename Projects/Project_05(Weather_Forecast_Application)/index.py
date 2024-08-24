import random


class WeatherCondition:
    def __init__(self, condition, temperature):
        self.condition = condition
        self.temperature = temperature

    def __str__(self):
        return f"{self.condition} with a temperature of {self.temperature}°C"

class WeatherForecast:
    def __init__(self, city):
        self.city = city
        self.conditions = [
            WeatherCondition("Sunny",random.randint(31, 50)),
            WeatherCondition("Cloudy", random.randint(20, 30)),
            WeatherCondition("Rainy", random.randint(14, 25)),
            WeatherCondition("Foggy", random.randint(1,13)),
            WeatherCondition("Snowy", random.randint(-15,0))
        ]

    def get_forecast(self):
        return random.choice(self.conditions)

    def display_forecast(self):
        forecast = self.get_forecast()
        print(f"The weather forecast for {self.city} is: {forecast}")


def run_weather_app():
    city = input("Enter the name of the city: ")
    weather_forecast = WeatherForecast(city)
    weather_forecast.display_forecast()


run_weather_app()
