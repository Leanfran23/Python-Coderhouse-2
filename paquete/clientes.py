
class Cliente:
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return self.nombre

    def realizar_compra(self, producto):
        # Se hace la compra
        print(f"{self.nombre} ha comprado {producto}")

    def actualizar_informacion(self, nueva_direccion, nuevo_telefono):
        self.direccion = nueva_direccion
        self.telefono = nuevo_telefono
        print(f"La información de {self.nombre} ha sido actualizada")
