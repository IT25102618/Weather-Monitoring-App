import requests

def get_weather(city):
    # The API key here is my own one modifiers must use there own.. ""
    api_key = "efb9e09410b76276e399eb631ce8a39c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Constructing the URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data["main"]
            temp = main["temp"]
            humidity = main["humidity"]
            report = data["weather"][0]["description"]
            
            print(f"\n--- Weather in {city.upper()} ---")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {report.capitalize()}")
        else:
            print("City Not Found!")
            
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
