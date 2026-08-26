from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "universidad.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=False, connect_args=connect_args)

def create_db_and_tables():
    """Crea las tablas en la base de datos si no existen."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Generador de sesiones para inyectar en las dependencias de FastAPI."""
    with Session(engine) as session:
        yield session
