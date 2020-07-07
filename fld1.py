from flask import Flask, request,jsonify
from flask import render_template
import requests
from logging.handlers import RotatingFileHandler

app = Flask(__name__,template_folder="templates",static_folder="static")

file_handler = RotatingFileHandler("error.log", maxBytes=1024 * 1024 * 100)
app.logger.addHandler(file_handler)

@app.route("/", methods=["GET","POST"])
def weather():
    return render_template("app.html")

@app.route("/api/get_weather", methods=['GET'])
def get_weather():
    city = request.args.get("city")
    weather = get_weather_record_fr_app(city)
    return jsonify(weather)

def get_weather_record_fr_app(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric" + "&appid=46e377ba3b7a64273badab88a86e1900"
    json_response = requests.get(url).json()
    weather_description = json_response["weather"] [0] ["description"]
    temp = json_response["main"] ["temp"]
    return [weather_description,temp]

@app.errorhandler(500)
def handle_500_err(exception):
    app.logger.error(exception)
    return "We are working on the Fix."

if __name__=='__main__':
    app.run(port=5000)