from pedidos import SistemaPedidos
class Caja:
    def __init__(self, sistema_pedidos=None):
         self.sistema_pedidos = sistema_pedidos or SistemaPedidos()
    def sumar_ordenes(self):
        total = self.sistema_pedidos.sumar_ordenes()
        print(f"Total a pagar: ${total}")

    def quitar_elemento(self, num_mesa, elemento):
        self.sistema_pedidos.quitar_elemento(num_mesa, elemento)


class Meseros:
    def __init__(self, sistema_pedidos=None):
         self.sistema_pedidos = sistema_pedidos or SistemaPedidos()

    def agregar_orden(self, num_mesa, elementos):
        self.sistema_pedidos.agregar_orden(num_mesa, elementos)

    def consultar_orden(self):
        orden = self.sistema_pedidos.consultar_orden()
        if orden:
            print(f"Consulta de orden: {orden}")
        else:
            print("No hay órdenes registradas.")


class Cocina:
    def __init__(self, sistema_pedidos=None):
        self.sistema_pedidos = sistema_pedidos or SistemaPedidos()

    def consultar_orden(self):
        orden = self.sistema_pedidos.consultar_orden()
        if orden:
            print(f"Consulta de orden para Cocina: {orden}")
        else:
            print("No hay órdenes registradas en Cocina.")

    def eliminar_orden_producida(self):
        self.sistema_pedidos.eliminar_orden_producida()




