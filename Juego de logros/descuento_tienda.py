Categoria = input("ingresa la categoria:")
cantidad = int("ingresa la cantidad:")
precio =  float("ingresa el precio C/U:")

  

total = cantidad * precio
if Categoria == "electronica" and cantidad > 7:
    descuento = total * 0.20
elif Categoria == "Ropa" and cantidad > 8:
    descuento = total * 0.25
else:
    descuento = 0
total_con_descuento = total - descuento
print("descuento aplicado: ", descuento)
print("total a pagar: ", total_con_descuento)
