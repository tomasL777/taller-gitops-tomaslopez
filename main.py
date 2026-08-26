from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from contextlib import asynccontextmanager

from database import create_db_and_tables, get_session
from models import Estudiante, Nota

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan, title="Sistema Estudiantes MVC")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def listar_estudiantes(request: Request, session: Session = Depends(get_session)):
    estudiantes = session.exec(select(Estudiante)).all()
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"estudiantes": estudiantes}
    )

@app.post("/estudiantes/")
def crear_estudiante(
    codigo: str = Form(...),
    nombre: str = Form(...),
    semestre: int = Form(...),
    session: Session = Depends(get_session)
):
    nuevo_estudiante = Estudiante(codigo=codigo, nombre=nombre, semestre=semestre)
    session.add(nuevo_estudiante)
    session.commit()
    return RedirectResponse(url="/", status_code=303)
