import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session, select
from sqlmodel.pool import StaticPool

from main import app
from database import get_session, create_db_and_tables
from models import Estudiante
from logica import calcular_estadisticas_notas

# --- FIXTURES DE BASE DE DATOS EN MEMORIA ---

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

# --- PRUEBAS DE LA APLICACIÓN WEB MVC ---

def test_listar_estudiantes_vacio(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert "Directorio de Estudiantes" in response.text
    assert "No hay estudiantes registrados." in response.text

def test_crear_estudiante(client: TestClient, session: Session):
    response = client.post(
        "/estudiantes/",
        data={"codigo": "E001", "nombre": "Juan Pérez", "semestre": 3},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert "Juan Pérez" in response.text
    assert "E001" in response.text

    estudiante = session.exec(select(Estudiante).where(Estudiante.codigo == "E001")).first()
    assert estudiante is not None
    assert estudiante.nombre == "Juan Pérez"
    assert estudiante.semestre == 3

def test_database_helpers():
    create_db_and_tables()
    gen = get_session()
    s = next(gen)
    assert isinstance(s, Session)

# --- PRUEBAS DEL RETO DE LÓGICA BÁSICA (logica.py) ---

def test_calcular_estadisticas_lista_vacia():
    resultado = calcular_estadisticas_notas([])
    assert resultado == {
        "total": 0,
        "promedio": 0.0,
        "aprobados": 0,
        "reprobados": 0,
        "nota_maxima": 0.0,
        "nota_minima": 0.0
    }

def test_calcular_estadisticas_notas_variadas():
    notas = [3.5, 4.0, 2.0, 5.0, 1.5]
    resultado = calcular_estadisticas_notas(notas)
    
    assert resultado["total"] == 5
    assert resultado["promedio"] == 3.2
    assert resultado["aprobados"] == 3
    assert resultado["reprobados"] == 2
    assert resultado["nota_maxima"] == 5.0
    assert resultado["nota_minima"] == 1.5

def test_calcular_estadisticas_todos_aprobados():
    notas = [4.5, 3.8, 5.0]
    resultado = calcular_estadisticas_notas(notas)
    
    assert resultado["total"] == 3
    assert resultado["promedio"] == 4.43
    assert resultado["aprobados"] == 3
    assert resultado["reprobados"] == 0
    assert resultado["nota_maxima"] == 5.0
    assert resultado["nota_minima"] == 3.8

def test_calcular_estadisticas_todos_reprobados():
    notas = [1.0, 2.5, 2.8]
    resultado = calcular_estadisticas_notas(notas)
    
    assert resultado["total"] == 3
    assert resultado["promedio"] == 2.1
    assert resultado["aprobados"] == 0
    assert resultado["reprobados"] == 3
    assert resultado["nota_maxima"] == 2.8
    assert resultado["nota_minima"] == 1.0
