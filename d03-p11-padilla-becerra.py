#practica 11
#padilla valdez gustavo
#becerra gonzalez diego ivan

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
from time import sleep; #Llama la funcion para pausar
import os; #Llamo funciones del sistema operativo para poder borrar pantalla
init(autoreset=True); #Se inicia el colorama, que se autoresetee para evitar basura en la consola

def dibujomenu(em,e1,e2,e3,e4): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+" ");
        x += 1;
    for i in range(11):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+"   ");
        y += 1;
    x=1;
    y=3;
    for i in range(10):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+"  ");
        y += 1;

    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+" ");
        x+=1;
    #Este for sera para rellenar la ventana de errores
    x=3;
    y=14;
    for i in range(3):
        for i2 in range (79):
            print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
            x += 1;
        x=3;
        y+=1;
    #En la esquina mandara a imprimir los errores con parametros
    else:
        errorcatch=str(em);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,16)+Back.LIGHTBLUE_EX+Style.BRIGHT+"Errores Menu: "+errorcatch, end="");
        errorcatch=str(e1);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,14)+Back.LIGHTBLUE_EX+Style.BRIGHT+"Errores en Ej. 1: "+errorcatch, end="");
        errorcatch=str(e2);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(35,14)+Back.LIGHTBLUE_EX+Style.BRIGHT+"Errores en Ej. 2: "+errorcatch, end="");
        errorcatch=str(e3);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,15)+Back.LIGHTBLUE_EX+Style.BRIGHT+"Errores en Ej. 3: "+errorcatch, end="");
        errorcatch=str(e4);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(35,15)+Back.LIGHTBLUE_EX+Style.BRIGHT+"Errores en Ej. 4: "+errorcatch, end="");

def dibujoej(errorcatch): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+" ");
        x += 1;
    for i in range(11):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+"   ");
        y += 1;
    x=1;
    y=3;
    for i in range(10):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+"  ");
        y += 1;

    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+" ");
        x+=1;
    #Este for sera para rellenar la ventana
    x=3;
    y=14;
    for i in range(3):
        for i2 in range (79):
            print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
            x += 1;
        x=3;
        y+=1;
    #En la esquina mandara a imprimir los errores con parametros
    if errorcatch== -1: 
        pass;
    else:
        errorcatch=str(errorcatch);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,15)+Back.LIGHTBLUE_EX+Style.BRIGHT+"Errores del Ejercicio : "+errorcatch, end="");
       
def nombres(errorcatch):#guarda nombres y devuelve los nombres que terminen con cierta letra
    #declarar las variables
    nombre = "";#guardara el nombre a agregar
    letra = "";#guardara la letra a buscar
    opcion = 1;#guardara la opcion elegida, se inicializa en 1 para que entre al while al principio
    nombresL = set();#conjunto que guardara los nombres
    while opcion != 3:#mientras opcion sea != 3
        dibujoej(errorcatch);
        
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Ingresa 1 para agregar un nombre",end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,5)+"Ingresa 2 para buscar nombres que terminen con cierta letra",end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,6)+"Ingresa 3 para ir al menu: ",end="");
        opcion = str(input());
        try:
            opcion = int(opcion);
            if opcion < 0 and opcion > 3:#si no esta dentro del rango
                dibujoej(errorcatch);
                print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Debes de ingresar una opcion dentro del rango",end="");
                sleep(1);
            if opcion == 1:#si opcion = 1
                dibujoej(errorcatch);
                nombre = str(input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Ingresa un nombre: "));#ingresa un nombre
                print("",end="");
                #se busca el nombre
                if nombre in nombresL: #si el nombre existe
                    dibujoej(errorcatch);
                    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"El nombre ya existe",end="");
                    sleep(1);
                else:#en otro caso
                    nombresL.add(nombre);#se guarda el nombre
            if opcion == 2:#si opcion = 2
                contador=0;
                dibujoej(errorcatch);
                letra = str(input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Ingresa la letra a buscar al final: "));#ingresa una letra a buscar
                print("",end="");
                dibujoej(errorcatch);
                for i in nombresL:
                    if i[-1] == letra:#si la ultima letra es igual a la letra a buscar
                        contador+=1;
                        dibujoej(errorcatch);
                        aux=str(contador);
                        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+aux+"# Nombre en coincidencia: "+i,end="");#imprimir el nombre    
                        input(); 
                if contador==0:
                    dibujoej(errorcatch);
                    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"No hubo ningun nombre",end="");#imprimir el nombre 
                    sleep(1);   
            if opcion == 3:#si opcion = 3
                pass;#sale
        except:
            errorcatch+=1;
            dibujoej(errorcatch);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"1.-Debes de ingresar numeros como opcion",end="");
            sleep(1);
            #errore1 += 1;#se suma 1 al contador de errores
    return errorcatch;

def cadena_corta(errorcatch):
    #declarar las variables
    nombre = "";#guardara el nombre a agregar
    opcion = 1;#guardara la opcion elegida, se inicializa en 1 para que entre al while al principio
    cadenas = []; #Se inicializara las cadenas como tabla
    contador=0;
    menor="";
    while opcion != 2:#mientras opcion sea != 3
        dibujoej(errorcatch);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Ingresa 1 para agregar una cadena",end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,5)+"Ingresa 2 para terminar e imprimir la cadena corta: ",end="");
        opcion = str(input());
        try: #Para evitar que ingrese caracteres
            opcion = int(opcion);
            if opcion < 1 and opcion > 2:#si no esta dentro del rango 
                dibujoej(errorcatch);
                print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Debes de ingresar una opcion dentro del rango",end="");
                sleep(1);
            if opcion == 1:#si elige meter otra cadena
                dibujoej(errorcatch);
                nombre = str(input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Ingresa un cadena: "));#ingresa un nombre
                print("",end="");
                contador+=1;
                cadenas.append(nombre);#se guarda el nombre
            if opcion == 2:#si opcion ya quiere ver el resultado
                cadenasC=set(cadenas); #Cambia la lista a conjunto para evitar repetidos
                cadenas=[];
                if contador==0:
                    dibujoej(errorcatch);
                    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"No se ingreso ninguna cadena",end="");
                else:
                    for i in cadenasC:
                        cadenas.append(i);
                    comparador=len(cadenas[0]);
                    menor=cadenas[0];
                    for i in range(contador): #Compara si la longitud de la cadena es menor y la cambia si es asi
                        if len(cadenas[i]) < comparador:
                            menor=cadenas[i];
                        comparador=len(cadenas[i]);
                    #Se imprime el conjunto en orden, y la cadena mas corta
                    dibujoej(errorcatch);
                    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"De las cadenas en orden: ",end="");
                    print(cadenas,end="");
                    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,5)+"La cadena primera mas corta fue: "+menor,end="");
        
        except:
            errorcatch+=1;
            dibujoej(errorcatch);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"-Debes de ingresar numeros como opcion-",end="");
            sleep(1);
            
    return errorcatch;

def longitud(errorcatch): #Se hara una funcion donde se impriman subcadenas de longitud dada por el usuario
    dibujoej(errorcatch);
    
    aumento=[0];
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Dame una cadena:");
    cadena = str(input(Cursor.POS(3,5)));
    subs=set(); #Declarara el set que guardara las subcadenas
    for i in aumento: #For para evitar que el usuario ingrese caracteres junto al try, except
        dibujoej(errorcatch);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"Dame la longitud de las subcadenas:");
        lon = str(input(Cursor.POS(3,5)));
        try:
            lon=int(lon);
            i=0;
            while i <= len(cadena): 
                #Hara un while para que mientras este dentro de la longitud de la cadena, cree subcadenas y las añada al conjunto
                aux=cadena[i:i+lon];
                if len(aux)==lon: #Si no alcanza a tener la longitud que pidio el usuario, no lo añadira
                    subs.add(aux);     
                i+=lon;
                
            #Imprimira las subcadenas
            dibujoej(errorcatch);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"-Subcadenas resultantes-");
            print(Cursor.POS(3,5),end="");
            for i in subs:
                print(Fore.WHITE+Style.BRIGHT+" '"+i+"' ",end="");
            
        except: #En caso de que ingrese caracteres
            errorcatch+=1;
            dibujoej(errorcatch);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+"-Debes de ingresar numeros como longitud-",end="");
            sleep(1);
            aumento.append(0);
    return errorcatch;

def e1(errorcatch):
    errorcatch=nombres(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,9)+"Ejercicio 1 Terminado", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,10)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e2(errorcatch):
    errorcatch=cadena_corta(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,10)+"Ejercicio 2 Terminado", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,11)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def pasa_a_lista(nombres):#pasa el conjunto a una lista
    nombresList = [];#lista que guardara el conjunto
    for i in nombres:#recorre el conjunto
        nombresList.append(i);#agrega el elemento del conjunto a la lista
    return nombresList;

def min_prefijo(nombresList):#devuelve el min comun prefijo
    tam_min = 0;#guardara el tamaño de la palabra mas corta, porque no puede haber un prefijo mas grande
    #que la palabra mas corta, servira como limite para comparar carecteres
    mcp = "";#guardara el minimo comun prefijo
    aux = "";#servira para comparar cada elemento de la cadena con la siguiente cadena
    primer_vuelta = 1;
    if len(nombresList) == 0:#si la lista esta vacia
        return "no tiene ";
    
    tam_min = len(nombresList[0]);#se asigna el tamaño del primer nombre de la lista
    for i in range(len(nombresList)):#se recorre la lista
        tam_min = min(len(nombresList[i]), tam_min);#guarda el tamaño de la palabra mas pequeña

    i = 0;#servira para determinar el tamaño del mcp
    while i < tam_min:#mientras el prefijo sea menor a la palabra mas corta
        aux = nombresList[0][i];#tomara como referencia el caracter de la posicion i de la primer cadena
        for j in range(1,len(nombresList)):#recorrera la lista a partir de la segunda cadena
            if nombresList[j][i] != aux:#si la primer letra de la cadena con posicion j no es igual
                #a la primer letra de la primera cadena, significa que no hay mcp
                aux = "";#se agrega nada al mcp para no afectarlo
        mcp = mcp + aux;#se agrega la letra que se tiene en comun al mcp
        i += 1;#se aumenta i en 1 para comparar la siguiente letra
    if len(mcp) == 0:#si no hay mcp
        return "no tiene ";
    else:
        return mcp;#se retorna el mcp
     
def prefijo():#permite ingresar varias cadenas de texto e imprime el prefijo comun mas corto
    #declarar las variables
    nombre1 = "";#guardara el nombre a agregar
    prefijo = "";#guardara el prefijo
    opcion = 1;#guardara la opcion elegida, se inicializa en 1 para que entre al while al principio
    nombres = set();#conjunto que guardara los nombres
    nombresList = [];#lista que guardara el conjunto
    while opcion != 3:#mientras opcion sea != 3
        opcion = str(input("Ingresa 1 para agregar un nombre, 2 para imprimir el prefijo comun mas corto y 3 para ir al menu: "));
        try:
            opcion = int(opcion);
            if opcion < 0 and opcion > 3:#si no esta dentro del rango
                print("Debes de ingresar una opcion dentro del rango");
            if opcion == 1:#si opcion = 1
                nombre1 = str(input("Ingresa un nombre: "));#ingresa un nombre
                #se busca el nombre
                if nombre1 in nombres: #si el nombre existe
                    print("El nombre ya existe");
                else:#en otro caso
                    nombres.add(nombre1);#se guarda el nombre
            if opcion == 2:#si opcion = 2
                nombresList = pasa_a_lista(nombres);
                prefijo = min_prefijo(nombresList);
                print(prefijo," prefijo comun");#se imprime el prefijo comun               
            if opcion == 3:#si opcion = 3
                pass;#sale
        except:
            print("3.-Debes de ingresar numeros como opcion");

def e3(errorcatch):
    prefijo();
    dibujoej(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,10)+"Ejercicio 3 Terminado", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,11)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu


def e4(errorcatch):
    errorcatch=longitud(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,11)+"Ejercicio 4 Terminado", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,12)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu


def menu():
    errorm=0;
    errore1=0; #Inicializa la variables de errores except
    errore2=0; #Inicializa la variables de errores except
    errore3=0; #Inicializa la variables de errores except
    errore4=0; #Inicializa la variables de errores except
    opcion=1;
    while opcion != 0: #Mientras la opcion no sea 0 para salir, seguira en el menu
        dibujomenu(errorm,errore1,errore2,errore3,errore4);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+Style.BRIGHT+"---Bienvenido a la Practica 11---", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,5)+Style.BRIGHT+"-Ingrese 1 para el ejercicio 1", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,6)+Style.BRIGHT+"-Ingrese 2 para el ejercicio 2", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,7)+Style.BRIGHT+"-Ingrese 3 para el ejercicio 3", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,8)+Style.BRIGHT+"-Ingrese 4 para el ejercicio 4:  ", end="");

        opcion=str(input(Fore.WHITE+Style.BRIGHT));
        print("",end="");
        try:
            opcion=int(opcion);
            if opcion < 0 or opcion > 4: #Si esta fuera de rango
                dibujomenu(errorm,errore1,errore2,errore3,errore4);
                print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+Cursor.POS(3,4)+"Ingresa un numero valido!",end ="");
                sleep(1);   
            
            else: #En otro caso realizara la opcion pedida
                if opcion == 1:
                    errore1=e1(errore1);
                   
                if opcion == 2:
                    errore2=e2(errore2);
                    
                if opcion == 3:
                    errore3=e3(errore3);
                    
                if opcion == 4:
                    errore4=e4(errore4);
                   
                
        except: #Si ingresa caracteres
            errorm+=1;
            dibujomenu(errorm,errore1,errore2,errore3,errore4);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+Cursor.POS(3,4)+"ERROR! Ingrese un numero entero!", end="");
            sleep(1);


menu();
dibujoej(-1);
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+Cursor.POS(3,4)+"practica 11", end="");
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+Cursor.POS(3,5)+"padilla valdez gustavo", end="");
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+Cursor.POS(3,6)+"becerra gonzalez diego ivan", end="");
input();
os.system("cls");
