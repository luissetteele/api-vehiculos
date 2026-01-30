from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from data.db import get_vehiculos, get_vehiculo_by_id

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/vehiculos", response_class=HTMLResponse)
async def lista_vehiculos(request: Request):
    vehiculos = get_vehiculos()
    return templates.TemplateResponse("coches.html", {"request": request, "vehiculos": vehiculos})

@app.get("/vehiculos/{vehiculo_id}", response_class=HTMLResponse)
async def detalle_vehiculo(vehiculo_id: int, request: Request):
    vehiculo = get_vehiculo_by_id(vehiculo_id)
    if vehiculo:
        return templates.TemplateResponse("vehiculos.html", {"request": request, "vehiculo": vehiculo})