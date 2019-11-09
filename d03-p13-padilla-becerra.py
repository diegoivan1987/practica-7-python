#practica 13
#padilla valdez gustavo
#becerra gonzalez diego ivan

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
from time import sleep; #Llama la funcion para pausar
import os; #Llamo funciones del sistema operativo para poder borrar pantalla
import msvcrt; #Llama funcion para poder leer lo que se presiona en el teclado
init(autoreset=True); #Se inicia el colorama, que se autoresetee para evitar basura en la consola

def dibujomenu(em,e1,e2,e3): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    for i in range(115):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x += 1;
    for i in range(26):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;
    x=1;
    y=3;
    for i in range(26):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;

    for i in range(117):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x+=1;
    #Los siguientes crearan el mini adornado tambien en el marco
    x=3;
    y=4;
    for i in range(111):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x += 1;
    for i in range(25):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;    
    x=3;
    y=4;
    for i in range(24):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;

    for i in range(111):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x+=1;
    #Este for sera para rellenar la ventana de errores
    x=98;
    y=21;
    for i in range(7):
        for i2 in range (16):
            print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
            x += 1;
        x=98;
        y+=1;
    #En la esquina mandara a imprimir los errores con parametros
    
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(98,21)+Back.LIGHTBLUE_EX+Style.BRIGHT+" ---Errores--- ", end="");
    errorcatch=str(em);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(98,22)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Menu:  "+errorcatch, end="");
    errorcatch=str(e1);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(98,23)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Ej. 1: "+errorcatch, end="");
    errorcatch=str(e2);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(98,24)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Ej. 2: "+errorcatch, end="");
    errorcatch=str(e3);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(98,25)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Ej. 3: "+errorcatch, end="");

def dibujoej(errorcatch,ej): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    for i in range(115):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x += 1;
    for i in range(26):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;
    x=1;
    y=3;
    for i in range(26):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;

    for i in range(117):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x+=1;
    #Los siguientes crearan el mini adornado tambien en el marco
    x=3;
    y=4;
    for i in range(111):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x += 1;
    for i in range(25):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;    
    x=3;
    y=4;
    for i in range(24):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;

    for i in range(111):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x+=1;
    #Este for sera para rellenar la ventana de errores
    x=98;
    y=21;
    for i in range(7):
        for i2 in range (16):
            print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
            x += 1;
        x=98;
        y+=1;
    
    #En la esquina mandara a imprimir los errores con parametros
    if errorcatch== -1: 
        pass;
    else:
        ej=str(ej);
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(50,4)+"--- Ejercicio "+ej+"---", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(98,21)+Back.LIGHTBLUE_EX+Style.BRIGHT+" ERRORES DEL", end="");
        errorcatch=str(errorcatch);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(98,22)+Back.LIGHTBLUE_EX+Style.BRIGHT+" EJERCICIO:  "+errorcatch, end="");

def reverse(s): #Funcion para hacer al reves una cadena y regresarla
  str = "" 
  for i in s: 
    str = i + str
  return str

def e1(errorcatch):
    errorcatch=inverso(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(6,27)+"Ejercicio 1 Terminado", end="");
    input();
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def inverso(errorcatch): 
    aumento=[0];
    for i in aumento:
        dibujoej(errorcatch,1);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,7)+"Ingrese el nombre del archivo a abrir: ", end=""); 
        name=str(input());
        try:
            archivo=open(name,mode="r",encoding="utf-8"); #Abre el archivo
            cont=0;
            inc=0;
            dibujoej(errorcatch,1);
            while(True):
                cont+=1;
                if cont+8>25: #Si ya no cabe en un lado, cambiara el parrafo hacia el otro lado
                    x=60;
                    inc+=1;
                    y=inc+8;
    
                else: #Si no lo deja del otro
                    x=6; 
                    y=cont+8;
                
                linea=archivo.readline();#Lee por linea los caracteres
                if not linea: #Si ya no hay lineas
                    break;
                imprimir=str(reverse(linea)); #Hace al reves las lineas
                imprimir=imprimir[1:];
                print(Fore.WHITE+Style.BRIGHT+Cursor.POS(x,y)+" ",imprimir, end=""); 
            archivo.close;

            archivo=open(name,mode="r",encoding="utf-8"); #Vuelve a abrir el archivo para evitar problemas
            leer=archivo.read(); #Por caracter lo lee
            palabras=leer.split();
            p_contador=0;
            c_contador=0;
            for i in palabras: #Cuenta el total de palabras en el texto
                p_contador+=1;
            for i in leer: #Cuenta el total de caracteres exceptuando espacios
                if i == " ":
                    pass;
                else:
                    c_contador+=1;
            archivo.close;
            aux=str(c_contador);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,6)+"El total de caracteres del archivo fue de: ",aux, end="");
            aux=str(p_contador);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,7)+"El total de palabras del archivo fue de: ",aux, end="");
        except:
            errorcatch+=1;
            aumento.append(0);
            dibujoej(errorcatch,1);
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,7)+"Ese archivo no se encontro, Verifique el nombre ", end=""); 
            sleep(2);
    return errorcatch;


def e2(errorcatch):
    
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(6,27)+"Ejercicio 2 Terminado", end="");
    input();
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e3(errorcatch):#recibe un texto y para cada caracter imprime la palabra mas larga donde se encuentra
  
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(6,27)+"Ejercicio 3 Terminado", end="");
    input();
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def menu():
    errorm=0;
    errore1=0; #Inicializa la variables de errores except
    errore2=0; #Inicializa la variables de errores except
    errore3=0; #Inicializa la variables de errores except
    opcion=1;
    while opcion != 0: #Mientras la opcion no sea 0 para salir, seguira en el menu
        dibujomenu(errorm,errore1,errore2,errore3);
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(40,4)+"---Bienvenido a la Practica 13---", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(40,7)+Style.BRIGHT+"-Presione 1 para el ejercicio 1-", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(40,9)+Style.BRIGHT+"-Presione 2 para el ejercicio 2-", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(40,11)+Style.BRIGHT+"-Presione 3 para el ejercicio 3-", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(40,13)+Style.BRIGHT+"   Presione ESC para terminar   ", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(40,15)+Style.BRIGHT+"      ESCRIBA SU OPCION:  ", end="");
     
        caracter=0;
        while caracter==0: #Leera todas las teclas que se presionen hasta que presione una valida
            aux=str(msvcrt.getch());
            if "1b" in aux: #1b es el hexadecimal para ESC, si esta eso en lo leido, significa que presiono esc
                opcion=0;
                caracter+=1;
            elif "b'1'" == aux: #Lo mismo con b'1' b'2' b'3', y en vez de input este cambiara la opcion al presionar su tecla
                opcion=1;
                caracter+=1;
            elif "b'2'" == aux:
                opcion=2;
                caracter+=1;
            elif "b'3'" == aux:
                opcion=3;
                caracter+=1;
            else:
                pass;
            
        if opcion == 1:
            errore1=e1(errore1);
                   
        if opcion == 2:
            errore2=e2(errore2);
                    
        if opcion == 3:
            errore3=e3(errore3);
            
menu();
dibujoej(-1,1);
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,7)+"practica 13", end="");
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,8)+"padilla valdez gustavo", end="");
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,9)+"becerra gonzalez diego ivan", end="");
input();
os.system("cls");