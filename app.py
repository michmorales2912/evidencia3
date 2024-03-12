from flask import Flask, render_template, request, redirect, session
import os
from menu import Menu
from pedidos import SistemaPedidos
from caja import Caja, Meseros, Cocina
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)
menu_restaurante = Menu()
sistema_pedidos = SistemaPedidos()
caja = Caja(sistema_pedidos)
meseros = Meseros(sistema_pedidos)
cocina = Cocina(sistema_pedidos)

#Obtener menu 
def obtener_menu():
    menu_restaurante = Menu()
    menu_data = {
        'Pizzas': menu_restaurante.pizzas,
        'Boneless': menu_restaurante.boneless,
        'Spaggetti': menu_restaurante.spaggetti,
        'Papas fritas': menu_restaurante.papas_fritas,
        'Ensaladas': menu_restaurante.ensaladas,
        'Bebidas': menu_restaurante.bebidas,
    }
    return menu_data


#Index
@app.route('/')
def index():
    return render_template('index.html')

#Menu
@app.route('/menu')
def mostrar_menu():
    menu = {
        "Pizzas": menu_restaurante.pizzas,
        "Boneless": menu_restaurante.boneless,
        "Spaggetti": menu_restaurante.spaggetti,
        "Papas fritas": menu_restaurante.papas_fritas,
        "Ensaladas": menu_restaurante.ensaladas,
        "Bebidas": menu_restaurante.bebidas
    }

    return render_template('menu.html', menu=menu)


@app.route('/realizar_pedido', methods=['GET', 'POST'])
def realizar_pedido():
    if request.method == 'POST':
        selected_item = request.form['order-item']
        quantity = int(request.form['quantity'])

        current_order = session.get('current_order', [])
        current_order.append({'item': selected_item, 'quantity': quantity})
        session['current_order'] = current_order

    return render_template('realizar_pedido.html', menu=menu_restaurante)
#Pedidos
@app.route('/sistema_pedidos')
def sistema_pedidos():
    current_order = session.get('current_order', [])
    return render_template('sistema_pedidos.html', current_order=current_order)
#Caja 
@app.route('/caja')
def caja():
    return render_template('caja.html', caja=caja)

if __name__ == '__main__':
    app.run(debug=True)
