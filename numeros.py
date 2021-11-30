"""para la creacion de variables solo es necesario poner el nombre y asignale el tipo de valor que este almacenara"""

numero = 19 #este es una varibale de tipo entero
numero2 = 3.1416 #este es una variable de tipo float

"""para el tipo de variable es necesario ponerle un int(nombre_variable), por un ejemplo si yo quiero convertir el valor que tiene
la variable numero que es un tipo int a float solo pondremos float(numero) y este nos cambiara a float y sera numero = 19.0, ahora si yo quiero
cambiar el numero2 que es tipo float a int entonces pondremos int(numero2) y entonces sera numero2 = 3, si nosotros queremos cambiar el numero que es int a int
no es necesari ya que es int entonces no tiene caso realizar el cambio"""

#imprimmos con los datos que tiene por default
print("Valor que tiene numero ",numero, " tipo de varibale ", type(numero))
print("Valor que tiene numero2 ",numero2, " tipo de varibale ", type(numero2))
print()
#ahora vamos a cambiar los valores

print("Valor que tiene numero ",float(numero), " tipo de varibale ", type(numero))
print("Valor que tiene numero2 ",int(numero2), " tipo de varibale ", type(numero2))
print()