#practica 12
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
    for i in range(100):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x += 1;
    for i in range(14):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;
    x=1;
    y=3;
    for i in range(14):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;

    for i in range(102):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x+=1;
    #Los siguientes crearan el mini adornado tambien en el marco
    x=3;
    y=4;
    for i in range(96):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x += 1;
    for i in range(13):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;    
    x=3;
    y=4;
    for i in range(12):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;

    for i in range(96):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x+=1;
    #Este for sera para rellenar la ventana de errores
    x=83;
    y=5;
    for i in range(11):
        for i2 in range (16):
            print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
            x += 1;
        x=83;
        y+=1;
    #En la esquina mandara a imprimir los errores con parametros
    
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,5)+Back.LIGHTBLUE_EX+Style.BRIGHT+" ---Errores--- ", end="");
    errorcatch=str(em);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,7)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Menu:  "+errorcatch, end="");
    errorcatch=str(e1);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,8)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Ej. 1: "+errorcatch, end="");
    errorcatch=str(e2);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,9)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Ej. 2: "+errorcatch, end="");
    errorcatch=str(e3);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,10)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  Ej. 3: "+errorcatch, end="");

def dibujoej(errorcatch): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    for i in range(100):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x += 1;
    for i in range(14):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;
    x=1;
    y=3;
    for i in range(14):
        print(Cursor.POS(x,y)+Back.RED+"  ");
        y += 1;

    for i in range(102):
        print(Cursor.POS(x,y)+Back.RED+" ");
        x+=1;
    x=3;
    y=4;
    for i in range(96):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x += 1;
    for i in range(13):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;    
    x=3;
    y=4;
    for i in range(12):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"**");
        y += 1;

    for i in range(96):
        print(Cursor.POS(x,y)+Back.LIGHTRED_EX+Fore.BLACK+"*");
        x+=1;
    #Este for sera para rellenar la ventana de errores
    x=83;
    y=5;
    for i in range(11):
        for i2 in range (16):
            print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
            x += 1;
        x=83;
        y+=1;
    #En la esquina mandara a imprimir los errores con parametros
    if errorcatch== -1: 
        pass;
    else:
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,5)+Back.LIGHTBLUE_EX+Style.BRIGHT+" ERRORES DEL", end="");
        errorcatch=str(errorcatch);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,7)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  EJERCICIO:  "+errorcatch, end="");

def e1(errorcatch):
   
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,9)+"Ejercicio 1 Terminado", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,10)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e2(errorcatch):
    
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(3,10)+"Ejercicio 2 Terminado", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(3,11)+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def pregunta_cadena():#pregunta la cadena a analizar en el ejercicio 3
    cadena = input(str(Fore.WHITE+Style.BRIGHT+Cursor.POS(5,5)+"Ingresa una cadena: "));
    return cadena;

def separar_letras(cadena):#separa la cadena en letras y las ingresa a un diccionario
    diccionario_letras = set();#diccionario que guardara las letras sin repetirse
    for letra in cadena :
        diccionario_letras.add(letra);
    try:#tratamos de quitar los espacios
        diccionario_letras.remove(" ");
    except:
        pass;
        
    return diccionario_letras;

def encuentra_letra(letras,palabras,diccionario,errorcatch):#encuentra la palabra mas larga donde esta cierta letra e imprime el diccionario
    for letra in letras:#recorre cada letra
        for palabra in palabras:#recorre cada palabra
            if letra in palabra:#si la letra esta en la palabra
                if letra in diccionario:#si ya hay una entrada de esa letra en el diccionario
                    if len(diccionario[letra][0]) < len(palabra):#si la entrada del diccionario es menor a la palabra actual
                        diccionario[letra]=[palabra];#guarda la palabra actual en el diccionario, ya que es la mas larga
                    elif len(diccionario[letra][0]) == len(palabra):#si la palabra actual y la del dicionario tienen el mismo largo
                        diccionario[letra].append(palabra);#guarda las dos en el diccionario
                else:#si no, la agrega al diccionario con la correspondiente palabra actual
                    diccionario[letra]=[palabra];
    if len(letras) > 0:#si existe alguna letra, lo que significa que hay palabra(s)
        dibujoej(errorcatch);
        abajo = 5;
        for letra in letras:#imprimimos el diccionario
            if abajo == 15:
                abajo = 5;
                print(Fore.WHITE+Style.BRIGHT+Cursor.POS(35,abajo)+"Letra ",letra,"palabra(s): ",diccionario[letra]);
            else:
                print(Fore.WHITE+Style.BRIGHT+Cursor.POS(5,abajo)+"Letra ",letra,"palabra(s): ",diccionario[letra]);
                abajo += 1;
    else:
        dibujoej(errorcatch);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(5,5)+"Diccionario vacio");

    return errorcatch;


def e3(errorcatch):#recibe un texto y para cada caracter imprime la palabra mas larga donde se encuentra
    letras_palabras = {};#diccionario que guardara cada letra y la palabra mas grande donde esta
    dibujoej(errorcatch);
    cadena = pregunta_cadena();#preguntar cadena
    letras = separar_letras(cadena);#ver cuales caracteres sin repetir componen la cadena
    palabras = cadena.split();#separar cadena en palabras y guardarla en una lista
    errorcatch = encuentra_letra(letras,palabras,letras_palabras,errorcatch);#encontrar la palabra mas larga donde
    #esta cada caracter
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(5,15)+"Ejercicio 3 Terminado", end="");
    input(Fore.WHITE+Style.BRIGHT+Cursor.POS(5,14)+"");
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
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(35,4)+"---Bienvenido a la Practica 12---", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(35,6)+Style.BRIGHT+"-Presione 1 para el ejercicio 1-", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(35,7)+Style.BRIGHT+"-Presione 2 para el ejercicio 2-", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(35,8)+Style.BRIGHT+"-Presione 3 para el ejercicio 3-", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(35,9)+Style.BRIGHT+"   Presione ESC para terminar   ", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(35,11)+Style.BRIGHT+"     ESCRIBA SU OPCION:  ", end="");
     
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
dibujoej(-1);
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,7)+"practica 12", end="");
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,8)+"padilla valdez gustavo", end="");
print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,9)+"becerra gonzalez diego ivan", end="");
input();
os.system("cls");
