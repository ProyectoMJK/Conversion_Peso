import os
from sqlalchemy import create_engine, MetaData, Table

# Configuración de la conexión a la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://conversiones_proy:12345proy@172.30.1.20/conversiones_peso")
                                                 
# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)  

# Metadata y tablas
metadata = MetaData()

ct = Table('conversion_peso', metadata, autoload_with=engine)