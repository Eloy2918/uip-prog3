
# Quiz#5
# Eloy Sánchez
# Instrucciones: Promedio de notas

print ("Escriba el nombre del alumno")
input ("nombre")


print ("Escriba las notas del alumno")

nota1 = float(input('Nota1 '))
nota2 = float(input('Nota2 '))
nota3 = float(input('Nota3 '))
nota4 = float(input('Nota4 '))
nota5 = float(input('Nota5 '))

promedio = float (nota1+nota2+nota3+nota4+nota5)/5

print ("El promedio es de : " + str (promedio))

if promedio >= 71:  

      print ("El estudiante aprobo la materia")

else:

      print (" El estudiante reprobo la materia ")

archivo = open('Juan.txt', 'w')

archivo.write("Estudiante 1 : \n\n ")

archivo.write("Nota 1 : \n ")

archivo.write("Nota 2 : \n ")

archivo.write("Nota 3 : \n ")

archivo.write("Nota 4 : \n ")

archivo.write("Nota 5 : \n ")

archivo.close()