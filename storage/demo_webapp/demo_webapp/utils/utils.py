import requests
from utils.formulas import kilos_a_libras, libras_a_kilos

API_URL = "http://172.30.0.20:80/api/conversiones/peso"

def obtener_conversiones():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener conversiones: {e}")
        return []

def crear_conversion(peso, tipo):
    peso = float(peso)
    if tipo == "L":
        resultado = kilos_a_libras(peso)
        tipo_completo = "Kilos a libras"
    elif tipo == "K":
        resultado = libras_a_kilos(peso)
        tipo_completo = "Libras a kilos"
    else:
        print("Tipo de conversión no válido")
        return False

    nueva_conversion = {
        ##"resultado": resultado,
        "resultado": round(resultado, 2),
        "tipo": tipo_completo
    }

    try:
        response = requests.post(API_URL, json=nueva_conversion)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error al crear la conversión: {e}")
        return False
