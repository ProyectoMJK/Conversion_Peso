from pydantic import BaseModel, condecimal
from datetime import datetime
from typing import Optional

class ConversionPesoSchema(BaseModel):
    id: Optional[int] = None
    resultado: Optional[condecimal(decimal_places=2)] = None
    tipo: Optional[str] = None
    registro: Optional[datetime] = None

    class Config:
        from_attributes = True  # Modificado para Pydantic V2

