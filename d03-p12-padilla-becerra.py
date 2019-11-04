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

def dibujoej(errorcatch,ej): #Esta funcion creara la ventana siempre que se necesite con colores
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
        ej=str(ej);
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(35,4)+"--- Ejercicio "+ej+"---", end="");
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,6)+Back.LIGHTBLUE_EX+Style.BRIGHT+" ERRORES DEL", end="");
        errorcatch=str(errorcatch);
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(83,7)+Back.LIGHTBLUE_EX+Style.BRIGHT+"  EJERCICIO:  "+errorcatch, end="");

def e1(errorcatch):
    errorcatch=repeticiones(errorcatch);
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(6,16)+"Ejercicio 1 Terminado", end="");
    input();
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def repeticiones(errorcatch): #Se hara un diccionario donde muestre que tantas palabras se repitieron y el mayor sera impreso al final
    dibujoej(errorcatch,1);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,7)+"Ingresa una cadena: ", end=""); 
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,8)+"", end="");
    cadena=str(input());

    cadena=cadena.lower(); #Transforma lo que puso el usuario a todo minusculas primero
    lista=cadena.split(); #Luego lo separa por los espacios
    listaF={}; #Se crea el diccionario donde se guardaran

    print("",end="");
    for y in lista: #Estos compararan cada dato con cada uno de los otros para verificar los que se repiten
        aux=0;
        for x in lista:
            if y == x : #En caso de que se repita, se le sumara 1 al auxiliar para las repeticiones
                aux+=1;
        listaF[y]=[aux]; #Añadira la palabra y sus repeticiones al diccionario

    mayor=1;
    contador=0;
    valores=list(listaF.values());
    for i in valores: #Este for sera para ver cual fue la palabra que mas se repitio
        x=i;
        x=x[0];
        x=int(x);
        if x > mayor:
            mayor=x;
            
    final=list(listaF.items());        
    for i in final: #Este for sera para evitar un bucle infinito, sabiendo cuantas palabras fueron tuvieron la mayor repeticion
        x=str(mayor);
        y=str(i);
        if x in y and mayor > 1:
            contador+=1;
    inf=0;
    it=0;
    posiciones=[];
    for i in final: #Este for movera de cierta manera los datos al final, si este tiene el valor mas alto de repeticiones
        x=str(mayor);
        y=str(i);
        if x in y and inf < contador and mayor != 1:
            inf+=1;
            var=y;
            posiciones.append(it);
            final.append(var);
        it+=1;
    it=0;
    for i in posiciones: #Este for eliminara los datos que se reinserte
        x=int(i);
        del(final[x-it]);
        it+=1;
    it=0;
    case=2;

    #Se imprimira en minusculas o mayusculas dependiendo de que dato se
    dibujoej(errorcatch,1);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(5,5)+"El diccionario final fue:", end="");
    cord=6;
    for i in final:
        x=str(i);
        y=str(mayor);
        it+=1;
        if y in x: #Si se imprimiran el o los valores mayores, este cambiara al ultimo ingresado con las variables case
            if case==1:
                x=x.lower();
            else:
                x=x.upper();
        else: 
            if it % 2 == 0: #Los ifs por medio de division definen su posicion
                x=x.lower();
                case=1;
            else:
                x=x.upper();
                case=2;         
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(5,cord)+x, end="");
        cord+=1;
    return errorcatch;

def e2(errorcatch):
    
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(6,13)+"Ejercicio 2 Terminado", end="");
    input();
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def e3(errorcatch):
    
    print(Fore.WHITE+Style.BRIGHT+Back.LIGHTMAGENTA_EX+Cursor.POS(6,13)+"Ejercicio 3 Terminado", end="");
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