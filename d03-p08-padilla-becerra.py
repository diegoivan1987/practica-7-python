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
    if cont < 0: #Si pide la tabla de un numero negativo
        cont = cont * (-1); #Cambia el auxiliar contador a positivo para sacar los valores de la tabla
    
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

def transito(): #Se leera las calcomanias de autos para saber cuantos autos tienen calcomania de cada color
    #Inicializamos las variables de las calcomanias
    amarillo = 0;
    rosa = 0;
    rojo = 0;
    verde = 0;
    azul = 0; 
    op=(int(input("Ingrese 1 si quiere ingresar una calcomania: "))); #Pregunta al usuario si quiere ingresar calcomania
    while op == 1: #Si es 1 ingresara la calcomania
        placa = (str(input("Digite el codigo de la calcomania: "))); #Pedira la calcomania
        #Comparara el ultimo caracter y dependiendo de que numero sea añadira a la variable de la respectiva calcomania 1
        if placa[-1] == "1" or placa[-1] == "2" : 
            amarillo += 1; 
        elif placa[-1] == "3" or placa[-1] == "4" :
            rosa += 1;
        elif placa[-1] == "5" or placa[-1] == "6" :
            rojo += 1;
        elif placa[-1] == "7" or placa[-1] == "8" :
            verde += 1;
        elif placa[-1] == "9" or placa[-1] == "0" :
            azul += 1;
        else : #Si su ultimo caracter no es un numero, la calcomania no sera valida
            print("Calcomania no valida!");
        op=(int(input("\nIngrese 1 si quiere ingresar otra calcomania: "))); #Pregunta al usuario si quiere ingresar otra calcomania

    #Imprime el total de cada calcomania
    print("Hay", amarillo, "calcomanias amarillas");
    print("Hay", rosa, "calcomanias rosas");
    print("Hay", rojo, "calcomanias rojas");
    print("Hay", verde, "calcomanias verdes");
    print("Hay", azul, "calcomanias azules");

def e6(): #Funcion para realizar el ejercicio 6
    print("\nEjercicio 6");
    transito();

def menu():
    pass;




