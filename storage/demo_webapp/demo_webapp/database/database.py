import os
from sqlalchemy import create_engine, MetaData, Table

# Configuración de la conexión a la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://users_login:mjk12345@172.30.1.21/proyecto_login")
                                               
# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)  

# Metadata y tablas
metadata = MetaData()

ct = Table('usuarios_login', metadata, autoload_with=engine)