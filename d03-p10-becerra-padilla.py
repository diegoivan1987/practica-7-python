#practica 10
#becerra gonzalez diego ivan
#padilla valdez gustavo

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
from time import sleep; #Llama la funcion para pausar
import os; #Llamo funciones del sistema operativo para poder borrar pantalla
init(autoreset=True); #Se inicia el colorama, que se autoresetee para evitar basura en la consola

def dibujo(errorcatch): #Esta funcion creara la ventana siempre que se necesite con colores
    os.system("cls"); #Borrara la ventana
    #Los siguiente 4 for sera para hacer el marco de la ventana
    x=1;
    y=3;
    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
        x += 1;
    for i in range(11):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+"   ");
        y += 1;
    x=1;
    y=3;
    for i in range(10):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+"  ");
        y += 1;

    for i in range(80):
        print(Cursor.POS(x,y)+Back.LIGHTBLUE_EX+" ");
        x+=1;
    #Este for sera para rellenar la ventana
    x=3;
    y=4;
    for i in range(9):
        for i2 in range (79):
            print(Cursor.POS(x,y)+Back.WHITE+" ");
            x += 1;
        x=3;
        y+=1;
    #En la esquina mandara a imprimir los errores con parametros
    if errorcatch == -1: 
        pass;
    else:
        errorcatch=str(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,12)+Back.LIGHTRED_EX+Style.DIM+"Errores Except: "+errorcatch, end="");
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"", end="");
    
def estacionamiento(errorcatch): #Se hara una funcion que calcule el costo del estacionamiento
    aumento=[0]; #Inicializa las variables
    entrada=-1;
    salida=-1;
    pago=0;
    for i in aumento:
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese la hora de entrada: ", end="");
        entrada=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try:
            entrada=int(entrada);
            if entrada < 0 or entrada > 2399: #Si la hora no esta dentro del rango la volver a pedir
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingrese una hora correcta en formato militar!", end="");
                aumento.append(0);
                sleep(1);
            else:
                aux=str(entrada);
                if entrada > 9: #Si la hora tiene 2 o mas digitos
                    #Comparara que el penultimo digito no sea 6,7,8 o 9, para que entre en el rango del horario
                    if aux[-2] == "6" or aux[-2] == "7" or aux[-2] == "8" or aux[-2] == "9": 
                        dibujo(errorcatch);
                        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Error con los minutos ingresados!", end="");
                        aumento.append(0);
                        sleep(1);
                    else:
                        pass;
                else:
                    pass;

        except: #Si ingresa caracteres
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese numeros!", end="");
            aumento.append(0);
            sleep(1);

    aumento=[0];
    for i in aumento:
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese la hora de salida: ", end="");
        salida=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try:
            salida=int(salida);
            if salida <= entrada or salida > 2399:#Si la hora no esta dentro del rango la volver a pedir
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingrese una hora correcta en formato militar!", end="");
                aumento.append(0);
                sleep(1);
            else:
                aux=str(salida);
                if salida > 9:#Si la hora tiene 2 o mas digitos
                    #Comparara que el penultimo digito no sea 6,7,8 o 9, para que entre en el rango del horario
                    if aux[-2] == "6" or aux[-2] == "7" or aux[-2] == "8" or aux[-2] == "9":
                        dibujo(errorcatch);
                        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Error con los minutos ingresados!", end="");
                        aumento.append(0);
                        sleep(1);
                    else:
                        pass;
                else:
                    pass;

        except: #Si ingresa caracteres
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese numeros!", end="");
            aumento.append(0);
            sleep(1);

    total=salida-entrada; #Sacara el total que estuvo estacionado
    horas=total/100; #Sacara las horas, diviendolas entre 100
    if horas % 1 != 0: #Si existe punto decimal en las horas
        pago+=1000; #Se añadira el dinero de la primera hora
        aux=horas % 1;
        horas -= aux; #Se le restara el decimal a las horas, para que ya quede entero
        if horas == 0: #Si ya no hay mas horas no hace nada
            pass;
        else:
            pago= pago + (horas*600); #Si hay mas horas, este multiplica las restantes y las suma
    else: #Si no hay punto decimal
        pago+=1000; #El pago de la primera hora y la resta
        horas-=1;
        pago= pago + (horas*600); #Añadira lo de la primera hora y las demas horas

    dibujo(errorcatch);
    aux=str(pago);
    #Mandara a imprimir el total a pagar y para mejor comprension tambien las horas
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,4)+"Su total a pagar es de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    print(Fore.BLACK+Back.WHITE+" $ por ", end="");
    horas+=1;
    aux=str(horas);
    print(Fore.BLACK+Back.WHITE+aux, end="");
    print(Fore.BLACK+Back.WHITE+" horas.", end="");
    return(errorcatch); #Regresara el total de except al ejercicio
        

def e1(errorcatch):
    errorcatch=estacionamiento(errorcatch);
    print(Fore.BLACK+Back.LIGHTMAGENTA_EX+Cursor.POS(3,6)+"Ejercicio 1", end="");
    input(Fore.BLACK+Cursor.POS(3,7)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def caja(errorcatch):#programa de caja registradora para n productos
    Sub_total = 0;#declaracion de variables
    Total = 0;
    indice = 0;#servira como indice en el while
    limite = 0;#servira como tope en el while
    codigo = 0;#guardara 1 codigo por vez
    precio = 0;#guardara un precio  por vez
    codigos = [];#guardara los codigos
    precios = [];#guardara los precios
    opcion = 1;#sera la opcion para registrar productos
    codigo = (input(str("Ingrese el codigo del producto ")));#se ingresa el codigo del producto
    try:#si ingreso un codigo correcto
        codigo = int(codigo);
        if codigo < 0:#si el codigo es un numero negativo
            codigo = input("El codigo debe ser un numero positivo ");
            errorcatch += 1;#se aumenta el contador de error
        codigos.append(codigo);#se almacena el codigo
    except:#si ingreso un caracter
        codigo = (input(str("Debe ingresar un numero en el codigo ")));#se ingresa el codigo del producto
        codigo = int(codigo);
        if codigo < 0:#si el codigo es un numero negativo
            codigo = input("El codigo debe ser un numero positivo ");
            errorcatch += 1;#se aumenta el contador de error
        codigos.append(codigo);#se almacena el codigo
        errorcatch += 1;#se aumenta el contador de error
    precio = (input(str("Ingrese el precio del producto ")));#se ingresa el precio del producto
    try:#si ingreso un precio correcto
        precio = int(precio);
        if precio < 0:#si el precio es un numero negativo
            precio = input("El precio debe ser un numero positivo ");
            errorcatch += 1;#se aumenta el contador de error
        precios.append(precio);#se almacena el precio
    except:#si ingreso un caracter
        precio = (input(str("Debe ingresar un numero en el precio ")));#se ingresa el precio del producto
        precio = int(precio);
        if precio < 0:#si el precio es un numero negativo
            precio = input("El precio debe ser un numero positivo ");
            errorcatch += 1;#se aumenta el contador de error
        precios.append(precio);#se almacena el precio
        errorcatch += 1;#se aumenta el contador de error
    
    while opcion == 1:
        opcion = str(input("Ingresa 1 para ingresar mas productos,cualquier otro numero para salir "));
        try:
            opcion = int(opcion);
            if opcion == 1 :
                codigo = (input(str("Ingrese el codigo del producto ")));#se ingresa el codigo del producto
                try:#si ingreso un codigo correcto
                    codigo = int(codigo);
                    if codigo < 0:#si el codigo es un numero negativo
                        codigo = input("El codigo debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                    codigos.append(codigo);#se almacena el codigo
                except:#si ingreso un caracter
                    codigo = (input(str("Debe ingresar un numero en el codigo ")));#se ingresa el codigo del producto
                    codigo = int(codigo);
                    if codigo < 0:#si el codigo es un numero negativo
                        codigo = input("El codigo debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                    codigos.append(codigo);#se almacena el codigo
                    errorcatch += 1;#se aumenta el contador de error
                precio = (input(str("Ingrese el precio del producto ")));#se ingresa el precio del producto
                try:#si ingreso un precio correcto
                    precio = int(precio);
                    if precio < 0:#si el precio es un numero negativo
                        precio = input("El precio debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                    precios.append(precio);#se almacena el precio
                except:#si ingreso un caracter
                   precio = (input(str("Debe ingresar un numero en el precio ")));#se ingresa el precio del producto
                   precio = int(precio);
                   if precio < 0:#si el precio es un numero negativo
                        precio = input("El precio debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                        precios.append(precio);#se almacena el precio
                        errorcatch += 1;#se aumenta el contador de error
        except:#si no ingresa un numero
            opcion = str(input("Debe ingresar 1 o cualquier numero como opcion valida para poder continuar "));
            opcion = int(opcion);
            if opcion == 1 :
                codigo = (input(str("Ingrese el codigo del producto ")));#se ingresa el codigo del producto
                try:#si ingreso un codigo correcto
                    codigo = int(codigo);
                    if codigo < 0:#si el codigo es un numero negativo
                        codigo = input("El codigo debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                    codigos.append(codigo);#se almacena el codigo
                except:#si ingreso un caracter
                    codigo = (input(str("Debe ingresar un numero en el codigo ")));#se ingresa el codigo del producto
                    codigo = int(codigo);
                    if codigo < 0:#si el codigo es un numero negativo
                        codigo = input("El codigo debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                    codigos.append(codigo);#se almacena el codigo
                    errorcatch += 1;#se aumenta el contador de error
                precio = (input(str("Ingrese el precio del producto ")));#se ingresa el precio del producto
                try:#si ingreso un precio correcto
                    precio = int(precio);
                    if precio < 0:#si el precio es un numero negativo
                        precio = input("El precio debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                    precios.append(precio);#se almacena el precio
                except:#si ingreso un caracter
                    precio = (input(str("Debe ingresar un numero en el precio ")));#se ingresa el precio del producto
                    precio = int(precio);
                    if precio < 0:#si el precio es un numero negativo
                        precio = input("El precio debe ser un numero positivo ");
                        errorcatch += 1;#se aumenta el contador de error
                    precios.append(precio);#se almacena el precio
                    errorcatch += 1;#se aumenta el contador de error
    
    
    print("Super Lagunitas S.A de C.V, Gomez de Mendiola #555");#Se imprime la linea de titulo del recibo
    limite = len(codigos);#se indica el numero de productos
    while limite > 0 :# se imprimen todos los productos y precios
        print("codigo",codigos[indice],"         $",precios[indice]);
        Sub_total += precios[indice];#se calcula el subtotal
        indice += 1;
        limite -= 1;
    iva = Sub_total*0.15;#se calcula el iva
    Total = Sub_total + iva;#se calcula el total
    #se imprime el subtotal, iva y total
    print("Subtotal $",Sub_total);
    print("IVA $",iva);
    print("Total $",Total);
    return errorcatch;#retorna el numero de errores
        
def e2(errorcatch):
    errorcatch = caja(errorcatch);
    print(Fore.BLACK+Back.LIGHTMAGENTA_EX+Cursor.POS(10,10)+"Ejercicio 2", end="");
    input(Fore.BLACK+Cursor.POS(3,11)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def fecha(errorcatch): #Se hara un algoritmo para determinar cuantos años, meses, semas y dias hay en un total de dias ingresados
    años=0; #Inicializamos las variables que necesitaremos
    meses=0;
    semanas=0;
    dias=0;
    dias_usu=0;
    bisiesto=0;
    aumento=[0];
    for i in aumento: #El for estara para en caso de error except, seguir repitiendo el ciclo
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese los dias: ", end="");
        dias_usu=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try: #Si ingreso un numero valido
            dias_usu=int(dias_usu);
            if dias_usu < 0: #Si los dias son negativos, los vuelve a pedir
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingrese un numero de dias real!", end="");
                aumento.append(0);
                sleep(1);
            elif dias_usu == 0: #Si son igual a 0, no hara nada que hacer
                pass;
            else:
                dias=dias_usu;
                while dias_usu >= 365: #Cada 365 contara un año
                    años+=1;
                    dias_usu-=365;
                    if años % 4 == 0: #Si pasan 4 años, habra 1 bisiesto en cada uno de ellos
                        bisiesto+=1;
                for x in range(bisiesto): #Por cada bisiesto que hubo, restara 1 dias al total, porque se habra puesto 1 dia extra
                    dias_usu-=1;
                if dias_usu == -1: #Para evitar errores, si el año dejo en negativos los dias, este, los regresara y restara un año
                    dias_usu+=366;
                    años-=1;

                while dias_usu >= 30: #Cada 1 mes se restaran 30 dias
                    meses+=1;
                    dias_usu-=30;
                    if meses % 2 == 0: #Cada 2 meses se restara 1 dia extra, para compensar que no todos los meses son de 30 dias
                        dias_usu-=1;
                if dias_usu==-1: #Para evitar errores, si los meses los deja en negativos,lo regresara para contarlo en semanas y dias
                    dias_usu+=31;
                    meses-=1;
                if meses==12: #No es posible que se llegue a 12 meses, asi que removera ese mes y regresara los dias
                    dias_usu+=31; 
                    meses-=1;
                while dias_usu >= 7: #Cada 7 dias contara 1 semana extra
                    semanas+=1;
                    dias_usu-=7;
                 
        except: #Si ingresa un dato incorrecto, manda error, y el ciclo se repite
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese un numero entero!", end="");
            aumento.append(0);
            sleep(1);
    #Aca se hara toda la impresion de datos
    dibujo(errorcatch);
    aux=str(dias);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,4)+"En el total de dias de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    aux=str(años);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,5)+"Hay un total de años de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    aux=str(meses);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,6)+"Con un numero de meses de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    aux=str(semanas);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,7)+"Con un numero de semanas de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    aux=str(dias_usu);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,8)+"Con un numero de dias de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    aux=str(bisiesto);
    print(Fore.BLACK+Back.WHITE+Cursor.POS(3,9)+"Hubo un total de año bisiestos de: ", end="");
    print(Fore.BLACK+Back.WHITE+aux, end="");
    return errorcatch;#Regresara el total de except al ejercicio


def e3(errorcatch):
    errorcatch=fecha(errorcatch);
    print(Fore.BLACK+Back.LIGHTMAGENTA_EX+Cursor.POS(3,10)+"Ejercicio 3", end="");
    input(Fore.BLACK+Cursor.POS(3,11)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu

def repetidos(errorcatch): #Se hara una funcion que cambie todos los numero repetidos en una lista
    aumento=[0]; #Se inicializan las variables de listas para los for, y las listas a imprimir al final
    aumentob=[0];
    lista=[];
    lista_n=[];
    numero=0;
    contador=0;
    cambios=0;
    for i in aumento: #El for sera para seguir preguntando si quiere ingresar un numero
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese 1 para ingresar numero y 0 para salir: ", end="");
        opcion=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try:
            opcion=int(opcion);
            if opcion < 0 or opcion > 1: #Si la opcion no es 0 ni 1
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingrese 1 ó 0!", end="");
                aumento.append(0);
                sleep(1);
            elif opcion == 0: #Si es 0 acaba el for
                pass;
            elif opcion == 1: #Si es 1 pide el valor a ingresar y comprueba que no sea negativo ni un caracter
                for x in aumentob:
                    dibujo(errorcatch);
                    aumento.append(0);
                    print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese un numero entero positivo: ", end="");
                    numero=str(input(Fore.BLACK+Back.WHITE));
                    print("",end="");
                    try:
                        numero=int(numero);
                        if numero < 0 : #En caso de que sea negativo
                            dibujo(errorcatch);
                            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Tiene que ser positivo!", end="");
                            aumentob.append(0);
                            sleep(1);
                        else: #En otro caso lo agregara a la lista
                            lista.append(numero);
                            contador+=1;
                            
                    except: #Si ingresa un dato incorrecto, manda error, y el ciclo se repite
                        errorcatch+=1;
                        dibujo(errorcatch);
                        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese un numero entero!", end="");
                        aumentob.append(0);
                        sleep(1);

        except: #Si ingresa un dato incorrecto, manda error, y el ciclo se repite
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese un numero entero!", end="");
            aumento.append(0);
            sleep(1);

    lista_n.extend(lista); #Se creara una copia de la lista para imprimir las diferencias
    for y in range(contador): #Estos compararan cada dato con cada uno de los otros para verificar los que se repiten
        for x in range(contador):
            if lista[y] == lista[x] and y!=x and lista[x] != -1: #En caso de que se repita, no sea el mismo de la posicion, y no sea -1
                lista[x]=-1; #Hara el cambio a -1
                cambios+=1;

    dibujo(errorcatch);
    if contador == 0: #Si no ingreso nada a la lista
        print(Fore.BLACK+Back.WHITE+Cursor.POS(3,4)+"No se ingreso nada en la lista", end="");
    else: 
        aux=str(lista_n);
        print(Fore.BLACK+Back.WHITE+Cursor.POS(3,4)+"Lista original   : ", end="");
        print(Fore.BLACK+Back.WHITE+aux, end="");
        aux=str(lista);
        print(Fore.BLACK+Back.WHITE+Cursor.POS(3,5)+"Lista actualizada: ", end="");
        print(Fore.BLACK+Back.WHITE+aux, end="");
        aux=str(cambios);
        print(Fore.BLACK+Back.WHITE+Cursor.POS(3,6)+"NO. de cambios: ", end="");
        print(Fore.BLACK+Back.WHITE+aux, end="");

    return errorcatch; #Regresara el total de except al ejercicio

def e4(errorcatch):
    errorcatch=repetidos(errorcatch);
    print(Fore.BLACK+Back.LIGHTMAGENTA_EX+Cursor.POS(3,8)+"Ejercicio 4", end="");
    input(Fore.BLACK+Cursor.POS(3,9)+Back.WHITE+"");
    print("",end="");
    return errorcatch; #Regresara el total de except al menu


def menu():
    errorcatch=0; #Inicializa la variables de errores except
    opcion=1;
    while opcion != 0: #Mientras la opcion no sea 0 para salir, seguira en el menu
        dibujo(errorcatch);
        print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Style.DIM+"Ingrese el numero de ejercicio a ejecutar o 0 para salir: ", end="");
        opcion=str(input(Fore.BLACK+Back.WHITE));
        print("",end="");
        try:
            opcion=int(opcion);
            if opcion < 0 or opcion > 4: #Si esta fuera de rango
                dibujo(errorcatch);
                print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"Ingresa un numero valido!",end ="");
                sleep(1);   
            
            else: #En otro caso realizara la opcion pedida
                if opcion == 1:
                    errorcatch=e1(errorcatch);
                   
                if opcion == 2:
                    errorcatch=e2(errorcatch);
                    
                if opcion == 3:
                    errorcatch=e3(errorcatch);
                    
                if opcion == 4:
                    errorcatch=e4(errorcatch);
                   
                
        except: #Si ingresa caracteres
            errorcatch+=1;
            dibujo(errorcatch);
            print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"ERROR! Ingrese un numero entero!", end="");
            sleep(1);


menu();
dibujo(-1);
print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,4)+"practica 10", end="");
print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,5)+"becerra gonzalez diego ivan", end="");
print(Fore.BLACK+Cursor.POS(3,4)+Back.WHITE+Cursor.POS(3,6)+"padilla valdez gustavo", end="");
input();
os.system("cls");
