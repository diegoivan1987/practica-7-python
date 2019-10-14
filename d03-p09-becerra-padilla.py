#practica 09
#becerra gonzalez diego ivan
#padilla valdez gustavo

def descuento():#calcula el descuento total que se hace en un teatro
    boletos = [-2];#arreglo donde se guardara el descuento del boleto
    cat1 = 0;#guardara el numerode personas qde la categoria 1
    cat2 = 0;#guardara el numerode personas qde la categoria 2
    cat3 = 0;#guardara el numerode personas qde la categoria 3
    cat4 = 0;#guardara el numerode personas qde la categoria 4
    cat5 = 0;#guardara el numerode personas qde la categoria 5
    for i2 in boletos :#for que pedira la edad del cliente hasta que se indique lo contrario
        edad = str(input("Ingresa la edad del cliente(debe de ser mayor de 4 años) y -1 para mostrar el dinero no percibido "));
        try :#si ingreso un numero, entra
            edad = int(edad);
            if edad > 0 and edad < 5 :#si entra dentro del rango de personas no permitidas
                print("No se permiten menores de 5 años");
                boletos.append(-2);
            elif edad >= 5 and edad <= 14 :#si entra dentro de la categoria 1
                boletos.append(35);#se guarda la edad de la persona
                cat1 += 1;#se agrega a su categoria
            elif edad >= 15 and edad <= 19 :#si entra dentro de la categoria 2
                boletos.append(25);#se guarda la edad de la persona
                cat2 += 1;#se agrega a su categoria
            elif edad >= 20 and edad <= 45 :#si entra dentro de la categoria 3
                boletos.append(10);#se guarda la edad de la persona
                cat3 += 1;#se agrega a su categoria
            elif edad >= 46 and edad <= 65 :#si entra dentro de la categoria 4
                boletos.append(25);#se guarda la edad de la persona
                cat4 += 1;#se agrega a su categoria
            elif edad >= 66 and edad <= 120 :#si entra dentro de la categoria 5
                boletos.append(35);#se guarda la edad de la persona
                cat5 += 1;#se agrega a su categoria
            elif edad == -1 :#si ingresa la opcion de salida
                pass;
            else : #en caso de que ingrese cualquier otro numero no valido
                print("Debes ingresar una edad valida");
                boletos.append(-2);
        except :#en caso de que ingrese un caracter
            print("\nDebes de ingresar solo numeros");
            boletos.append(-2);

    costo = 100;#costo del boleto
    desc1 = costo * 0.35;#descuento de la categoria 1
    desc2 = costo * 0.25;#descuento de la categoria 2
    desc3 = costo * 0.1;#descuento de la categoria 3
    desc4 = costo * 0.25;#descuento de la categoria 4
    desc5 = costo * 0.35;#descuento de la categoria 5
    descuento_total = (desc1*cat1)+(desc2*cat2)+(desc3*cat3)+(desc4*cat4)+(desc5*cat5);#sumatoria
    #se imprimen los datos
    print("El boleto cuesta 100");
    print("Personas de la categoria 1: ",cat1);
    print("Personas de la categoria 2: ",cat2);
    print("Personas de la categoria 3: ",cat3);
    print("Personas de la categoria 4: ",cat4);
    print("Personas de la categoria 5: ",cat5);
    print("Descuento total: ",descuento_total);

def e1():#funcion para el ejercicio 1
    print("\nEjercicio 1");
    descuento();

def e2():#funcion para el ejercicio 2
    print("\nEjercicio 2");

def e3():#funcion para el ejercicio 3
    print("\nEjercicio 3");

def e4():#funcion para el ejercicio 4
    print("\nEjercicio 4");

def e5():#funcion para el ejercicio 5
    print("\nEjercicio 5");
   
def e6():#funcion para el ejercicio 6
    print("\nEjercicio 6");

def e7():#funcion para el ejercicio 7
    print("\nEjercicio 7");

def menu():#muestra un menu para ejecutar los ejercicios
        aumento = [0] ;#sera la variable que hace infinito el ciclo
        for i in aumento :#se repetira hasta llegar a 1, al llegar a una opcion o validacion i se inicia en 0
                opcion = str(input("\nIngresa el numero de ejercicio a ejecutar y 8 para salir "));
                try :#si ingresa un numero, lo ejecuta
                        opcion = int(opcion);
                        if opcion < 1 or opcion > 8 :#si esta fuera del rango o es negativo
                                opcion = str(input("Debes ingresar un numero valido "));
                                opcion = int(opcion);
                                if opcion == 1 :#ejecuta el ejercicio 1
                                        e1();
                                        aumento.append(0);
                                if opcion == 2 :#ejecuta el ejercicio 2
                                        e2();
                                        aumento.append(0);
                                if opcion == 3 :#ejecuta el ejercicio 3
                                        e3();
                                        aumento.append(0);
                                if opcion == 4 :#ejecuta el ejercicio 4
                                        e4();
                                        aumento.append(0);
                                if opcion == 5 :#ejecuta el ejercicio 5
                                        e5();
                                        aumento.append(0);
                                if opcion == 6 :#ejecuta el ejercicio 6
                                        e6();
                                        aumento.append(0);
                                if opcion == 7 :#ejecuta el ejercicio 7
                                        e7();
                                        aumento.append(0);
                                if opcion == 8 :
                                        pass;#no se agrega nada para que termine el ciclo
                        else :#en otro caso
                                if opcion == 1 :#ejecuta el ejercicio 1
                                        e1();
                                        aumento.append(0);
                                if opcion == 2 :#ejecuta el ejercicio 2
                                        e2();
                                        aumento.append(0);
                                if opcion == 3 :#ejecuta el ejercicio 3
                                        e3();
                                        aumento.append(0);
                                if opcion == 4 :#ejecuta el ejercicio 4
                                        e4();
                                        aumento.append(0);
                                if opcion == 5 :#ejecuta el ejercicio 5
                                        e5();
                                        aumento.append(0);
                                if opcion == 6 :#ejecuta el ejercicio 6
                                        e6();
                                        aumento.append(0);
                                if opcion == 7 :#ejecuta el ejercicio 7
                                        e7();
                                        aumento.append(0);
                                if opcion == 8 :
                                        pass;#no se agrega nada para que termine el ciclo
                                
                except :#en caso de que ingrese un caracter
                        print("\nDebes de ingresar solo numeros menu");
                        aumento.append(0);
                        

menu();

print("\npractica 09");
print("becerra gonzalez diego ivan");
print("padilla valdez gustavo");
