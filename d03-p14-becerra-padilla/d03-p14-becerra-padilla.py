#practica 14
#becerra gonzalez diego ivan
#padilla valdez gustavo

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
from time import sleep; #Llama la funcion para pausar
import os; #Llamo funciones del sistema operativo para poder borrar pantalla
import msvcrt; #Llama funcion para poder leer lo que se presiona en el teclado
init(autoreset=True); #Se inicia el colorama, que se autoresetee para evitar basura en la consola

def ventana(xM,yM,seccion): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 while sera para hacer el marco de la ventana
    
    aux=0;
    
    x=(120-xM)//2;
    y=(30-yM)-1;

    limiteX = x + xM;
    limiteY = y +yM;

    while x <= limiteX:
        print(Cursor.POS(x,y)+Back.BLUE+" ");
        x += 1;
    
    while y <= limiteY:
        print(Cursor.POS(x,y)+Back.BLUE+"  ");
        y += 1;

    x=(120-xM)//2;
    y=(30-yM)-1;
    while y <= limiteY-1:
        print(Cursor.POS(x,y)+Back.BLUE+"  ");
        y += 1;

    while x <= limiteX:
        print(Cursor.POS(x,y)+Back.BLUE+" ",end="");
        x += 1;

    #Los siguientes crearan el mini adornado tambien en el marco
    x=(120-xM)//2+2;
    y=(30-yM);

    while x <= limiteX-2:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"*");
        x += 1;
    
    while y <= limiteY-1:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"**");
        y += 1;

    x=(120-xM)//2+2;
    y=(30-yM);
    while y <= limiteY-2:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"**");
        y += 1;

    while x <= limiteX-2:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"*",end="");
        x += 1;

    #Estos for crean la "sombra" de la ventana
    x=(120-xM)//2+2;
    y=(30-yM)-2;
    while x <= limiteX+3:
        print(Cursor.POS(x,y)+Back.LIGHTBLACK_EX+" ");
        x += 1;   
    
    while y <= limiteY-1:
        print(Cursor.POS(x-1,y)+Back.LIGHTBLACK_EX+" ");
        print(Cursor.POS(x,y)+Back.LIGHTBLACK_EX+" ");
        y += 1;
    
    archivo = open("d03-p14-becerra-padilla-H.txt",mode = "r",encoding="utf-8"); #Abrira el archivo del hospital
    hosp=archivo.readline(); #Leera el nombre
    dom=archivo.readline(); #Leera la direccion
    hosp=str(hosp);
    dom=str(dom);
    archivo.close();

    centro_ventana = limiteX //2;
    y=(30-yM);

    aux=int(len(seccion)); #Encuentra la mitad de la ventana para imprimir la seccion
    aux=aux//2;
    print(Fore.LIGHTYELLOW_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(centro_ventana-aux,y)+seccion, end="");

    aux=int(len(hosp)); #Encuentra la mitad de la ventana para imprimir los datos del hospital
    aux=aux//2;
    #Los imprime
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(centro_ventana-aux,y+1)+hosp, end="");
    print(Fore.LIGHTBLACK_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(centro_ventana-aux,y+2)+dom, end="");

    x=(120-xM)//2;
    limiteY = y +yM;
    
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(x+4,limiteY-3)+"->Padilla Valdez Gustavo, Becerra Gonzalez Diego Ivan, PoliProgramming®<-", end="");

#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu1(xM,yM):
    x=(120-xM)//2+4;
    y=(30-yM)+2;
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=(y+yM)//2;
    cX=(x+xM)//2;
    aux = len(hosp)//2;
    cX = cX - aux;
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX,cY)+pac+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+1)+med+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+2)+hosp+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+3)+sal+"    ", end="");

#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu2(xM,yM):
    x=(120-xM)//2+4;
    y=(30-yM)+2;
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=(y+yM)//2;
    cX=(x+xM)//2;
    aux = len(hosp)//2;
    cX = cX - aux;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY)+pac+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX,cY+1)+med+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+2)+hosp+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+3)+sal+"    ", end="");

#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu3(xM,yM):
    x=(120-xM)//2+4;
    y=(30-yM)+2;
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=(y+yM)//2;
    cX=(x+xM)//2;
    aux = len(hosp)//2;
    cX = cX - aux;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY)+pac+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+1)+med+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX,cY+2)+hosp+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+3)+sal+"    ", end="");

#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu4(xM,yM):
    x=(120-xM)//2+4;
    y=(30-yM)+2;
    pac="1.-Alta de Pacientes"
    med="2.-Alta de Medicos"
    hosp="3.-Alta de datos de Hospital"
    sal="4.-Salir"
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=(y+yM)//2;
    cX=(x+xM)//2;
    aux = len(hosp)//2;
    cX = cX - aux;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY)+pac+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+1)+med+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+2)+hosp+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX,cY+3)+sal+" <--", end="");
    

def iniciar(): #Pide los datos para crear la ventana
    print("Antes de Iniciar, porfavor ingrese las medidas de la ventana");
    a=1;
    while a==1:
        xM=str(input("Dame la medida horizontal: "));
        try:
            xM=int(xM);
            if xM < 0 or xM > 108:
                print("El tamaño debe ser entre 0 y 108");
            else:
                a=2;
        except:
            print("Error!, ingrese numeros enteros");
    a=1;
    while a==1:
        yM=str(input("Dame la medida Vertical: "));
        try:
            yM=int(yM);
            if yM < 0 or yM > 27:
                print("El tamaño debe ser entre 0 y 27");
            else:
                a=2;
        except:
            print("Error!, ingrese numeros enteros");
    menu(xM,yM);

def paciente(xM,yM):
    pass;

def medico(xM,yM): #Funcion de cambios que tengan que ver con el medico
    seccion="Alta de Medico";
    ventana(xM,yM,seccion);
    x=(120-xM)//2+4;
    y=(30-yM)+2;
    nmed="1.-Añadir un nuevo medico";
    alta="2.-Dar de alta un paciente";
    analis="3.-Crear resultados de analisis";
    sal="4.-Salir";
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=(y+yM)//2;
    cX=(x+xM)//2;
    aux = len(analis)//2;
    cX = cX - aux;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY)+nmed, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+1)+alta, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+2)+analis, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+3)+sal, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+5)+"Presione su opcion: ", end="");
    while True:
        aux=str(msvcrt.getch());
        if "b'1'" == aux:
            alta_med(xM,yM,cX,seccion);
            break;
        elif "b'2'" == aux:
            
            break;
        elif "b'3'" == aux:
            break;
        elif "b'4'" == aux:
            break;
        else:
            pass;

def alta_med(xM,yM,cX,seccion): #Funcion para dar de alta un nuevo medico
    ventana(xM,yM,seccion);
    x=(120-xM)//2+4;
    y=(30-yM)+5;
    er=1;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y)+"Ingrese el nombre del medico", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y+1)+"", end="");
    nom=str(input());
    while er==1: #While para verificar que la cedula no se repita
        cont=0;
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y)+"Ingrese su Cedula", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y+1)+"", end="");
        ced=str(input());
        verificar=open("d03-p14-becerra-padilla-M.txt", mode = "r",encoding="utf-8");
        while(True): #Abrira el archivo y verificara que la cedula no coincida con otra
            cont+=1;
            linea=verificar.readline();
            linea=str(linea);
            linea=linea.split();
            if not linea:
                er=0;
                break;
            elif linea[0]==ced and cont % 2 == 0:
                er=1;
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y+2)+"Cedula ya existente, Verifiquela", end=""); 
                input();
                break;
            else:
                er=0;
    verificar.close();
    ventana(xM,yM,seccion);
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y)+"Ingrese el su especialidad", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y+1)+"", end="");
    esp=str(input());
    #Ahora verificara para poner en servicios del hospital, la especialidad del doctor
    verificar=open("d03-p14-becerra-padilla-H.txt", mode = "r",encoding="utf-8");
    er=0;
    linea=verificar.readline();
    linea=verificar.readline();
    linea=verificar.readline();
    linea=linea.split(",");
    verificar.close();
    for i in linea:
        if i == esp: #Si ya esta su especialidad, no la agrega
            er=1;
        else:
            pass;
    aux=esp+",";
    if er==0: #Si es nueva, lo abre y lo agrega
        archivo=open("d03-p14-becerra-padilla-H.txt", mode = "a",encoding="utf-8");
        archivo.write(aux);
        archivo.close();
    nom=nom+"\n";
    ced=ced+"\n";
    esp=esp+"\n"+","+"\n";
    #Agrega los datos del nuevo medico al documento
    archivo=open("d03-p14-becerra-padilla-M.txt", mode = "a",encoding="utf-8");
    archivo.write(nom);
    archivo.write(ced);
    archivo.write(esp);
    archivo.close();
    

def hospital(xM,yM): #Funcion de cambios del hospital
    seccion="Cambios al Hospital";
    ventana(xM,yM,seccion);
    x=(120-xM)//2+4;
    y=(30-yM)+5;
    nom="1.-Modificar Nombre de Hospital";
    dire="2.-Modificar Direccion del Hospital";
    sal="3.-Salir";
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=(y+yM)//2;
    cX=(x+xM)//2;
    aux = len(nom)//2;
    cX = cX - aux;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY)+nom, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+1)+dire, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+2)+sal, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX,cY+4)+"Presione su opcion: ", end="");
    while True:
        aux=str(msvcrt.getch());
        if "b'1'" == aux:
            nom_hos(xM,yM,cX,seccion);
            break;
        elif "b'2'" == aux:
            dire_hos(xM,yM,cX,seccion);
            break;
        elif "b'3'" == aux:
            break;
        else:
            pass;

def nom_hos(xM,yM,cX,seccion): #Funcion para cambiar el nombre del hospital
    ventana(xM,yM,seccion);
    x=(120-xM)//2+4;
    y=(30-yM)+5;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y)+"Ingrese el nuevo nombre del hospital", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y+1)+"", end="");
    nom=str(input());
    nom=nom+"\n"; #Se añade un salto de lineas, para evitar que el texto se pegue
    reemplazar_linea("d03-p14-becerra-padilla-H.txt", 0,nom);

def dire_hos(xM,yM,cX,seccion): #Funcion para cambiar la direccion del hospital
    ventana(xM,yM,seccion);
    x=(120-xM)//2+4;
    y=(30-yM)+5;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y)+"Ingrese la nueva direccion del hospital", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(x,y+1)+"", end="");
    nom=str(input());
    nom=nom+"\n"; #Se añade un salto de lineas, para evitar que el texto se pegue
    reemplazar_linea("d03-p14-becerra-padilla-H.txt", 1,nom);

def reemplazar_linea(archivo, linea, texto): #Funcion para reemplazar una linea especifica en un txt
    lines = open(archivo, 'r').readlines();
    lines[linea] = texto;
    out = open(archivo, 'w');
    out.writelines(lines);
    out.close();


def menu(xM,yM): #Este sera el menu del hospital principal
    caracter=0;
    opcion=0;
    mover=0;
    dib=0;
    seccion="Menú Principal"
    ventana(xM,yM,seccion);
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
                    paciente(xM,yM);
                    dib=1;
                elif mover==1:
                    medico(xM,yM);
                    dib=1;
                elif mover==2:
                    hospital(xM,yM);
                    dib=1;
                elif mover==3: #Si elige salir, hara un break del menu y acabara
                    break;
            else:
                pass;
            #Estos if dibujaran lo de adentro del menu dependiendo en que opcion se encuentre
            if dib==1:
                ventana(xM,yM,seccion);
                dib=0;
            if mover==0:
                opmenu1(xM,yM);
            elif mover==1:
                opmenu2(xM,yM);
            elif mover==2:
                opmenu3(xM,yM);
            elif mover==3:
                opmenu4(xM,yM);

iniciar();