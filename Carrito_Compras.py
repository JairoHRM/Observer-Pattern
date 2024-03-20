# Evento de compra 
class CompraEvent:
    def __init__(self, productos):
        self.productos = productos

# Interfaz Observador
class Observador:
    def actualizar(self, evento):
        pass

# Servicio CarritoDeCompras
class CarritoDeCompras(Observador):
    def __init__(self):
        self.productos_en_carrito = []

    def actualizar(self, evento):
        print("Limpiando el carrito de compras...")
        self.productos_en_carrito.clear()

# Servicio Inventario
class Inventario(Observador):
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto, cantidad):
        self.inventario[producto] = cantidad

    def actualizar(self, evento):
        print("Actualizando inventario...")
        for producto in evento.productos:
            if producto in self.inventario:
                del self.inventario[producto] # Simplemente se está asumiendo que se descuentan del inventario

# Servicio Usuario
class Usuario(Observador):
    def actualizar(self, evento):
        print("Notificando al usuario de los productos comprados...")
        # Aquí puedes implementar la lógica para notificar al usuario sobre los productos comprados

# Servicio Payment
class Payment:
    def __init__(self):
        self.observadores = []

    def registrar_observador(self, observador):
        self.observadores.append(observador)

    def realizar_compra(self, productos_comprados):
        print("Compra realizada con éxito")
        evento = CompraEvent(productos_comprados)
        self.notificar_observadores(evento)

    def notificar_observadores(self, evento):
        for observador in self.observadores:
            observador.actualizar(evento)

# Ejemplo de uso
if __name__ == "__main__":
    # Creación de los servicios
    payment = Payment()
    carrito = CarritoDeCompras()
    inventario = Inventario()
    usuario = Usuario()

    # Registro de observadores
    payment.registrar_observador(carrito)
    payment.registrar_observador(inventario)
    payment.registrar_observador(usuario)

    # Simulación de una compra
    productos_comprados = ["Producto A", "Producto B", "Producto C"]
    payment.realizar_compra(productos_comprados)
