#practica 09
#becerra gonzalez diego ivan
#padilla valdez gustavo

def e1():#funcion para el ejercicio 1
    print("\nEjercicio 1");

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
                                aumento.append(0);
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
                                        pass;
                                
                except :#en caso de que ingrese un caracter
                        opcion = str(input("Debes ingresar un numero "));
                        aumento.append(0);
                        

menu();

print("\npractica 09");
print("becerra gonzalez diego ivan");
print("padilla valdez gustavo");
