# Importing required libraries
import os
import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

# Retriving OPENWEATHER_API_KEY from .env file
load_dotenv()

# Getting weather data from API
def get_weather_data(location):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    return data

root = tk.Tk()
root.title("Weather App")
root.geometry('500x150')

# GUI using Tkinter
def fetch_weather():
    location = location_entry.get()
    weather_data = get_weather_data(location)
    
    try:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_condition = weather_data['weather'][0]['description']
        
        result_label.config(text=f"Temperature: {round(temperature -273,2)}°C\nHumidity: {humidity}%\nCondition: {weather_condition.capitalize()}")
    except KeyError:
        messagebox.showerror("Error", "Invalid location. Please try again.")

label = tk.Label(root, text="Enter Location: ")
label.pack()

location_entry = tk.Entry(root)
location_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
