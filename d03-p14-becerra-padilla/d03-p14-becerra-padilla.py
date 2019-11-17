#practica 14
#becerra gonzalez diego ivan
#padilla valdez gustavo

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
from time import sleep; #Llama la funcion para pausar
import os; #Llamo funciones del sistema operativo para poder borrar pantalla
import msvcrt; #Llama funcion para poder leer lo que se presiona en el teclado
init(autoreset=True); #Se inicia el colorama, que se autoresetee para evitar basura en la consola

def ventana(xM,yM,hosp,dom): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    aux=0;
    for i in range(xM):
        print(Cursor.POS(x,y)+Back.BLUE+" ");
        x += 1;

    for i in range(yM):
        print(Cursor.POS(x,y)+Back.BLUE+"  ");
        y += 1;
    x=1;
    y=3;
    for i in range(yM):
        print(Cursor.POS(x,y)+Back.BLUE+"  ");
        y += 1;

    for i in range(xM+2):
        print(Cursor.POS(x,y)+Back.BLUE+" ");
        x+=1;
    #Los siguientes crearan el mini adornado tambien en el marco
    x=3;
    y=4;
    for i in range(xM-4):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"*");
        x += 1;
    for i in range(yM-1):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"**");
        y += 1;    
    x=3;
    y=4;
    for i in range(yM-2):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"**");
        y += 1;

    for i in range(xM-4):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"*");
        x+=1;
    aux=int(len(hosp)); #Encuentra la mitad de la ventana para imprimir los datos del hospital
    aux=xM-aux;
    aux=aux//2;
    #Los imprime
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(aux+2,4)+hosp, end="");
    print(Fore.LIGHTBLACK_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(xM-len(dom)-1,5)+dom, end="");
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(2,27)+"->PoliProgramming®<-", end="");
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(2,28)+"->Becerra Gonzalez Diego Ivan<-", end="");
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(2,29)+"->Padilla Valdez Gustavo<-", end="");

#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu1(xM,yM):
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(hosp));
    cX=xM-cX;
    cX=cX//2;
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2,cY)+pac+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+1)+med+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+2)+hosp+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+3)+sal+"    ", end="");
#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu2(xM,yM):
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(hosp));
    cX=xM-cX;
    cX=cX//2;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY)+pac+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2,cY+1)+med+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+2)+hosp+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+3)+sal+"    ", end="");
#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu3(xM,yM):
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(hosp));
    cX=xM-cX;
    cX=cX//2;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY)+pac+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+1)+med+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2,cY+2)+hosp+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+3)+sal+"    ", end="");
#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu4(xM,yM):
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(hosp));
    cX=xM-cX;
    cX=cX//2;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY)+pac+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+1)+med+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2,cY+2)+hosp+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2,cY+3)+sal+" <--", end="");
    

def iniciar(): #Pide los datos para crear la ventana
    print("Antes de Iniciar, porfavor ingrese las medidas de la ventana");
    a=1;
    while a==1:
        xM=str(input("Dame la medida horizontal: "));
        try:
            xM=int(xM);
            if xM > 115 or xM < 50:
                print("El tamaño debe ser entre 50 y 115");
            else:
                a=2;
        except:
            print("Error!, ingrese numeros enteros");
    a=1;
    while a==1:
        yM=str(input("Dame la medida Vertical: "));
        try:
            yM=int(yM);
            if yM > 23 or yM < 12:
                print("El tamaño debe ser entre 11 y 23");
            else:
                a=2;
        except:
            print("Error!, ingrese numeros enteros");
    archivo = open("d03-p14-becerra-padilla-H.txt",mode = "r",encoding="utf-8"); #Abrira el archivo del hospital
    hosp=archivo.readline(); #Leera el nombre
    dom=archivo.readline(); #Leera la direccion
    hosp=str(hosp);
    dom=str(dom);
    archivo.close();
    menu(xM,yM,hosp,dom);

def paciente(xM,yM,hosp,dom):
    pass;

def medico(xM,yM,hosp,dom):
    pass;

def hospital(xM,yM,hosp,dom):
    pass;

def menu(xM,yM,hosp,dom): #Este sera el menu del hospital principal
    caracter=0;
    opcion=0;
    mover=0;
    ventana(xM,yM,hosp,dom);
    opmenu1(xM,yM);
    while True: #Leera todas las teclas que se presionen hasta que presione una valida
            aux=str(msvcrt.getch());  
            for i in aux: #Buscara en la tecla presionada
                if "H" in i and mover>0: #Si esta la H, significara que presiono la tecla de arriba(No afecta la H normal)
                    mover-=1;  
                elif "P" in i and mover<3:#Si esta la P, significara que presiono la tecla de arriba(No afecta la P normal)
                    mover+=1;                          
            if "r"==aux[3]: #Si presiona enter, elegira dependiendo la funcion que quiera y entrara
                if mover==0:
                    paciente(xM,yM,hosp,dom);
                elif mover==1:
                    medico(xM,yM,hosp,dom);
                elif mover==2:
                    hospital(xM,yM,hosp,dom);
                elif mover==3: #Si elige salir, hara un break del menu y acabara
                    break;
            else:
                pass;
            #Estos if dibujaran lo de adentro del menu dependiendo en que opcion se encuentre

            if mover==0:
                opmenu1(xM,yM);
            elif mover==1:
                opmenu2(xM,yM);
            elif mover==2:
                opmenu3(xM,yM);
            elif mover==3:
                opmenu4(xM,yM);

iniciar();