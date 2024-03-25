from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import requests
import json

root = Tk()
root.title('Codemy.com - Lear To Code!')
root.geometry("400x100")

def zipLookup():
    try: 
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=" + key.get())
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#FF9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"     
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 15), background=weather_color)
        myLabel.grid(row=2, column=0, columnspan=2)
        root.configure(backgroun=weather_color)                      
    except Exception as e:
        print(e)
    
    
key = Entry(root)
key.grid(row=0, column=0, columnspan=2)    
    
    
zip = Entry(root)
zip.grid(row=1,column=0)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=1, column=1)


root.mainloop()