#practica 10
#padilla valdez gustavo
#becerra gonzalez diego ivan

from colorama import Cursor,Fore,Back,init,Style; 
from time import sleep;
import os;

def dibujo(errorcatch):
    init();
    
    os.system("cls");
    x=1;
    y=3;
    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTCYAN_EX+" ");
        x += 1;
    for i in range(11):
        print(Cursor.POS(x,y)+Back.LIGHTCYAN_EX+"   ");
        y += 1;
    x=1;
    y=3;
    for i in range(10):
        print(Cursor.POS(x,y)+Back.LIGHTCYAN_EX+"  ");
        y += 1;

    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTCYAN_EX+" ");
        x+=1;

    x=3;
    y=4;
    for i in range(9):
        for i2 in range (79):
            print(Cursor.POS(x,y)+Back.WHITE+" ");
            x += 1;
        x=3;
        y+=1;
    
    errorcatch=str(errorcatch);
    print(Fore.BLACK+Cursor.POS(3,12)+Back.RED+Style.DIM+"Errores Macros: "+errorcatch, end="");
    print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"", end="");
    init(autoreset=True);
    
    
    


def e1(errorcatch):
    dibujo(errorcatch);
    print(Cursor.POS(3,4)+"Ejercicio 1", end="");
    input();
def e2(errorcatch):
    dibujo(errorcatch);
    print(Cursor.POS(3,4)+"Ejercicio 2", end="");
    input();
def e3(errorcatch):
    dibujo(errorcatch);
    print(Cursor.POS(3,4)+"Ejercicio 3", end="");
    input();
def e4(errorcatch):
    dibujo(errorcatch);
    print(Cursor.POS(3,4)+"Ejercicio 4", end="");
    input();


def menu():
    errorcatch=0;
    aumento=[0];
    for i in aumento:
        dibujo(errorcatch);
        
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese el numero de ejercicio a ejecutar o 0 para salir ", end="");
        
        opcion=str(input());
        
        try:
            opcion=int(opcion);
            if opcion < 0 or opcion > 4:
                
                dibujo(errorcatch);
                print(Cursor.POS(3,4)+"Ingresa un numero valido!",end ="");
                sleep(1);
                aumento.append(0);
              
            else:
                if opcion == 1:
                    e1(errorcatch);
                    aumento.append(0);
                if opcion == 2:
                    e2(errorcatch);
                    aumento.append(0);
                if opcion == 3:
                    e3(errorcatch);
                    aumento.append(0);
                if opcion == 4:
                    e4(errorcatch);
                    aumento.append(0);
                if opcion == 0:
                    pass;
        except:
            errorcatch+=1;
            dibujo(errorcatch);
            print(Cursor.POS(3,4)+"ERROR! Ingrese un numero entero!", end="");
            sleep(1);
            aumento.append(0);




    
    os.system("cls");
    pass;


menu();

print("\npractica 10");
print("padilla valdez gustavo");
print("becerra gonzalez diego ivan");

