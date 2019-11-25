#practica 14
#becerra gonzalez diego ivan
#padilla valdez gustavo

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
from time import sleep; #Llama la funcion para pausar
from datetime import datetime; #Funcion para obtener la fecha
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

def paciente(x,y,xM,yM,numero):#funcion que tiene que ver con los cambios del paciente
    seccion="Alta de paciente";
    ventana(xM,yM,seccion);
    regi="1.-Registrar un paciente";
    resul="2.-Ver resultados de un paciente";
    sal="3.-Salir";
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(regi));
    cX=xM-cX;
    cX=cX//2;
    y=y-1;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,cY+y)+regi, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,cY+y+1)+resul, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,cY+y+2)+sal, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,cY+y+4)+"Presione su opcion: ", end="");
    while True:
        aux=str(msvcrt.getch());
        if "b'1'" == aux:
            numero=alta_pac(x,y,cX,xM,yM,numero);
            break;
        elif "b'2'" == aux:
            ver_resultados(x,y,cX,xM,yM);
            break;
        elif "b'3'" == aux:
            break;
        else:
            pass;
    return numero;

def alta_pac(x,y,cX,xM,yM,numero):#funcion para registrar un nuevo paciente
    seccion = "Registro de paciente";
    ventana(xM,yM,seccion);
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese el nombre del paciente", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
    nom=str(input());
    er=1;
    er=1;
    while er==1: #While para verificar que la edad es un numero
        seccion = "Registro de paciente";
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese la edad del paciente", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
        edad=str(input());
        try:#si es numero
            edad = int(edad);
            if edad < 0 or edad > 110:
                ventana(xM,yM,seccion);
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Edad Imposible! Ingrese de nuevo", end="");
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
                input();
                er=1;
            else:
                er = 0;
        except:#si no
            ventana(xM,yM,seccion);
            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Debe ingresar un numero", end="");
            er =1;
            sleep(2);
    
    #se ingresa la especialidad a la que acudio
    ventana(xM,yM,seccion);
    aux = len("Elija la especialidad a la que acudió:");
    abrir=open("d03-p14-becerra-padilla-H.txt", mode = "r",encoding="utf-8");
    linea=abrir.readline();
    linea=abrir.readline();
    linea=abrir.readline();
    linea=linea.split(",");
    abrir.close();
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Elija la especialidad a la que acudió:", end="");
    cont=1;
    for i in linea:
        aux=str(cont)+".-"+str(i);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7+cont)+aux, end="");
        cont+=1;
    
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+13)+"", end="");
    while True:
        op=str(msvcrt.getch());
        if "b'1'" == op:
            esp = "Alergologo";
            doctor=elegir_med(x,y,cX,xM,yM,esp,numero);
            break;
        elif "b'2'" == op:
            esp = "Odontologia";
            doctor=elegir_med(x,y,cX,xM,yM,esp,numero);
            break;
        elif "b'3'" == op:
            esp = "Oftalmologia";
            doctor=elegir_med(x,y,cX,xM,yM,esp,numero);
            break;
        elif "b'4'" == op:
            esp = "Cardiologia";
            doctor=elegir_med(x,y,cX,xM,yM,esp,numero);
            break;
        elif "b'5'" == op:
            esp = "Cirugia";
            doctor=elegir_med(x,y,cX,xM,yM,esp,numero);
            break;
        else:
            pass;
    if doctor == "NOHAYDOCTOR":
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"No se hizo el registro", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
        input();
    else:
        #Agrega los datos del nuevo paciente al documento
        now = datetime.now();
        fecha=str(now.day)+"/"+str(now.month)+"/"+str(now.year)+ "\n";
        nom = nom + "\n";
        aux = str(numero)+ "\n";
        edad = str(edad)+ "\n";
        alta="NO"+"\n";
        analisis = "Sin ingresar aun \n"
        esp = esp + "\n";
        archivo=open("d03-p14-becerra-padilla-P.txt", mode = "a",encoding="utf-8");
        archivo.write(nom);
        archivo.write(doctor);
        archivo.write(esp);
        archivo.write(edad);
        archivo.write(analisis);
        archivo.write(fecha);
        archivo.write(alta);
        archivo.write(aux);
        archivo.close();
        
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Tu numero de paciente es: ",numero, end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
        input();
        numero=numero+1;
    return numero;

def elegir_med(x,y,cX,xM,yM,esp,numero):
    seccion = "Elegir medico";
    sal=0;
    aux="";
    regreso="NOHAYDOCTOR";
    abrir=open("d03-p14-becerra-padilla-M.txt", mode = "r",encoding="utf-8");
    cont=0;
    agregar=0;
    while(True):
        agregar+=1;
        linea=abrir.readline();
        if not linea:
            aux="NOHAYDOCTOR";
            break;
        elif linea == (esp+"\n"):
            ventana(xM,yM,seccion);
            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"Presione 1 Si quiere a este Medico", end="");
            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"Presione 2 en otro caso", end="");
            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+10)+"Cedula del Medico: "+aux, end="");
            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+11)+" ", end="");
            while(True):
                car=str(msvcrt.getch());
                if "b'1'" == car:
                    sal=1;
                    break;
                elif "b'2'" == car:
                    sal=0;
                    break;
                else:
                    pass;
            cont+=1;
        if sal==1:
            break;
        aux=linea;
    abrir.close();
    if cont != 0 and aux!="NOHAYDOCTOR":
        numero=str(numero);
        numero=numero+",";
        agregar_linea("d03-p14-becerra-padilla-M.txt",agregar,numero);
        regreso=aux;
    else:
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"No eligio doctor, vuelva a ingresar", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"", end="");
        input();
        regreso=aux;    
    if cont == 0:
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"No disponibles, Vaya a otro hospital", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"", end="");
        input();
        sal=1;
    return regreso;

def ver_resultados(x,y,cX,xM,yM):#muestra los resultados de un paciente
    seccion = "Resultados de analisis";
    er=1;
    lugar=0;
    while er==1: #While para verificar que el numero no se repita
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"Ingrese el numero del paciente", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"", end="");
        numero=str(input());
        verificar=open("d03-p14-becerra-padilla-P.txt", mode = "r",encoding="utf-8");
        cont=0;
        while(True): #Abrira el archivo y buscara el numero
            cont+=1;
            linea=verificar.readline();
            linea=str(linea);
            if not linea:#si llego al final sin encontrar el numero de paciente
                er=0;
                ventana(xM,yM,seccion);
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"No existe el paciente", end="");
                input();
                er=1;
                break;
                
            elif linea == (numero+"\n"):
                er=0;
                lugar=cont;
                break;
            else:
                er=0;
    cont=0;
    verificar=open("d03-p14-becerra-padilla-P.txt", mode = "r",encoding="utf-8");
    while(True):
        linea=verificar.readline();
        cont+=1;
        if cont==lugar-7:
            nombre = linea;
            doctor = verificar.readline();
            servicio = verificar.readline();
            edad = verificar.readline();
            resultados = verificar.readline();
            fecha=verificar.readline();
            alta=verificar.readline();
            lugar=verificar.readline();
            break;
        
            
    verificar.close();
    ventana(xM,yM,seccion);
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Nombre: "+nombre, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"Edad: "+edad, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"Servicio usado: "+servicio, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+10)+"Fecha: "+fecha, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+11)+"Alta: "+alta, end=""); 
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+12)+"Doctor(Cedula): "+doctor, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+13)+"Resultados: "+resultados, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+14)+"", end="");
    input();
    
            

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
            dar_alta(x,y,xM,yM,cX);
            break;
        elif "b'3'" == aux:
            crea_resultados(x,y,xM,yM,cX);
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
    #se ingresa la especialidad
    ventana(xM,yM,seccion);
    abrir=open("d03-p14-becerra-padilla-H.txt", mode = "r",encoding="utf-8");
    linea=abrir.readline();
    linea=abrir.readline();
    linea=abrir.readline();
    linea=linea.split(",");
    abrir.close();
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Elija una especialidad:", end="");
    cont=1;
    for i in linea:
        aux=str(cont)+".-"+str(i);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7+cont)+aux, end="");
        cont+=1;
    
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+13)+"", end="");
    while True:
        op=str(msvcrt.getch());
        if "b'1'" == op:
            esp = "Alergologo";
            break;
        elif "b'2'" == op:
            esp = "Odontologia";
            break;
        elif "b'3'" == op:
            esp = "Oftalmologia";
            break;
        elif "b'4'" == op:
            esp = "Cardiologia";
            break;
        elif "b'5'" == op:
            esp = "Cirugia";
            break;
        else:
            pass;
    vacio=open("d03-p14-becerra-padilla-M.txt", mode = "r",encoding="utf-8");
    nada=vacio.readline();
    vacio.close();
    if not nada:
        nom=nom+"\n";
    else:
        nom="\n"+nom+"\n";
    ced=ced+"\n";
    esp=esp+"\n"+",";
    #Agrega los datos del nuevo medico al documento
    archivo=open("d03-p14-becerra-padilla-M.txt", mode = "a",encoding="utf-8");
    archivo.write(nom);
    archivo.write(ced);
    archivo.write(esp);
    archivo.close();
    ventana(xM,yM,seccion);
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x+4,y+7)+"Registrado Con Exito!", end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x+4,y+8)+"", end="");
    input();

def dar_alta(x,y,xM,yM,cX):
    seccion = "Dar de alta";
    er=1;
    while er==1: #While para verificar que el numero no se repita
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese su cedula", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
        cedula=str(input());
        verificar_cedula=open("d03-p14-becerra-padilla-M.txt", mode = "r",encoding="utf-8");
        while(True): #Abrira el archivo y verificara que exista la cedula
            linea=verificar_cedula.readline();
            linea=str(linea);
            if not linea:#si llego al final sin encontrar la cedula
                er=0;
                ventana(xM,yM,seccion);
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Cedula no encontrada, no puede continuar", end="");
                input();
                break;
            elif linea == (cedula+"\n"):
                #aqui se busca el paciente
                elegir_pac=verificar_cedula.readline();
                elegir_pac=verificar_cedula.readline();
                elegir_pac=elegir_pac.split(",");
                elegir_pac.remove("");
                elegir_pac.remove("\n");
                ventana(xM,yM,seccion);
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Pacientes asignados:", end="");
                contador = 8;
                for numero in elegir_pac:
                    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+contador)+numero, end="");
                    contador +=1;
                contador +=1;
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+contador)+"Ingresar el numero del paciente:", end="");
                numero_que_editara = str(input());
                er2=1;
                buscar=0;
                for p in elegir_pac:
                    if numero_que_editara==p:
                        er2=0;
                        ver_pac=open("d03-p14-becerra-padilla-P.txt", mode = "r",encoding="utf-8");
                        al_n="SI\n";
                        ayuda="";
                        exito=0;
                        while(True):
                            buscar+=1;
                            o=ver_pac.readline();
                            if not o:
                                exito=0;
                                break;
                            elif buscar%8==0 and o == (numero_que_editara+"\n") and ayuda == "NO\n":
                                ver_res=open("d03-p14-becerra-padilla-P.txt", mode = "r",encoding="utf-8");
                                resul="";
                                for h in range(buscar-3):
                                    resul=ver_res.readline();
                                print(resul);
                                input();
                                if "Sin ingresar aun" in resul:
                                    exito=0;
                                else:
                                    exito=1;
                                ver_res.close();
                                break;
                            ayuda=o;
                       
                        ver_pac.close();
                        ventana(xM,yM,seccion);
                        if exito==1:
                            reemplazar_linea("d03-p14-becerra-padilla-P.txt",buscar-2,al_n);
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"       Alta con exito!", end="");
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
                        elif exito==0:
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Paciente ya esta dado de alta", end="");
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"O aun no se le entregan resultados", end="");
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"", end="");
                        input();

                if er2==1:
                    ventana(xM,yM,seccion);
                    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Paciente no encontrado", end="");
                    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
                    input();
                    
                    
                break;
            else:
                er=0;

        verificar_cedula.close();

def crea_resultados(x,y,xM,yM,cX):#permite al medico guardar los analisis de un paciente
    seccion = "Guardad resultados de analisis";
    er=1;
    while er==1: #While para verificar que el numero no se repita
        ventana(xM,yM,seccion);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Ingrese su cedula", end="");
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
        cedula=str(input());
        verificar_cedula=open("d03-p14-becerra-padilla-M.txt", mode = "r",encoding="utf-8");
        while(True): #Abrira el archivo y verificara que exista la cedula
            linea=verificar_cedula.readline();
            linea=str(linea);
            if not linea:#si llego al final sin encontrar la cedula
                er=0;
                ventana(xM,yM,seccion);
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Cedula no encontrada, no puede continuar", end="");
                input();
                break;
            elif linea == (cedula+"\n"):
                #aqui se busca el paciente
                elegir_pac=verificar_cedula.readline();
                elegir_pac=verificar_cedula.readline();
                elegir_pac=elegir_pac.split(",");
                elegir_pac.remove("");
                elegir_pac.remove("\n");
                ventana(xM,yM,seccion);
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Pacientes asignados:", end="");
                contador = 8;
                for numero in elegir_pac:
                    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+contador)+numero, end="");
                    contador +=1;
                contador +=1;
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+contador)+"Ingresar el numero del paciente:", end="");
                numero_que_editara = str(input());
                er2=1;
                buscar=0;
                for p in elegir_pac:
                    if numero_que_editara==p:
                        er2=0;
                        ver_pac=open("d03-p14-becerra-padilla-P.txt", mode = "r",encoding="utf-8");
                        ventana(xM,yM,seccion);
                        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Escriba los resultados", end="");
                        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x-8,y+8)+"", end="");
                        nuevos_r=str(input());
                        nuevos_r=nuevos_r+"\n";
                        ayuda="";
                        exito=0;
                        while(True):
                            buscar+=1;
                            o=ver_pac.readline();
                            if not o:
                                exito=0;
                                break;
                            elif buscar%8==0 and o == (numero_que_editara+"\n") and ayuda == "NO\n":
                                exito=1;
                                break;
                            ayuda=o;
                       
                        ver_pac.close();
                        ventana(xM,yM,seccion);
                        if exito==1:
                            reemplazar_linea("d03-p14-becerra-padilla-P.txt",buscar-4,nuevos_r);
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Resultados Nuevos Ingresados!", end="");
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
                        elif exito==0:
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Paciente ya esta dado de alta", end="");
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"No se ingreso nada", end="");
                            print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+9)+"", end="");
                        input();

                if er2==1:
                    ventana(xM,yM,seccion);
                    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+7)+"Paciente no encontrado", end="");
                    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"", end="");
                    input();
                    
                    
                break;
            else:
                er=0;

        verificar_cedula.close();

def hospital(x,y,xM,yM): #Funcion de cambios del hospital
    seccion="Cambios al Hospital";
    ventana(xM,yM,seccion);
    nom="1.-Modificar Nombre de Hospital";
    dire="2.-Modificar Direccion del Hospital";
    ser = "3.-Mostrar servicios";
    sal="4.-Salir";
    #Los cY y cX son para encontrar el centro de la pantalla dependiendo y colocar cada linea donde es
    cY=yM+2;
    cY=cY//2;
    cX=int(len(nom));
    cX=xM-cX;
    cX=cX//2;
    y=y-1;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y)+nom, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+1)+dire, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+2)+ser, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+3)+sal, end="");
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+2+x,cY+y+5)+"Presione su opcion: ", end="");
    while True:
        aux=str(msvcrt.getch());
        if "b'1'" == aux:
            nom_hos(x,y,xM,yM,cX,seccion);
            break;
        elif "b'2'" == aux:
            dire_hos(x,y,xM,yM,cX,seccion);
            break;
        elif "b'3'" == aux:
            ser_hos(x,y,xM,yM,cX,seccion);
            break;
        elif "b'4'" == aux:
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

def agregar_linea(archivo, linea, texto): #Funcion para agregar en una linea especifica en un txt
    lines = open(archivo, 'r').readlines();
    aux= lines[linea];
    if aux==",":
        pass;
    else:
        aux=aux[:-1];
    lines[linea] = aux+texto+"\n";
    out = open(archivo, 'w');
    out.writelines(lines);
    out.close();

def ser_hos(x,y,xM,yM,cX,seccion):#muestra los servicios del hospital
    ventana(xM,yM,seccion);
    cX=int(len(" Servicios: "));
    cX=xM-cX;
    cX=cX//2;
    abrir=open("d03-p14-becerra-padilla-H.txt", mode = "r",encoding="utf-8");
    linea=abrir.readline();
    linea=abrir.readline();
    linea=abrir.readline();
    linea=linea.split(",");
    abrir.close();
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8)+"Servicios:", end="");
    cont=1;
    for i in linea:
        aux=str(cont)+".-"+str(i);
        print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+8+cont)+aux, end="");
        cont+=1;
    print(Fore.WHITE+Back.BLACK+Style.BRIGHT+Cursor.POS(cX+x,y+14)+"", end="");
    input();


def menu(xM,yM): #Este sera el menu del hospital principal
    x=(118-xM)//2;
    y=(26-yM)//2;
    caracter=0;
    opcion=0;
    mover=0;
    dib=0;
    aux=" ";
    #Este while buscara en que numero se quedo el ultimo paciente
    archivo= open("d03-p14-becerra-padilla-P.txt",mode="r",encoding="utf-8");
    while(True):
        linea=str(archivo.readline());#Lee por linea los caracteres
        if not linea: #Si ya no hay lineas
            break;
        aux=linea;
    archivo.close();
    if aux==" ":
        aux="0";
    numero=int(aux);
    numero=numero+1;
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
                    numero=paciente(x,y,xM,yM,numero);
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