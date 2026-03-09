# Weather API Analyzer 🌦️

A lightweight full-stack application that retrieves real-time weather information for any city.
The application demonstrates how a frontend interacts with a backend API that consumes data from an external weather service.

This project was built to practice **REST APIs, backend development, and basic frontend integration** using Python and FastAPI.

---

## 🚀 Features

* Retrieve real-time weather information by city
* Backend API built using **FastAPI**
* Frontend interface built using **HTML and JavaScript**
* Integration with an external weather API
* JSON data processing and transformation

---

## 🧠 Concepts Demonstrated

This project demonstrates several important software engineering concepts:

* REST API design
* HTTP requests and responses
* API consumption (calling third-party APIs)
* JSON data parsing
* Backend-frontend communication
* Basic full-stack architecture

---

## 🛠 Technologies Used

* **Python**
* **FastAPI**
* **Requests**
* **HTML**
* **JavaScript (Fetch API)**
* **Jinja2 Templates**

---

## 📂 Project Structure

```
weather-api-analyzer
│
├── main.py
├── requirements.txt
├── README.md
└── templates
    └── index.html
```

---

## ⚙️ How the Application Works

1. The user enters a city name in the web interface.
2. JavaScript sends a request to the backend endpoint:

```
/weather/{city}
```

3. The FastAPI backend calls an external weather API.
4. The server extracts useful data such as:

* temperature
* humidity
* weather conditions

5. The processed data is returned as JSON.
6. The frontend displays the result to the user.

---

## ▶️ Running the Project

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Start the API server

```
uvicorn main:app --reload
```

### 3️⃣ Open the application

```
http://127.0.0.1:8000
```

---

## 📌 Example API Endpoint

```
GET /weather/winnipeg
```

Example response:

```json
{
  "city": "winnipeg",
  "temperature": "18",
  "weather": "Partly cloudy",
  "humidity": "62"
}
```

---

## 👨‍💻 Author

Harsh Panchal
BSc Computer Science
University of Winnipeg

---
