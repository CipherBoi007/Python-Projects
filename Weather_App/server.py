from flask import Flask, request, jsonify, render_template, send_from_directory
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY').strip()

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units={units}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            return jsonify({'error': data.get('message', 'Failed to fetch weather data')}), response.status_code
        
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure'],
            'unit': '°C' if units == 'metric' else '°F'
        }
        
        return jsonify(weather_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)