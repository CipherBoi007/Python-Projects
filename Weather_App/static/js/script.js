document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('cityInput');
    const searchBtn = document.getElementById('searchBtn');
    const celsiusBtn = document.getElementById('celsiusBtn');
    const fahrenheitBtn = document.getElementById('fahrenheitBtn');
    const weatherInfo = document.getElementById('weatherInfo');
    const errorDiv = document.getElementById('error');
    
    let currentUnits = 'metric';

    searchBtn.addEventListener('click', fetchWeather);
    cityInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') fetchWeather();
    });
    
    celsiusBtn.addEventListener('click', function() {
        if (currentUnits !== 'metric') {
            switchUnits('metric');
            if (cityInput.value.trim()) fetchWeather();
        }
    });
    
    fahrenheitBtn.addEventListener('click', function() {
        if (currentUnits !== 'imperial') {
            switchUnits('imperial');
            if (cityInput.value.trim()) fetchWeather();
        }
    });
    
    function switchUnits(unit) {
        currentUnits = unit;
        celsiusBtn.classList.toggle('active', unit === 'metric');
        fahrenheitBtn.classList.toggle('active', unit === 'imperial');
    }
    
    function fetchWeather() {
        const city = cityInput.value.trim();
        
        if (!city) {
            showError('Please enter a city name');
            return;
        }
        
        errorDiv.textContent = '';
        
        fetch(`/weather?city=${encodeURIComponent(city)}&units=${currentUnits}`)
            .then(handleResponse)
            .then(displayWeather)
            .catch(handleError);
    }
    
    function handleResponse(response) {
        if (!response.ok) {
            return response.json().then(err => {
                throw new Error(err.error || 'Failed to fetch weather data');
            });
        }
        return response.json();
    }
    
    function displayWeather(data) {
        document.getElementById('location').textContent = `${data.city}, ${data.country}`;
        document.getElementById('temperature').textContent = Math.round(data.temperature);
        document.getElementById('unit').textContent = data.unit;
        document.getElementById('feelsLike').textContent = Math.round(data.feels_like);
        document.getElementById('feelsLikeUnit').textContent = data.unit;
        document.getElementById('weatherDescription').textContent = 
            data.description.charAt(0).toUpperCase() + data.description.slice(1);
        document.getElementById('humidity').textContent = data.humidity;
        document.getElementById('windSpeed').textContent = data.wind_speed;
        
        const iconUrl = `https://openweathermap.org/img/wn/${data.icon}@2x.png`;
        const weatherIcon = document.getElementById('weatherIcon');
        weatherIcon.src = iconUrl;
        weatherIcon.alt = data.description;
        
        weatherInfo.style.display = 'block';
    }
    
    function handleError(error) {
        console.error('Error:', error);
        showError(error.message);
        weatherInfo.style.display = 'none';
    }
    
    function showError(message) {
        errorDiv.textContent = message;
    }
});