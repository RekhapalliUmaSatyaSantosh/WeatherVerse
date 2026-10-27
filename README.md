# 🌦️ WeatherVerse — Django Weather Forecast App

WeatherVerse is a weather forecasting web application built with **Python and Django** that uses a weather API to retrieve weather information based on a user's search. It combines backend development with a clean, modern interface to make checking the weather simple and convenient.

## ✨ Features

- 🌍 **City-Based Search** — Search for weather information by city name.
- 🌤️ **Weather API Integration** — Retrieve weather data from the OpenWeather API.
- 📊 **Weather Information** — Display available weather details through an organized interface.
- 🎨 **Modern UI** — Responsive layout with a weather-themed design.
- ⚙️ **Django Backend** — Handle application logic and API requests using Django.
- 🔍 **Search-Based Results** — Fetch weather information for the requested location.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Page structure |
| CSS3 | Styling and layout |
| OpenWeather API | Weather data |
| SQLite | Development database |

## 📁 Project Structure

```text
WeatherVerse/
├── Weather_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── api/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/RekhapalliUmaSatyaSantosh/WeatherVerse.git
```

### 2. Navigate to the Project Directory

```bash
cd WeatherVerse
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Django

```bash
pip install django requests
```

If your project has a `requirements.txt` file, you can install its dependencies using:

```bash
pip install -r requirements.txt
```

### 5. Configure the Weather API

1. Create an account on [OpenWeather](https://openweathermap.org/).
2. Generate an API key.
3. Configure the API key in your Django settings or the configuration method used by your project.

Example:

```python
API_KEY = "your_openweather_api_key"
```

**Security tip:** Never commit your real API key or other secrets to GitHub. Use environment variables to keep them private.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## 💡 What I Learned

- Building web applications using Django.
- Integrating external APIs into a Python application.
- Handling user input and processing API responses.
- Connecting backend functionality with HTML and CSS.
- Organizing a Django project and managing application configuration.
- Debugging and testing web application functionality.

## 🔮 Future Improvements

- Add a five-day weather forecast.
- Display weather icons and additional atmospheric details.
- Improve mobile responsiveness.
- Add location-based weather detection.
- Implement better error handling for invalid city names and API failures.

## 👨‍💻 Developer

**Rekhapalli Uma Satya Santosh**

Python Full-Stack Developer | Django | REST APIs | SQL

- **GitHub:** [RekhapalliUmaSatyaSantosh](https://github.com/RekhapalliUmaSatyaSantosh)
- **Project:** [WeatherVerse Repository](https://github.com/RekhapalliUmaSatyaSantosh/WeatherVerse)

---

⭐ If you find this project interesting, consider giving the repository a star!
