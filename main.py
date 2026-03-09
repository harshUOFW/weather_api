from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Home page (frontend)
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint
@app.get("/weather/{city}")
def get_weather(city: str):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    result = {
        "city": city,
        "temperature": data["current_condition"][0]["temp_C"],
        "weather": data["current_condition"][0]["weatherDesc"][0]["value"],
        "humidity": data["current_condition"][0]["humidity"]
    }

    return result