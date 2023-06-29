import requests

api_key = "1db7fb7e0f7db72159ed68f0f76fa28d"

def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo"))