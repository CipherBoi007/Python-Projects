from flask import Flask, request, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Use your actual API key here
API_KEY = os.getenv("OPENWEATHER_API_KEY")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')

    if not city:
        return jsonify({'error': 'City is required'}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': data.get('message', 'Invalid request')}), response.status_code

    result = {
        'city': data['name'],
        'country': data['sys']['country'],
        'temp': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind': data['wind']['speed'],
        'icon': data['weather'][0]['icon']
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
