#practica 10
#padilla valdez gustavo
#becerra gonzalez diego ivan

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
from time import sleep; #Llama la funcion para pausar
import gc; 
import os; #Llamo funciones del sistema operativo para poder borrar pantalla
init(autoreset=True); #Se inicia el colorama, que se autoresetee para evitar basura en la consola

def dibujo(errorcatch): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
        x += 1;
    for i in range(11):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+"   ");
        y += 1;
    x=1;
    y=3;
    for i in range(10):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+"  ");
        y += 1;

    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
        x+=1;
    #Este for sera para rellenar la ventana
    x=3;
    y=4;
    for i in range(9):
        for i2 in range (79):
            print(Cursor.POS(x,y)+Back.WHITE+" ");
            x += 1;
        x=3;
        y+=1;
    #En la esquina mandara a imprimir los errores con parametros
    errorcatch=str(errorcatch);
    print(Fore.BLACK+Cursor.POS(3,12)+Back.LIGHTRED_EX+Style.DIM+"Errores Except: "+errorcatch, end="");
    print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"", end="");
    
def estacionamiento(errorcatch): #Se hara una funcion que calcule el costo del estacionamiento
    aumento=[0]; #Inicializa las variables
    entrada=-1;
    salida=-1;
    pago=0;
    for i in aumento:
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese la hora de entrada: ", end="");
        entrada=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try:
            entrada=int(entrada);
            if entrada < 0 or entrada > 2399: #Si la hora no esta dentro del rango la volver a pedir
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingrese una hora correcta en formato militar!", end="");
                aumento.append(0);
                sleep(1);
            else:
                aux=str(entrada);
                if entrada > 9: #Si la hora tiene 2 o mas digitos
                    #Comparara que el penultimo digito no sea 6,7,8 o 9, para que entre en el rango del horario
                    if aux[-2] == "6" or aux[-2] == "7" or aux[-2] == "8" or aux[-2] == "9": 
                        dibujo(errorcatch);
                        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Error con los minutos ingresados!", end="");
                        aumento.append(0);
                        sleep(1);
                    else:
                        pass;
                else:
                    pass;

        except: #Si ingresa caracteres
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese numeros!", end="");
            aumento.append(0);
            sleep(1);

    aumento=[0];
    for i in aumento:
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese la hora de salida: ", end="");
        salida=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try:
            salida=int(salida);
            if salida <= entrada or salida > 2399:#Si la hora no esta dentro del rango la volver a pedir
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingrese una hora correcta en formato militar!", end="");
                aumento.append(0);
                sleep(1);
            else:
                aux=str(salida);
                if salida > 9:#Si la hora tiene 2 o mas digitos
                    #Comparara que el penultimo digito no sea 6,7,8 o 9, para que entre en el rango del horario
                    if aux[-2] == "6" or aux[-2] == "7" or aux[-2] == "8" or aux[-2] == "9":
                        dibujo(errorcatch);
                        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Error con los minutos ingresados!", end="");
                        aumento.append(0);
                        sleep(1);
                    else:
                        pass;
                else:
                    pass;

        except: #Si ingresa caracteres
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese numeros!", end="");
            aumento.append(0);
            sleep(1);

    total=salida-entrada; #Sacara el total que estuvo estacionado
    horas=total/100; #Sacara las horas, diviendolas entre 100
    if horas % 1 != 0: #Si existe punto decimal en las horas
        pago+=1000; #Se añadira el dinero de la primera hora
        aux=horas % 1;
        horas -= aux; #Se le restara el decimal a las horas, para que ya quede entero
        if horas == 0: #Si ya no hay mas horas no hace nada
            pass;
        else:
            pago= pago + (horas*600); #Si hay mas horas, este multiplica las restantes y las suma
    else: #Si no hay punto decimal
        pago+=1000; #El pago de la primera hora y la resta
        horas-=1;
        pago= pago + (horas*600); #Añadira lo de la primera hora y las demas horas

    dibujo(errorcatch);
    aux=str(pago);
    #Mandara a imprimir el total a pagar y para mejor comprension tambien las horas
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,4)+"Su total a pagar es de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    print(Fore.BLACK+Back.WHITE+" $ por ", end="");
    horas+=1;
    aux=str(horas);
    print(Fore.BLACK+Back.WHITE+aux, end="");
    print(Fore.BLACK+Back.WHITE+" horas.", end="");
    return(errorcatch); #Regresara el total de except al ejercicio
        

def e1(errorcatch):
    errorcatch=estacionamiento(errorcatch);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,7)+"Ejercicio 1", end="");
    input(Fore.BLACK+Cursor.POS(3,8)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e2(errorcatch):
    dibujo(errorcatch);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,7)+"Ejercicio 2", end="");
    input(Fore.BLACK+Cursor.POS(3,8)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e3(errorcatch):
    dibujo(errorcatch);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,7)+"Ejercicio 3", end="");
    input(Fore.BLACK+Cursor.POS(3,8)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e4(errorcatch):
    dibujo(errorcatch);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,7)+"Ejercicio 4", end="");
    input(Fore.BLACK+Cursor.POS(3,8)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu


def menu():
    errorcatch=0; #Inicializa la variables de errores except
    opcion=1;
    while opcion != 0: #Mientras la opcion no sea 0 para salir, seguira en el menu
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese el numero de ejercicio a ejecutar o 0 para salir: ", end="");
        opcion=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try:
            opcion=int(opcion);
            if opcion < 0 or opcion > 4: #Si esta fuera de rango
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingresa un numero valido!",end ="");
                sleep(1);   
            
            else: #En otro caso realizara la opcion pedida
                if opcion == 1:
                    errorcatch=e1(errorcatch);
                   
                if opcion == 2:
                    errorcatch=e2(errorcatch);
                    
                if opcion == 3:
                    errorcatch=e3(errorcatch);
                    
                if opcion == 4:
                    errorcatch=e4(errorcatch);
                   
                
        except: #Si ingresa caracteres
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese un numero entero!", end="");
            sleep(1);

    os.system("cls"); 
    pass;


menu();
print("\npractica 10");
print("padilla valdez gustavo");
print("becerra gonzalez diego ivan");

