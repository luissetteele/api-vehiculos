import os
from sqlmodel import create_engine, SQLModel, Session
from models.vehiculos import Vehiculo

# Configuración de variables de entorno
db_user = os.getenv("DB_USER", "quevedo")
db_password = os.getenv("DB_PASSWORD", "1234")
db_server = os.getenv("DB_HOST", "localhost")
db_port = int(os.getenv("DB_PORT", 5432))
db_name = os.getenv("DB_NAME", "vehiculosdb")

# Detectar tipo de base de datos según el puerto
if db_port == 5432:
    DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"
    print("✓ MODO: PostgreSQL detectado.")
else:
    DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"
    print("✓ MODO: MySQL detectado.")

print(f"✓ Conectando a: {db_server}:{db_port}...")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        count = session.query(Vehiculo).count()
        if count == 0:
            vehiculos_data = [
                Vehiculo(marca="Tesla", matricula="ABC123", electrico=True, fecha_matriculacion="2023-01-15", kilometros=5000),
                Vehiculo(marca="BMW", matricula="DEF456", electrico=False, fecha_matriculacion="2022-06-20", kilometros=15000),
                Vehiculo(marca="Nissan", matricula="GHI789", electrico=True, fecha_matriculacion="2023-03-10", kilometros=8000),
                Vehiculo(marca="Audi", matricula="JKL012", electrico=False, fecha_matriculacion="2021-11-05", kilometros=45000),
                Vehiculo(marca="Volkswagen", matricula="MNO345", electrico=True, fecha_matriculacion="2023-02-28", kilometros=3000),
            ]
            for vehiculo in vehiculos_data:
                session.add(vehiculo)
            session.commit()

init_db()

def get_vehiculos():
    with Session(engine) as session:
        return session.query(Vehiculo).all()

def get_vehiculo_by_id(vehiculo_id: int):
    with Session(engine) as session:
        return session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
