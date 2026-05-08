vehiculo = input("tipo de vehiculo: ")
hora_pico = input("¿Es hora pico? (si/no): ")
if vehiculo == "Carro":
    print("El peaje es de 5$")
elif vehiculo == "Moto":
    print("El peaje es de 1.2$")
elif vehiculo == "Camion":
    print("El peaje es de 10$")
else:
    print("Vehiculo no reconocido")
    if precio is not None:
        if hora_pico == "si":
            precio *= 0.4
            print("Es hora pico, se aplica un descuento del 20%")
        print("El peaje es de ", precio, "$")
      




