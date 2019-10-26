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
    else:
        errorcatch=str(em);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,16)+Back.LIGHTBLUE_EX+Style.DIM+"Errores Menu: "+errorcatch, end="");
        errorcatch=str(e1);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,14)+Back.LIGHTBLUE_EX+Style.DIM+"Errores en Ej. 1: "+errorcatch, end="");
        errorcatch=str(e2);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(35,14)+Back.LIGHTBLUE_EX+Style.DIM+"Errores en Ej. 2: "+errorcatch, end="");
        errorcatch=str(e3);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,15)+Back.LIGHTBLUE_EX+Style.DIM+"Errores en Ej. 3: "+errorcatch, end="");
        errorcatch=str(e4);
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(35,15)+Back.LIGHTBLUE_EX+Style.DIM+"Errores en Ej. 4: "+errorcatch, end="");

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
        print(Fore.BLACK+Style.BRIGHT+Cursor.POS(3,15)+Back.LIGHTBLUE_EX+Style.DIM+"Errores del Ejercicio : "+errorcatch, end="");
       
           
    
def e1(errorcatch):
    dibujoej(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,6)+"Ejercicio 1", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,7)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e2(errorcatch):
    dibujoej(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,10)+"Ejercicio 2", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,11)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e3(errorcatch):
    dibujoej(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,10)+"Ejercicio 3", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,11)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu


def e4(errorcatch):
    dibujoej(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,8)+"Ejercicio 4", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,9)+"");
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
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,4)+Style.DIM+"---Bienvenido a la Practica 11---", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,5)+Style.DIM+"-Ingrese 1 para el ejercicio 1", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,6)+Style.DIM+"-Ingrese 2 para el ejercicio 2", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,7)+Style.DIM+"-Ingrese 3 para el ejercicio 3", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,8)+Style.DIM+"-Ingrese 4 para el ejercicio 4:  ", end="");

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
                    errore3=e2(errore2);
                    
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
