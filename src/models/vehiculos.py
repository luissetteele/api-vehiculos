from sqlmodel import SQLModel, Field
from typing import Optional

class Vehiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    marca: str
    matricula: str
    electrico: bool
    fecha_matriculacion: str
    kilometros: int


