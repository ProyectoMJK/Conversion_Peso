from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
import psycopg2
from psycopg2.extras import RealDictCursor
import os

DB_LOGIN_CONFIG = {
    'host': os.getenv('DB_LOGIN_HOST', 'demo_login_db'),
    'database': os.getenv('DB_LOGIN_NAME', 'proyecto_login'),
    'user': os.getenv('DB_LOGIN_USER', 'users_login'),
    'password': os.getenv('DB_LOGIN_PASSWORD', 'mjk12345'),
    'port': os.getenv('DB_LOGIN_PORT', '5432')
}

def get_db_connection():
    """Obtener conexión a la base de datos de login"""
    try:
        conn = psycopg2.connect(**DB_LOGIN_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Error conectando a la base de datos de login: {e}")
        return None

def verificar_usuario(username, password):
    """
    validacion - verifica los datos ingresados del usuario en la base de datos
    """
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT * FROM usuarios_login WHERE username = %s AND password = %s",
                (username, password)
            )
            user = cursor.fetchone()
            return user is not None
    except psycopg2.Error as e:
        print(f"Error verificando usuario: {e}")
        return False
    finally:
        conn.close()