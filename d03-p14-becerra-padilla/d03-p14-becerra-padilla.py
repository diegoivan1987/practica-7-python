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
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=(118-xM)//2;
    y=(30-yM)//2;
    i=0;
    aux=0;
    while i <= xM:
        print(Cursor.POS(x,y)+Back.BLUE+" ");
        x += 1;
        i+=1;
    i=0;
    while i <= yM:
        print(Cursor.POS(x,y)+Back.BLUE+"  ");
        y += 1;
        i+=1;
    x=(118-xM)//2;
    y=(30-yM)//2;
    i=0;
    while i <= yM:
        print(Cursor.POS(x,y)+Back.BLUE+"  ");
        y += 1;
        i+=1;
    i=0;
    while i <= xM+2:
        print(Cursor.POS(x,y)+Back.BLUE+" ");
        x+=1;
        i+=1;
    #Los siguientes crearan el mini adornado tambien en el marco
    x=((118-xM)//2)+2;
    y=((30-yM)//2)+1;
    i=0;
    while i <= xM-4:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"*");
        x += 1;
        i+=1;
    i=0;
    while i <= yM-1:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"**");
        y += 1;  
        i+=1;

    x=((118-xM)//2)+2;
    y=((30-yM)//2)+1;
    i=0;
    while i <= yM-2:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"**");
        y += 1;
        i+=1;
    i=0;
    while i <= xM-4:
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+Fore.BLACK+"*");
        x+=1;
        i+=1;
    x=(118-xM)//2;
    y=(30-yM)//2;
    i=0;
    while i <= xM+3:
        print(Cursor.POS(x+2,y-1)+Back.LIGHTBLACK_EX+" ");
        x += 1;
        i+=1;
    x=x-1;
    i=0;
    while i <= yM-1:
        print(Cursor.POS(x,y)+Back.LIGHTBLACK_EX+"   ");
        y += 1;
        i+=1;
    

    x=(118-xM)//2;
    y=(30-yM)//2;
    archivo = open("d03-p14-becerra-padilla-H.txt",mode = "r",encoding="utf-8"); #Abrira el archivo del hospital
    hosp=archivo.readline(); #Leera el nombre
    dom=archivo.readline(); #Leera la direccion
    hosp=str(hosp);
    dom=str(dom);
    archivo.close();

    aux=int(len(hosp)); #Encuentra la mitad de la ventana para imprimir los datos del hospital
    aux=xM-aux;
    aux=aux//2;
    #Los imprime
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(aux+2+x,y+1)+hosp, end="");
    aux=int(len(seccion)); #Encuentra la mitad de la ventana para imprimir los datos del hospital
    aux=xM-aux;
    aux=aux//2;
    print(Fore.LIGHTYELLOW_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(aux+2+x,3+y)+seccion, end="");
    print(Fore.LIGHTBLACK_EX+Back.BLACK+Style.BRIGHT+Cursor.POS((xM-len(dom)-1)+x,2+y)+dom, end="");
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(2,29)+"->PoliProgramming®<-", end="");
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+Cursor.POS(2,30)+"->Becerra Gonzalez Diego Ivan y Padilla Valdez Gustavo<-", end="");

#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu1(x,y,xM,yM):
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
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2+x,cY+y)+pac+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+1)+med+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+2)+hosp+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+3)+sal+"    ", end="");
#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu2(x,y,xM,yM):
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
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y)+pac+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2+x,cY+y+1)+med+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+2)+hosp+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+3)+sal+"    ", end="");
#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu3(x,y,xM,yM):
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
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y)+pac+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+1)+med+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2+x,cY+y+2)+hosp+" <--", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+3)+sal+"    ", end="");
#Crea las diferencias de menu, dependiendo de donde se encuentre la opcion 
def opmenu4(x,y,xM,yM):
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
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y)+pac+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+1)+med+"    ", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+2)+hosp+"    ", end="");
    print(Fore.BLACK+Back.WHITE+Cursor.POS(cX+2+x,cY+y+3)+sal+" <--", end="");
    

def iniciar(): #Pide los datos para crear la ventana
    print("Antes de Iniciar, porfavor ingrese las medidas de la ventana");
    a=1;
    while a==1:
        xM=str(input("Dame la medida horizontal: "));
        try:
            xM=int(xM);
            if xM > 115 or xM < 60:
                print("El tamaño debe ser entre 60 y 105");
            else:
                a=2;
        except:
            print("Error!, ingrese numeros enteros");
    a=1;
    while a==1:
        yM=str(input("Dame la medida Vertical: "));
        try:
            yM=int(yM);
            if yM > 23 or yM < 14:
                print("El tamaño debe ser entre 14 y 23");
            else:
                a=2;
        except:
            print("Error!, ingrese numeros enteros");
    menu(xM,yM);

def paciente(x,y,xM,yM):
    pass;

def medico(x,y,xM,yM): #Funcion de cambios que tengan que ver con el medico
    seccion="Alta de Medico";
    ventana(xM,yM,seccion);
    nmed="1.-Añadir un nuevo medico";
    alta="2.-Dar de alta un paciente";
    analis="3.-Crear resultados de analisis";
    sal="4.-Salir";
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(alta));
    cX=xM-cX;
    cX=cX//2;
    y=y-1;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y)+nmed, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+1)+alta, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+2)+analis, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+3)+sal, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+5)+"Presione su opcion: ", end="");
    while True:
        aux=str(msvcrt.getch());
        if "b'1'" == aux:
            alta_med(x,y,xM,yM,cX,seccion);
            break;
        elif "b'2'" == aux:
            
            break;
        elif "b'3'" == aux:
            break;
        elif "b'4'" == aux:
            break;
        else:
            pass;

def alta_med(x,y,xM,yM,cX,seccion): #Funcion para dar de alta un nuevo medico
    ventana(xM,yM,seccion);
    er=1;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese el nombre del medico", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
    nom=str(input());
    while er==1: #While para verificar que la cedula no se repita
        cont=0;
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese su Cedula", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
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
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+10)+"Cedula ya existente, Verifiquela", end=""); 
                input();
                break;
            else:
                er=0;
    verificar.close();
    ventana(xM,yM,seccion);
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese el su especialidad", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
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
    

def hospital(x,y,xM,yM): #Funcion de cambios del hospital
    seccion="Cambios al Hospital";
    ventana(xM,yM,seccion);
    nom="1.-Modificar Nombre de Hospital";
    dire="2.-Modificar Direccion del Hospital";
    sal="3.-Salir";
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(nom));
    cX=xM-cX;
    cX=cX//2;
    y=y-1;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y)+nom, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+1)+dire, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+2)+sal, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+4)+"Presione su opcion: ", end="");
    while True:
        aux=str(msvcrt.getch());
        if "b'1'" == aux:
            nom_hos(x,y,xM,yM,cX,seccion);
            break;
        elif "b'2'" == aux:
            dire_hos(x,y,xM,yM,cX,seccion);
            break;
        elif "b'3'" == aux:
            break;
        else:
            pass;

def nom_hos(x,y,xM,yM,cX,seccion): #Funcion para cambiar el nombre del hospital
    ventana(xM,yM,seccion);
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese el nuevo nombre del hospital", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
    nom=str(input());
    nom=nom+"\n"; #Se añade un salto de lineas, para evitar que el texto se pegue
    reemplazar_linea("d03-p14-becerra-padilla-H.txt", 0,nom);

def dire_hos(x,y,xM,yM,cX,seccion): #Funcion para cambiar la direccion del hospital
    ventana(xM,yM,seccion);
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,7+y)+"Ingrese la nueva direccion del hospital", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,8+y)+"", end="");
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
    x=(118-xM)//2;
    y=(26-yM)//2;
    caracter=0;
    opcion=0;
    mover=0;
    dib=0;
    seccion="Menú Principal"
    ventana(xM,yM,seccion);
    opmenu1(x,y,xM,yM);
    
    while True: #Leera todas las teclas que se presionen hasta que presione una valida
            aux=str(msvcrt.getch());  
            for i in aux: #Buscara en la tecla presionada
                if "H" in i and mover>0: #Si esta la H, significara que presiono la tecla de arriba(No afecta la H normal)
                    mover-=1;  
                elif "P" in i and mover<3:#Si esta la P, significara que presiono la tecla de arriba(No afecta la P normal)
                    mover+=1;                          
            if "r"==aux[3]: #Si presiona enter, elegira dependiendo la funcion que quiera y entrara
                if mover==0:
                    paciente(x,y,xM,yM);
                    dib=1;
                elif mover==1:
                    medico(x,y,xM,yM);
                    dib=1;
                elif mover==2:
                    hospital(x,y,xM,yM);
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
                opmenu1(x,y,xM,yM);
            elif mover==1:
                opmenu2(x,y,xM,yM);
            elif mover==2:
                opmenu3(x,y,xM,yM);
            elif mover==3:
                opmenu4(x,y,xM,yM);

iniciar();