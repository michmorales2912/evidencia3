class SistemaPedidos:
    def __init__(self):
        self.ordenes = [] 
        self.cola_pedidos = [] 

    def verificar_estructura_vacia(self):
        return not self.ordenes

    def agregar_orden(self, num_mesa, elementos):
        if len(self.ordenes) < 6:
            nueva_orden = {"num_mesa": num_mesa, "elementos": elementos}
            self.ordenes.append(nueva_orden)
            self.cola_pedidos.append(nueva_orden)
            print("La orden fue registrada con éxito.")
        else:
            print("El sistema no acepta más de 6 órdenes al mismo tiempo.")

    def consultar_orden(self):
        if self.ordenes:
            return self.ordenes[-1]
        else:
            return None

    def eliminar_orden_producida(self):
        if self.ordenes:
            orden_eliminada = self.ordenes.pop()
            print(f"Orden eliminada: {orden_eliminada}")
        else:
            print("No hay órdenes para eliminar.")

    def sumar_ordenes(self):
        if self.ordenes:
            total = sum(len(orden["elementos"]) for orden in self.ordenes)
            return total
        else:
            return 0

    def quitar_elemento(self, num_mesa, elemento):
        for orden in self.ordenes:
            if orden["num_mesa"] == num_mesa:
                if elemento in orden["elementos"]:
                    orden["elementos"].remove(elemento)
                    print(f"Elemento {elemento} eliminado de la orden {num_mesa}.")
                    return
                else:
                    print(f"El elemento {elemento} no está en la orden {num_mesa}.")
                    return
        print(f"No se encontró la orden {num_mesa}.")

# Objeto 
sistema = SistemaPedidos()

