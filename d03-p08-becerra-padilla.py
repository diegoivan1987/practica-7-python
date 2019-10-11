#practica 08
#becerra gonzalez diego ivan
#padilla valdez gustavo

def esfera(): #Funcion para calcular el area de una esfera
    pi = 3.1416;#Definimos pi
    radio = float(input("Dame el radio: ")); #Le pedimos al usuario el radio
    while radio <= 0: #Si es menor o igual a 0 este pedira que vuelva a ingresar el radio hasta que sea valido
        print("ERROR: El radio debe ser mayor que cero");
        radio = float(input("\nDame el radio: "));
    area = 4 * pi * (radio*radio);#Calculara el area con los datos ya dados
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
    cont = tabla; #La tabla empezara multiplicandose con el mismo valor ingresado
    if cont < 0: #Si pide la tabla de un numero negativo
        cont = cont * (-1); #Cambia el auxiliar contador a positivo para sacar los valores de la tabla
    
    while cont >=0: #Mientras que el contador sea mayor o igual a 0
        valor = tabla * cont; #Sacara el valor de cada multiplicacion
        print("\n",tabla, "x", cont, "=", valor); #Lo mandara a imprimir
        cont -= 1; #Y se le ira descontando 1 para ir en descendiente
        
def e3(): #Funcion para realizar el ejercicio 3
    print("\nEjercicio 3");
    tablas();

def numeros():#lee un numero que ingrese el usuario y lo imprime en negativo
    numero = 1;#se inicializa asi para que entre al while
    while numero != 0 :#mientras no ingrese la opcion de salida, seguira dentro
        numero = float(input("Ingresa un numero positivo o 0 para salir "));#guarda el valor del numero
        while numero < 0 :#mientras ingresa un numero negativo, pide que lo ingrese positivo
            numero = float(input("Debes ingresar un numero positivo "));
        if numero != 0 :#si el numero no es 0, imprime el negativo
            negativo = numero * -1;#hace la conversion a negativo
            print(negativo);
    
def e4():#Funcion para realizar el ejercicio 4
    print("\nEjercicio 4");
    numeros();

def cal_alumnos():#guarda las calificaciones de los alumnos, muestra la calificacion mas baja y la moda
    limite = float(input("Ingresa el numero de alumnos "));#ingresa el numero de alumnos
    while limite % 1 != 0: #Si ingresa decimal, lo pide de nuevo
        limite = float(input("Ingresa un numero entero "));#ingresa el numero de alumnos
    while limite < 0 : #Si ingresa un numero negativo, lo pide de nuevo
        limite = float(input("Ingresa un numero positivo "));#ingresa el numero de alumnos
        while limite % 1 != 0: #Si ingresa decimal, lo pide de nuevo, y asi no se lo salta
             limite = float(input("Ingresa un numero entero "));#ingresa el numero de alumnos
    contador = int(0);#contador que se usara como auxiliar
    calificaciones = [];#lista que guardara todas las calificaciones
    while contador < limite :#mientras el contador no supere al limite, se repetira
        print("Ingresa la calificacion del alumno ",contador+1);#pide la calificacion del alumno 
        calificaciones.append(float(input()));#la guarda en la lista
        while calificaciones[contador] < 0 or calificaciones[contador] > 100 :#si la calificacion no entra dentro del rango, la vuelve a pedir
            calificaciones[contador]=(float(input("Ingresa una calificacion valida ")));
        contador += 1;#aumenta el contador en 1
        
    contador = 0;
    print("\nLas calificaciones fueron:");
    while contador < limite :#imprime todas las calificaciones
        print("Alumno ",contador + 1," calificacion ",calificaciones[contador]);
        contador += 1;
        
    repeticiones = [];#aqui se guardaran cuantas veces se repite cada calificacion
    contador = 0;
    while contador < limite :#agregamos campos a la lista igual al numero de calificaciones
        repeticiones.append(0);#llenamos los campos con 0 para que al momento de introducir un numero de repeticion real, diferenciarlo
        contador += 1;

    contador = 0;
    contador2 = 0;
    while contador < limite :#recorremos la lista
        contador2 = 0;
        while contador2 < limite :#recorremos la lista de nuevo
            if calificaciones[contador] == calificaciones[contador2] :#comparara cada elemento de la lista y contara cuantas veces se repite cada uno
                repeticiones[contador] = (repeticiones[contador])+1;#guarda el numero de repeticiones en la otra lista
            contador2 += 1;
        contador += 1;

    contador = 0;
    mayor = 0;#guardara la mayor cantidad de repeticiones
    posicion_mayor = 0;#guardara la posicion del numero con mayor cantidad de repeticiones
    while contador < limite :#recorremos la lista
        if repeticiones[contador] > mayor :#si el numero de repeticiones es mayor al de la variable, se copia el numero mayor a la varibale
            mayor = repeticiones[contador];
            posicion_mayor = contador;#guarda la posicion del numero con mas repeticiones
        contador += 1;

    contador = 0;
    menor = 101;#guardara el numero menor
    posicion_menor = 0;#guardara la posicion del numero menor
    while contador < limite :
        if menor > calificaciones[contador] :#si hay un numero menor que 'menor', lo guarda
            menor = calificaciones[contador];
            posicion_menor = contador;
        contador += 1;
        
    #imprimimos los datos que nos piden
    print("La calificacion menor fue del alumno ",posicion_menor+1,"con calificacion de ",calificaciones[posicion_menor]);
    print("La moda es ",calificaciones[posicion_mayor],"con ",repeticiones[posicion_mayor],"repeticiones");
    
                

def e5():
    print("\nEjercicio 5");
    cal_alumnos();

def transito(): #Se leera las calcomanias de autos para saber cuantos autos tienen calcomania de cada color
    #Inicializamos las variables de las calcomanias
    amarillo = 0;
    rosa = 0;
    rojo = 0;
    verde = 0;
    azul = 0; 
    op=(int(input("Ingrese 1 si quiere ingresar una placa: "))); #Pregunta al usuario si quiere ingresar calcomania
    while op == 1: #Si es 1 ingresara la calcomania
        placa = (str(input("Digite el codigo de la placa: "))); #Pedira la calcomania
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
            print("Placa no valida!");
        op=(int(input("\nIngrese 1 si quiere ingresar otra placa: "))); #Pregunta al usuario si quiere ingresar otra calcomania

    #Imprime el total de cada calcomania
    print("Hay", amarillo, "calcomanias amarillas");
    print("Hay", rosa, "calcomanias rosas");
    print("Hay", rojo, "calcomanias rojas");
    print("Hay", verde, "calcomanias verdes");
    print("Hay", azul, "calcomanias azules");

def e6(): #Funcion para realizar el ejercicio 6
    print("\nEjercicio 6");
    transito();

def menu():#funcion que pide el ejercicio a ejecutar
    opcion = int(input("\nIngresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#le pide el ejercicio a ejecutar
    while opcion != 7 :#mientras no ingrese salir, el while se repetira
        if opcion == 1 :#si la opcion es = a 1 ejecuta el ejercicio 1
            e1();
            opcion = int(input("\nIngresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#vuelve a preguntar que opcion quiere
        elif opcion == 2 :#si la opcion es = a 2 ejecuta el ejercicio 2
            e2();
            opcion = int(input("\nIngresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#vuelve a preguntar que opcion quiere            
        elif opcion == 3 :#si la opcion es = a 3 ejecuta el ejercicio 3
            e3();
            opcion = int(input("\nIngresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#vuelve a preguntar que opcion quiere
        elif opcion == 4 :#si la opcion es = a 4 ejecuta el ejercicio 4
            e4();
            opcion = int(input("\nIngresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#vuelve a preguntar que opcion quiere
        elif opcion == 5 :#si la opcion es = a 5 ejecuta el ejercicio 5
            e5();
            opcion = int(input("\nIngresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#vuelve a preguntar que opcion quiere
        elif opcion == 6 :#si la opcion es = a 6 ejecuta el ejercicio 6
            e6();
            opcion = int(input("\nIngresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#vuelve a preguntar que opcion quiere
        else :#si ingresa cualquier otro numero, pide que ingrese uno correcto
            print("\nIngresa un numero valido");
            opcion = int(input("Ingresa el numero de ejercicio que quieres ejecutar y 7 para salir "));#vuelve a preguntar que opcion quiere
            

menu();

print("\npractica 08");
print("becerra gonzalez diego ivan");
print("padilla valdez gustavo");

