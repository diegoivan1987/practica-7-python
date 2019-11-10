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


def e2(errorcatch):#crea copias de un archivo, alterando su contenido
    #mientras no presione esc
    dibujoej(errorcatch,2);
    entrar = True;
    while entrar:#mientras no presione esc, sigue ejecutandose
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,6)+"Ingresa 1 para buscar un archivo o esc para salir: ",end="");
        tecla = str(msvcrt.getch());#capturamos la tecla
        if "1b" in tecla:#sale del while
            entrar = False;
        elif "b'1'" == tecla: #Lo mismo con b'1'
            errorcatch = buscar_archivo(errorcatch);#obtener nombre del archivo
        else:
            print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,6)+"Debes ingresar una opcion correcta: ",end="");
            sleep(1);
    return errorcatch; #Regresara el total de except al menu

def buscar_archivo(errorcatch):#busca un archivo
    dibujoej(errorcatch,2);
    print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,6)+"Ingresa el nombre del archivo: ",end="");
    nombre = str(input());
    while len(nombre) > 0:#si ingreso algo
        try:#tratar de abrir archivo
            archivo = open(nombre,mode = "r",encoding="utf-8");
            repeticiones = buscar_repeticiones(errorcatch,nombre)#si existe, contar el numero de archivos con el mismo nombre antes de ()
            copia_creada = crea_copia(errorcatch, nombre,repeticiones)#crear un nuevo archivo con mismo nombre terminacion (n)
            da_formato(errorcatch,copia_creada,repeticiones);#copiar el contenido del archivo (n-1), alternando las palabras en mayuscula y minuscula y cambiandolas de color
            input();
            #mostrar el nombre del archivo creado
        except:#si no existe, avisar y permitir ingresar un nombre que exista
            nombre = str(input(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,6)+"El archivo no existe, ingresa otro nombre: "));
            errorcatch += 1;
    if len(nombre) == 0:#si no ingreso nada
        print(Fore.WHITE+Style.BRIGHT+Cursor.POS(6,7)+"Debe ingresar el nombre del archivo");
        sleep(1);
    return errorcatch;

def buscar_repeticiones(errorcatch,nombre):#busca que tantas veces se ha repetido un archivo
    repeticiones = 0;#numero de repeticiones de un archivo
    sin_extension = "";#guardara el nombre del archivo sin extension
    for letra in nombre:#recorremos el nombre del archivo
        if (letra == "(") or (letra=="."):#si llega al parentesis o al punto, sale
            break;
        else :#si no, va guardando el nombre del archivo por letras
            sin_extension = sin_extension + letra;

    ruta = os.path.dirname(os.path.abspath(__file__));#Variable para la ruta al directorio
    
    lstDir = os.walk(ruta);  #Lista directorios y ficheros
    #recorrer la lista
    for root, dirs, files in lstDir:
        for fichero in files:#compara cada fichero
            (nombreFichero, extension) = os.path.splitext(fichero);#obtiene el nombre y extension de cada fichero
            nombreFichero_sin_par = "";#guardara el nombre del fichero evaluado sin parentesis
            for letra in nombreFichero:#recorremos el nombre del fichero evaluado
                if (letra == "("):#si llega al parentesis, sale
                    break;
                else :#si no, va guardando el nombre del archivo por letras
                    nombreFichero_sin_par = nombreFichero_sin_par + letra;
            if (nombreFichero_sin_par == sin_extension) and (extension == ".txt"):#si tienen el mismo nombe y extension
               repeticiones += 1;
    repeticiones = repeticiones - 1;#le restamos uno porque se cuenta el archivo original, el que no tiene parentesis
    return repeticiones;

def crea_copia(errorcatch, nombre,numero_copia):#crea una copia de un archivo existente, agregando el numero de copia al archivo
    sin_extension = "";#guardara el nombre del archivo sin extension
    numero_copia += 1;
    nombre_nuevo = "";#guardara el nuevo nombre del archivo
    for letra in nombre:#recorremos el nombre del archivo
        if (letra == "(") or (letra=="."):#si llega al parentesis o al punto, sale
            break;
        else :#si no, va guardando el nombre del archivo por letras
            sin_extension = sin_extension + letra;

    nombre_nuevo = sin_extension;
    nombre_nuevo = nombre_nuevo + "(";
    nombre_nuevo = nombre_nuevo + str(numero_copia);
    nombre_nuevo = nombre_nuevo + ").txt";
    nuevo = open(nombre_nuevo,mode = "w",encoding="utf-8");
    nuevo.close();

    return nombre_nuevo;

def da_formato(errorcatch, nombre,numero_copia):#da el formato de mayusculas y minusculas al contenido del archivo
    numero_copia += 1;
    nombre_anterior = "";#el es nombre del antecesos del archivo a modificar
    if numero_copia == 1:#si es la primer copia
        nombre_anterior = nombre.replace("(1)","");#se obtiene el nombre del archivo original
    else:#si es de la segunda copia en adelante
        aux = "("+str(numero_copia)+")";#guarda lo que esta entre parentesis de la copia a modificar
        aux2 = "("+str(numero_copia-1)+")";#guarda lo que esta entre parentesis del archivo anterior
        nombre_anterior = nombre.replace(aux,aux2);#se obtiene el nombre del archivo anterior
    archivo_a_leer = open(nombre_anterior,mode = "r",encoding="utf-8");
    archivo_a_modificar = open(nombre,mode = "w",encoding="utf-8");

    while True:#recorremos por lineas el archivo anterior
        linea = archivo_a_leer.readline();
        if not linea:#si ya no hay lineas se acaba
            break;
        else:
            palabras = linea.split();#dividimos la linea en palabras

        nueva_linea = [];#modificacion de la linea leida
        
        bandera = False;
        for palabra in palabras:#recorremos la linea
            if numero_copia%2 != 0:#si es una copia impar, convierte la linea a mayuscula minuscula
                
                if bandera == False:
                    palabra = palabra.upper();
                    bandera = True;
                elif bandera == True:
                    palabra = palabra.lower();
                    bandera = False;
            elif numero_copia%2 == 0:#si es una copia par, convierte la linea a  minuscula mayuscula
                
                if bandera == True:
                    palabra = palabra.upper();
                    bandera = False;
                elif bandera == False:
                    palabra = palabra.lower();
                    bandera = True;
                
            nueva_linea.append(palabra);#se añade cada palabra a la linea

        insertar = "";#lo que se insertara en la nueva copia
        for palabra in nueva_linea:#se forma de nuevo la linea
            insertar = insertar + palabra + " ";
        insertar = insertar[:-1];
        archivo_a_modificar.write(insertar);#se inserta en el documento
    #se cierran los dos documentos
    archivo_a_leer.close();
    archivo_a_modificar.close();



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