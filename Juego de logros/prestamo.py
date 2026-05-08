ingresos = float(input("Cual son tus ingresos:"))
edad = int(input("Cual es tu edad:"))

if ingresos > 40000 and edad > 21:
    print("Resultado: Aprobado el prestamo")
elif ingresos >= 20000 and ingresos <= 40000:
    print("Resultado: aprovado con aval")
else:
    print("Resultado: Prestamo no aprbado")
