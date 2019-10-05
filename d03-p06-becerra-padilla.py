#practica 06
#becerra gonzalez diego ivan
#padilla valdez gustavo

#funciones ejercicio 1
def promMat():
    totalTareas=300;
    totalExamen=100;
    t1=20;
    t2=70;
    t3=80;
    tareasReal=t1+t2+t3;
    examenReal=90;
    valorEx=20;
    valorTar=80;
    porcentajeEx=(examenReal*valorEx)/totalExamen;
    porcentajeTar=(tareasReal*valorTar)/totalTareas;
    promedio=porcentajeEx+porcentajeTar;
    print("\nEn el examen de matematicas saco",examenReal);
    print("En su tarea 1 su calificacion fue: ",t1);
    print("En su tarea 2 su calificacion fue: ",t2);
    print("En su tarea 3 su calificacion fue: ",t3);
    print("Su promedio en matematicas fue",promedio);
    return promedio;

def promFis():
    totalExamen=100;
    totalTareas=300;
    t1=20;
    t2=70;
    t3=80;
    tareasReal=t1+t2+t3;
    examenReal=90;
    valorEx=45;
    valorTar=55;
    porcentajeEx=(examenReal*valorEx)/totalExamen;
    porcentajeTar=(tareasReal*valorTar)/totalTareas;
    promedio=porcentajeEx+porcentajeTar;
    print("\nEn el examen de fisica saco",examenReal);
    print("En su tarea 1 su calificacion fue: ",t1);
    print("En su tarea 2 su calificacion fue: ",t2);
    print("En su tarea 3 su calificacion fue: ",t3);
    print("Su promedio en fisica fue",promedio);
    return promedio;

def promQuim():
    totalExamen=100;
    totalTareas=900;
    t1=20;
    t2=70;
    t3=80;
    t4=20;
    t5=70;
    t6=80;
    t7=20;
    t8=70;
    t9=80;
    tareasReal=t1+t2+t3+t4+t5+t6+t7+t8+t9;
    examenReal=90;
    valorEx=85;
    valorTar=15;
    porcentajeEx=(examenReal*valorEx)/totalExamen;
    porcentajeTar=(tareasReal*valorTar)/totalTareas;
    promedio=porcentajeEx+porcentajeTar;
    print("\nEn el examen de quimica saco",examenReal);
    print("En su tarea 1 su calificacion fue: ",t1);
    print("En su tarea 2 su calificacion fue: ",t2);
    print("En su tarea 3 su calificacion fue: ",t3);
    print("En su tarea 4 su calificacion fue: ",t4);
    print("En su tarea 5 su calificacion fue: ",t5);
    print("En su tarea 6 su calificacion fue: ",t6);
    print("En su tarea 7 su calificacion fue: ",t7);
    print("En su tarea 8 su calificacion fue: ",t8);
    print("En su tarea 9 su calificacion fue: ",t9);
    print("Su promedio en quimica fue",promedio);
    return promedio;

def promGeneral():
    matematicas=promMat();
    fisica=promFis();
    quimica=promQuim();
    promedio=(matematicas+fisica+quimica)/3;
    print("\nSu promedio general fue",promedio);

def e1():
    print("Ejercicio 1");
    promGeneral();

#funciones ejercicio 2
def calculaGanancia():
    capital=100;
    razon=0.073;
    ganancia=capital*razon;
    total=ganancia+capital;
    print("El capital invertido fue",capital,"y la ganancia fue de",ganancia);
    print("Tu total es $", total);

def e2():
    print("\nEjercicio 2");
    calculaGanancia();

#funciones ejercicio 3
def calculaDinero():
    sueldoBase=1000;
    porcentajeComision=0.15;
    venta1=100;
    venta2=100;
    venta3=100;
    venta4=100;
    venta5=100;
    venta6=100;
    venta7=100;
    venta8=100;
    venta9=100;
    venta10=100;
    totalVentas=venta1+venta2+venta3+venta4+venta5+venta6+venta7+venta8+venta9+venta10;
    totalComisiones=porcentajeComision*totalVentas;
    sueldoAnual=sueldoBase+totalComisiones;
    sueldoMensual=sueldoAnual/12;
    print("Su sueldo base es de",sueldoBase);
    print("la venta 1 fue por",venta1);
    print("la venta 2 fue por",venta2);
    print("la venta 3 fue por",venta3);
    print("la venta 4 fue por",venta4);
    print("la venta 5 fue por",venta5);
    print("la venta 6 fue por",venta6);
    print("la venta 7 fue por",venta7);
    print("la venta 8 fue por",venta8);
    print("la venta 9 fue por",venta9);
    print("la venta 10 fue por",venta10);
    print("Su sueldo mensual es de",sueldoMensual);
    

def e3():
    print("\nEjercicio 3");
    calculaDinero();

#funciones ejercicio 4
def descuento():
    part=100;
    desc=0.155;
    descart=part*desc;
    pfinal=part-descart;
    print("El articulo costaba: ",part);
    print("El descuento fue de ",desc*100,"%");
    print("El precio final del articulo a pagar es: ",pfinal);

def e4():
    print("\nEjercicio 4");
    descuento();

#funciones ejercicio 5
def califalgoritmos():
    cp1=90;
    cp2=90;
    ef=90;
    tf=20;
    cpf=(cp1+cp2)/2;
    totalp=(55/100)*cpf;
    totale=(30/100)*ef;
    totalt=(15/100)*tf;
    calfinal=totalp+totale+totalt;
    print("En su primer parcial su calificacion fue de: ",cp1);
    print("En su segundo parcial su calificacion fue de: ",cp2);
    print("En su examen final su calificacion fue de: ",ef);
    print("En su trabajo final su calificacion fue de: ",tf);
    print("Su calificacion final de la materia de Algoritmos es: ",calfinal);

def e5():
    print("\nEjercicio 5");
    califalgoritmos();

#funciones ejercicio 6
def grupoestudiantes():
    hombres=30;
    mujeres=20;
    total=hombres+mujeres;
    porh=(100/total)*hombres;
    porm=(100/total)*mujeres;
    print("El numero de hombre en el salon es de ",hombres);
    print("El numero de mujeres en el salon es de ",mujeres);
    print("El porcentaje de hombres en el salon es del:",porh,"%");
    print("El porcentaje de mujeres en el salon es del:",porm,"%");
    
def e6():
    print("\nEjercicio 6");
    grupoestudiantes();

#funciones ejercicio 7
def edad():
    fact=2019;
    fnac=1999;
    edad=fact-fnac;
    print("Estamos en el año",fact);
    print("Naciste en el año",fnac);
    print("Tu edad es de",edad,"años");

def e7():
    print("\nEjercicio 7");
    edad();

#funciones ejercicio 8
def hospital():
    prepanual=1000;
    gine=(prepanual/100)*30;
    trauma=(prepanual/100)*30;
    pedia=(prepanual/100)*40;
    print("El presupuesto anual del hospital es de $",prepanual);
    print("El presupuesto anual para Ginecologia es de $",gine);
    print("El presupuesto anual para Traumatologia es de $",trauma);
    print("El presupuesto anual para Pediatria es de $",pedia);
    

def e8():
    print("\nEjercicio 8");
    hospital();

#funciones ejercicio 9
def gananciaArticulo():
    art=100;
    gan=0.15;
    adgan=art*gan;
    preciof=art+adgan;
    print("El articulo fue adquirido por $",art);
    print("Se quiere una ganancia del",gan*100,"%");
    print("El precio final sera de $",preciof);
    
def e9():
    print("\nEjercicio 9");
    gananciaArticulo();

#funciones ejercicio 10
def tiempoProm():
    lunes=10;
    miercoles=10;
    viernes=1;
    promedio=(lunes+miercoles+viernes)/3;
    print("El tiempo que duro el lunes fue de",lunes,"minutos");
    print("El tiempo que duro el miercoles fue de",miercoles,"minutos");
    print("El tiempo que duro el viernes fue de",viernes,"minutos");
    print("Su tiempo promedio es de",promedio,"minutos");
    
def e10():
    print("\nEjercicio 10");
    tiempoProm();

#funciones ejercicio 11
def promPers():
    per1=100;
    per2=500;
    per3=400;
    invTotal=per1+per2+per3;
    por1=(per1*100)/invTotal;
    por2=(per2*100)/invTotal;
    por3=(per3*100)/invTotal;
    print("La inversion total fue de $",invTotal);
    print("La primer persona invirtio $",per1,"o el",por1,"% de la inversion total");
    print("La segunda persona invirtio $",per2,"o el",por2,"% de la inversion total");
    print("La tercer persona invirtio $",per3,"o el",por3,"% de la inversion total");
    
def e11():
    print("\nEjercicio 11");
    promPers();

e1();
e2();
e3();
e4();
e5();
e6();
e7();
e8();
e9();
e10();
e11();

print("\npractica 06");
print("becerra gonzalez diego ivan");
print("padilla valdez gustavo");
