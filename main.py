from paquete.clientes import Cliente

cliente1 = Cliente("Leandro", "lean@gmail.com", "Figueroa Alcorta y Udaondo", "0123456789")
print(cliente1)

#metodos
cliente1.realizar_compra("Camiseta River")  # El cliente realiza una compra

cliente1.actualizar_informacion("Avenida 456", "9876543210")  # El cliente actualiza su información