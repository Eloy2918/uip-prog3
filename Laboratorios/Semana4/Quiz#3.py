print(" Ingrese su nombre y ventas ")
nombre=input(" Nombre: ")

venta1=float(input("Venta 1: "))
venta2=float(input("Venta 2: "))
venta3=float(input("Venta 3: "))

totalventas=(venta1+venta2+venta3)

comision=((totalventas)*12.5)/100

totalcomision=totalventas+comision


print("               Vendedor :  " + str(nombre))


print("El total de la venta es de : " + str(totalventas))



print("La comision es de : " + str(comision))


print("Y el Total es de : " + str(totalcomision))



input()
