#practica 09
#becerra gonzalez diego ivan
#padilla valdez gustavo

def e1():
        print("\ejercicio 1");
def e2():
        print("\ejercicio 2");
def e3():
        print("\ejercicio 3");
def e4():
        print("\ejercicio 4");
def e5():
        print("\ejercicio 5");
def e6():
        print("\ejercicio 6");
def e7():
        print("\ejercicio 8");

def menu():#muestra el menu
    i = int(input("Ingresa el numero de ejercicio a ejecutar y 8 para salir"));
    for i in range (8):
        
        if i == 1 :
            e1();
            i = 0;
        elif i == 2 :
            e2();
            i = 0;
        elif i == 3 :
            e3();
            i = 0;
        elif i == 4 :
            e4();
            i = 0;
        elif i == 5 :
            e5();
            i = 0;
        elif i == 6 :
            e6();
            i = 0;
        elif i == 7 :
            e7();
            i = 0;
        i = int(input("Ingresa el numero de ejercicio a ejecutar y 8 para salir"));
        i=0;
menu();
print("\nPractica 9");
