from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Estudiante(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True)
    nombre: str
    semestre: int
    
    notas: List["Nota"] = Relationship(back_populates="estudiante")

class Nota(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    materia: str
    calificacion: float
    
    estudiante_id: int = Field(foreign_key="estudiante.id")
    estudiante: Estudiante = Relationship(back_populates="notas")
