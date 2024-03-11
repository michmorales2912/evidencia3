from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página del Menú
@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/realizar_pedido', methods=['GET', 'POST'])
def realizar_pedido():
    if request.method == 'POST':
        # Obtener datos del formulario
        selected_item = request.form['order-item']
        quantity = int(request.form['quantity'])

        # Almacenar en la sesión
        current_order = session.get('current_order', [])
        current_order.append({'item': selected_item, 'quantity': quantity})
        session['current_order'] = current_order

    # Cargar la página de realizar pedido
    return render_template('realizar_pedido.html')

# Ruta para la página de sistema de pedidos
@app.route('/sistema_pedidos')
def sistema_pedidos():
    # Recuperar el pedido de la sesión
    current_order = session.get('current_order', [])
    return render_template('sistema_pedidos.html', current_order=current_order)

if __name__ == '__main__':
    app.run(debug=True)
