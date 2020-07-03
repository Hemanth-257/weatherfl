from flask import Flask, request
from flask import render_template
import requests

app = Flask(__name__,template_folder="templates",static_folder="static")

names = ["Hemanth","Vijay","Tej","Harish"]

@app.route("/", methods=["GET","POST"])
def weather():
      if request.method =="GET":
        return render_template("app.html")
      elif request.method =="POST":
        weather_details = get_weather(request.form['loct'])
        print (weather_details)
        return render_template("index.html" , weather_details=weather_details , location=request.form['loct'])


def get_weather(city):
    url= "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric" + "&appid=46e377ba3b7a64273badab88a86e1900"
    json_response = requests.get(url).json()
    weather_description = json_response["weather"] [0] ["description"]
    temp = json_response["main"] ["temp"]
    return {"description": weather_description,"temp":temp}

if __name__=='__main__':
    app.run(port=5000, debug=True)