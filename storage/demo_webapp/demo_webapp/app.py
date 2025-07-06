from flask import Flask, render_template, request, redirect, url_for, flash, session 
from utils.utils import obtener_conversiones, crear_conversion
from util.util import verificar_usuario

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesaria para usar flash messages


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/peso/', methods=['GET'], strict_slashes=False)
def get_peso():
    conversiones = obtener_conversiones()
    return render_template('get_peso.html', conversiones=conversiones)

@app.route('/peso/crear/', methods=['GET', 'POST'], strict_slashes=False)
def create_peso():
    if request.method == 'POST':
        peso = request.form['peso']  # Obtener peso del formulario
        tipo = request.form['tipo']  # Obtener tipo de conversión del formulario
        exito = crear_conversion(peso, tipo)  # Llamar a crear_conversion
        if exito:
            flash('Conversión creada exitosamente', 'success')
            return redirect(url_for('get_peso'))
        else:
            flash('Error al crear la conversión', 'danger')
    return render_template('create_peso.html')

@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']
        if verificar_usuario(username, password):
            # ACCESO: Crear sesión
            session['username'] = username
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Has cerrado sesión correctamente')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
