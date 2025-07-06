from fastapi import FastAPI
from routes.routes import peso_router

app = FastAPI()

# Incluir el router de peso_router con la etiqueta 'Conversiones de Peso'
app.include_router(peso_router, tags=["Conversiones de Peso"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)  
