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







