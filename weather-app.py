from tkinter import *
import requests

root = Tk()
root.title('Weather App: Siphenkosi')
root.geometry("400x300")


def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = 'f12f1c3b6c309591f01c770ac2b401df'
    location = loc_entry.get()
    par = {'appid': api_key, 'q': location, 'units': 'Metric'}
    result = requests.get(url, params=par)
    weather = result.json()
    # print(weather['sys'])
    temp_out.config(text=str((weather['main']['temp'])))
    humid_out.config(text=str((weather['main']['humidity'])))
    descript_out.config(text=str((weather['weather'][0]['description'])))
    print(weather['weather'])


header = Label(root, text="Weather App", font=("arial", 20, "bold")).place(x=115, y=10)

loc_lbl = Label(root, text="Location: ", font=("arial", 12, "bold")).place(x=20, y=70)
loc_entry = Entry(root, width=30)
loc_entry.place(x=100, y=70)

res_btn = Button(root, text="Show Weather", bg="powderblue", fg="white", command=get_weather).place(x=150, y=100)

temp_lbl = Label(root, text="Temperature: ").place(x=20, y=130)
temp_out = Label(root)
temp_out.place(x=140, y=130)

humid_lbl = Label(root, text="Humidity: ").place(x=20, y=160)
humid_out = Label(root)
humid_out.place(x=140, y=160)

wind_lbl = Label(root, text="Wind Speed: ").place(x=20, y=190)
wind_out = Label(root)
wind_out.place(x=140, y=190)

cloud_lbl = Label(root, text="Cloud cover: ").place(x=20, y=220)
cloud_out = Label(root)
cloud_out.place(x=140, y=220)

descript_lbl = Label(root, text="Description: ").place(x=20, y=250)
descript_out = Label(root)
descript_out.place(x=140, y=250)

root.mainloop()
