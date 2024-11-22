"""Cree una funcion que calcule el promedio de N notas"""

def promedio (N):
    suma = 0
    
    for i in range (1, N+1): #tuve que poner N + 1 porque al momento de probar solo llegaba hasta el 4.
        nota = float(input(f"Ingrese la nota numero {i}: \n"))
        suma += nota
    
    promedio = suma / N
    print (f"El promedio de todas las notas es de: {promedio}\n")

N = int (input("Ingrese la cantidad de notas: "))
promedio (N)

"""Cree una funcion que determine si un color es primario o no, se debe imprimir por
pantalla la leyenda “el color X es primero “ o “el color X no es primario”""" 

def def_color (color):
    if color == "rojo" or color == "amarillo" or color == "azul":
        print(f"El color {color} es primario")
    else:
        print(f"El color {color} no es primario")
    
    
color = input ("Ingrese algun color: \n").strip().lower() #elimino espacios y paso a minuscula el color
def_color (color)



"""Cree una funcion que determine que numero de una serie de N numeros es mayor"""

def mayor (N):
    ban = 0
    maximo = 0
    
    for i in range (N):
        num = int (input ("Ingrese un numero: \n"))
        if ban == 0 or num > maximo:
            maximo = num
            ban+=1
    
    return maximo
    
N = int(input("Ingrese un numero: \n"))
max_num = mayor (N)
print (f"El maximo numero de la cadena es:{max_num}")



"""Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el
usuario"""

def dibujar_rectangulo (x, y):
   for i in range (y):
       print("X"*y)

x = int (input ("Ingrese una cantidad para los ejes X: \n"))
y = int (input ("Ingrese una cantidad para los ejes Y: \n"))

dibujar_rectangulo (x,y)



"""Cree una funcion que calcule el Factorial de un numero entero positivo"""

def factorial (num):
    resu_factorial = 1
    if num >= 0:
        for i in range (1, num+1):
            resu_factorial *= i
    else:
        print("El numero no esta dentro del rango\n")
            
    return resu_factorial

num = int (input("Ingrese un numero entero y positivo: \n"))
resultado = factorial (num)
print(f"El resultado de aplicar el factorial al numero {num} es :{resultado}")