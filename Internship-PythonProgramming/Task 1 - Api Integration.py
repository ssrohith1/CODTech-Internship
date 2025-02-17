import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# OpenWeatherMap API details
API_KEY = "d4f8f2d1cef80583eb863635aa55134e"
CITY = "chennai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching data from API
response = requests.get(URL)
data = response.json()

# Debugging: Print API response
print(data)

# Check for API errors
if data.get("cod") != "200":
    print(f"API Error: {data.get('message', 'Unknown error')}")
    exit()
# Check if 'list' key exists
if 'list' not in data:
    print("Error: 'list' key not found in response. Check API key and city name.")
    exit()

# Extract relevant data
times = []
temperatures = []

for item in data['list']:
    times.append(datetime.datetime.fromtimestamp(item['dt']))
    temperatures.append(item['main']['temp'])

# Creating visualization
sns.set_style("darkgrid")
plt.figure(figsize=(10, 5))
sns.lineplot(x=times, y=temperatures, marker="o", linestyle="-", label="Temperature (°C)")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Forecast for {CITY}")
plt.xticks(rotation=45)
plt.legend()
plt.show()