from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from database.database import engine, ct
from schemas.schemas import ConversionPesoSchema
from typing import List

## Router para diferentes temperaturas
peso_router = APIRouter()

@peso_router.get("/api/conversiones/peso", response_model=List[ConversionPesoSchema])
def get_conversion_peso():
    try:
        with engine.connect() as connection:
            query = select(ct)
            result: Result = connection.execute(query)
            resultados = [ConversionPesoSchema(**dict(zip(result.keys(), row))) for row in result]
            return resultados
    except Exception as e:
        print(f"Error inesperado: {e}")  # Imprimir el error en la consola
        raise HTTPException(status_code=500, detail="Error al consultar la base de datos.")
    
@peso_router.post("/api/conversiones/peso", response_model=ConversionPesoSchema)
def create_conversion_peso(conversion: ConversionPesoSchema):
    try:
        with engine.connect() as connection:
            # Crear la sentencia de inserción
            stmt = insert(ct).values(
                resultado=conversion.resultado,
                tipo=conversion.tipo,
            )
            result: Result = connection.execute(stmt)
            connection.commit()
            conversion.id = result.inserted_primary_key[0]  # Esto asume que el ID es autoincremental
            return conversion
    except Exception as e:
        print(f"Error inesperado: {e}")  # Imprimir el error en la consola
        raise HTTPException(status_code=500, detail="Error al insertar datos en la base de datos.")
