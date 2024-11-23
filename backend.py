import requests

API_KEY = "5fa6bf3a4ae5bbacd8e7ae6a58d25cc4"

def get_data(place, forecast_day):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    reponse = requests.get(url)
    data = reponse.json()
    filter_data = data["list"]
    nr_values = 8 * forecast_day
    filter_data = filter_data[:nr_values]
    return filter_data


if __name__ == "__main__":
    print(get_data(place="ahmedabad", forecast_day=2))