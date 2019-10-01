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

def e2():
    pass;

def e3():
    pass;

def e4():
    pass;

def e5():
    pass;

def e6():
    pass;

def menu():
    pass;


