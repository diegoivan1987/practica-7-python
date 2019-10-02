#practica 08
#padilla valdez gustavo
#becerra gonzalez diego ivan

def esfera(): #Funcion para calcular el area de una esfera
    pi=3.1416;#Definimos pi para mayor comodidad
    radio=(float(input("Dame el radio: "))); #Le pedimos al usuario el radio
    while radio <= 0: #Si es menor o igual a 0 este pedira que vuelva a ingresar el radio hasta que sea valido
        print("ERROR: El radio debe ser mayor que cero");
        radio=(float(input("\nDame el radio: ")));
    area= 4 * pi * (radio*radio);#Calculara el area con los datos ya dados
    print("El área de una esfera de radio", radio, "es de:", area); #Y lo imprimira


def e1(): #Funcion para realizar el ejercicio 1
    print("\nEjercicio 1");
    esfera();

def cubo(): #Funcion para calcular el volumen de un cubo mientras se pueda
    arista = (float(input("Deme una arista:"))); #Pedimos la arista
    cont = 0; #Inicializamos el contador en 0
    while arista > 0: #Mientras la arista sea mayor a 0, seguira calculando volumenes
        cont += 1; #Se le añade 1 al contador por cada vez que calcula un volumen
        volumen = arista * arista * arista; #Saca el volumen del cubo
        print("El volumen del cubo de arista", arista,"es:", volumen); #Lo imprime
        print("Ha calculado el volumen de", cont, "cubos"); #Imprime cuantos volumenes se han calculado
        arista = (float(input("\nDeme una arista:"))); #Se vuelve a pedir la arista para seguir el ciclo

def e2(): #Funcion para realizar el ejercicio 2
    print("\nEjercicio 2");
    cubo();

def tablas(): #Imprimir la tabla de multiplicacion del numero que digite el usuario
    tabla = (float(input("Digite de cual numero quiera la tabla: "))); #Pide el numero de la tabla
    cont = tabla; #La tabla empezara multiplicandose con el mismo
    while cont >=0: #Mientras que el contador sea mayor o igual a 0
        valor = cont * tabla; #Sacara el valor de cada multiplicacion
        print(tabla, "x", cont, "=", valor); #Lo mandara a imprimir
        cont -=1; #Y se le ira descontando 1 para ir en descendiente
        
def e3(): #Funcion para realizar el ejercicio 3
    print("\nEjercicio 3");
    tablas();

  

def e4():
    pass;

def e5():
    pass;

def e6():
    pass;

def menu():
    pass;



