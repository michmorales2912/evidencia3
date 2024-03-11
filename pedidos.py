class SistemaPedidos:
    def __init__(self):
        self.ordenes = []

    def verificar_estructura_vacia(self):
        return len(self.ordenes) == 0

    def agregar_orden(self, orden):
        if len(self.ordenes) < 6:
            self.ordenes.append(orden)
            print("La orden fue registrada con éxito.")
        else:
            print("El sistema no acepta más de 6 órdenes al mismo tiempo.")

    def consultar_orden(self):
        return self.ordenes

    def eliminar_orden(self, numero_orden):
        if numero_orden < len(self.ordenes):
            del self.ordenes[numero_orden]
            print(f"Orden {numero_orden} eliminada correctamente.")
        else:
            print("Número de orden no válido.")

    def sumar_orden(self):
        total = 0
        for orden in self.ordenes:
            # Supongamos que cada orden tiene un precio asociado
            total += orden.precio
        return total

    def quitar_elemento(self, numero_orden, elemento):
        if numero_orden < len(self.ordenes):
            if elemento in self.ordenes[numero_orden].elementos:
                self.ordenes[numero_orden].elementos.remove(elemento)
                print(f"Elemento {elemento} eliminado de la orden {numero_orden}.")
            else:
                print(f"Elemento {elemento} no encontrado en la orden {numero_orden}.")
        else:
            print("Número de orden no válido.")


#Caja
class MenuCaja:
    def __init__(self):
        self.accion_1 = "Sumar"
        self.accion_2 = "Quitar_elemento"
        self.accion_3 = "Eliminar_orden"

menu_caja = MenuCaja()

class MenuMeseros:
    def __init__(self):
        self.accion_1 = "Añadir"
        self.accion_2 = "Consultar"
        self.accion_3 = "Consultar"

menu_meseros = MenuMeseros()

class MenuCocina:
    def __init__(self):
        self.accion_1 = "Consultar"
        self.accion_2 = "Consultar"
        self.accion_3 = "Eliminar_orden"

menu_cocina = MenuCocina()

# Ejemplo de cómo acceder a las acciones en cada área:
print("Caja:")
print(f"#10 {menu_caja.accion_1}")
print(f"#40 {menu_caja.accion_2}")
print(f"#30 {menu_caja.accion_3}")

print("\nMeseros:")
print(f"#10 {menu_meseros.accion_1}")
print(f"#20 {menu_meseros.accion_2}")
print(f"#20 {menu_meseros.accion_3}")

print("\nCocina:")
print(f"#20 {menu_cocina.accion_1}")
print(f"#30 {menu_cocina.accion_2}")
print(f"#30 {menu_cocina.accion_3}")


#Menu
class Menu:
    def __init__(self):
        self.pizzas = [
            {"id": 1, "nombre": "Pizza especial", "precio": 289},
            {"id": 2, "nombre": "Pizza campesina", "precio": 289},
            {"id": 3, "nombre": "Pizza Pancho Villa", "precio": 289},
            {"id": 4, "nombre": "Pizza norteña", "precio": 320},
            {"id": 5, "nombre": "Pizza chicken-bufalo", "precio": 289}
        ]

        self.boneless = [
            {"id": 11, "nombre": "Naturales", "precio": 175},
            {"id": 12, "nombre": "Búfalo", "precio": 175},
            {"id": 13, "nombre": "Mango-habanero", "precio": 175},
            {"id": 14, "nombre": "BBQ", "precio": 175}
        ]

        self.spaggetti = [
            {"id": 6, "nombre": "De la casa", "precio": 175},
            {"id": 7, "nombre": "Con crema", "precio": 175},
            {"id": 8, "nombre": "Chorizo", "precio": 175},
            {"id": 9, "nombre": "Boloñés", "precio": 175}
        ]

        self.papas_fritas = [
            {"id": 15, "nombre": "Chicas", "precio": 110},
            {"id": 16, "nombre": "Grandes", "precio": 165}
        ]

        self.ensaladas = [
            {"id": 17, "nombre": "Chicas", "precio": 110},
            {"id": 18, "nombre": "Grandes", "precio": 165}
        ]

        self.bebidas = [
            {"id": 19, "nombre": "Agua natural", "precio": 28},
            {"id": 21, "nombre": "Coca cola", "precio": 28},
            {"id": 22, "nombre": "Fanta", "precio": 28},
            {"id": 23, "nombre": "Uva", "precio": 28},
            {"id": 24, "nombre": "Fresa", "precio": 28},
            {"id": 25, "nombre": "Naranja", "precio": 28},
            {"id": 26, "nombre": "Manzanita", "precio": 28}
        ]

    def mostrar_menu(self):
        print("----------- Menú -----------")
        self.mostrar_categoria("Pizzas", self.pizzas)
        self.mostrar_categoria("Boneless", self.boneless)
        self.mostrar_categoria("Spaggetti", self.spaggetti)
        self.mostrar_categoria("Papas fritas", self.papas_fritas)
        self.mostrar_categoria("Ensaladas", self.ensaladas)
        self.mostrar_categoria("Bebidas", self.bebidas)

    def mostrar_categoria(self, nombre_categoria, lista_items):
        print(f"\n{nombre_categoria}")
        for item in lista_items:
            print(f"{item['id']} {item['nombre']} ${item['precio']}")

# Ejemplo de uso
menu_restaurante = Menu()
menu_restaurante.mostrar_menu()
