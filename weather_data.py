#importing requests module
import requests  
city_name=input("Enter the city name:")

#url with city name and API key
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=ab6f61f9d233c5b3ff024d0fba152411&units=metric'  


response_get=requests.get(url)

#checking respose request

if response_get.status_code==200:
        weather_data=response_get.json()

        #getting weather information of the given city

        weather_description=weather_data['weather'][0]['description']     
        coordinates=weather_data['coord']
        temperature=weather_data['main']['temp']
        feels_like=weather_data['main']['feels_like']
        humidity=weather_data['main']['humidity']
        wind_speed=weather_data['wind']['speed']

else:
        print("No response")

#printing the weather information
#         
print(f"Showing weather data for {city_name}....")
print(f"Weather description of is : {weather_description}")
print(f"coordinates are : {coordinates}")
print(f"temperature is : {temperature} celsius and it feels like : {feels_like} celsius")
print(f"Humidity is : {humidity} %")
print(f"Wind speed is : {wind_speed} m/s")