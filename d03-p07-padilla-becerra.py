#practica 07
#padilla valdez gustavo
#becerra gonzalez diego ivan


#Funciones del ejercicio 1
def aprobacion():
    calif = (float(input("Dime tu calificacion "))); #Pedimos al usuario su calificacion
    aprobatoria = 80;
    if calif > aprobatoria and calif <=100: #Si su calificacion es mayor a 80 y menor o
        #igual a 100 esta aprobado
        print("aprobado");
    elif calif <= aprobatoria and calif >= 0: #Si es menor a 80  y mayor o igual a 0 esta
        #reprobado
        print("Reprobado");
    else: #Si no cumple las condiciones imprime eso
        print("Ingresa una calificacion valida");

def e1():
    print("\nEjercicio 1");
    aprobacion();


#Funciones del ejercicio 2
def sueldo():
    sueldo = (float(input("Dime cuanto es tu sueldo "))); #Se pide al usuario el sueldo
    sueldo_final = sueldo; #Se le agrega el sueldo al sueldo final
    if sueldo < 20000:
        sueldo_final += (sueldo/100)*30;#A lo que ya teniamos de sueldo se le agrega un 30%
    elif sueldo <= 23000:
        sueldo_final += (sueldo/100)*15;#A lo que ya teniamos de sueldo se le agrega un 15%
    elif sueldo <= 25000:
        sueldo_final += (sueldo/100)*5;#A lo que ya teniamos de sueldo se le agrega un 5%
    else:
        pass;#En otro caso no agrega nada al sueldo
    
    print("Su nuevo sueldo es de $", sueldo_final);

def e2():
    print("\nEjercicio 2");
    sueldo();


#Funciones del ejercicio 3 
def horas_extra():
    sueldo_hora = (float(input("Cuanto te pagan por hora: ")));
    horas = (int(input("Cuantas horas trabajaste: ")));
    sueldo = 0;
    sueldo_extra = 0;
    sueldo_extra_tp = 0; 
    sueldo_total = 0;
    horas_extra = 0; #Declaro las variables para poder usarlas al final
    
    if horas <= 40:
        sueldo = sueldo_hora * horas; #El sueldo sera igual a cuanto le pagan por hora, por las horas que trabajo
        sueldo_total = sueldo;
    elif horas > 40 and horas <= 48:
        horas_extra = horas - 40; #Para saber cuantas horas extra trabajo, le restamos 40 a las horas trabajadas
        sueldo_extra = (sueldo_hora * 2) * horas_extra;#Multiplica esas horas extra por el sueldo, y luego las hace dobles(*2)
        sueldo = sueldo_hora * 40;#Saca el sueldo normal, solo contando las primeras 40 horas
        sueldo_total = sueldo + sueldo_extra; #Suma el sueldo normal y el sueldo extra
    else:
        horas_extra = horas - 40; #Saca las horas extra
        horas_extra_tp = horas_extra - 8; #Calcula las horas extras triple, restando las primeras 8 extra que son dobles
        sueldo_extra = (sueldo_hora * 2) * 8; #Calula el sueldo de las horas doble
        sueldo_extra_tp = (sueldo_hora * 3) * horas_extra_tp; #Calcula el sueldo de las horas triple
        sueldo = sueldo_hora * 40; #Saca el sueldo normal
        sueldo_total = sueldo + sueldo_extra + sueldo_extra_tp; #Suma los sueldos
        
    print("Tu sueldo normal es de $", sueldo);
    print("Trabajaste ", horas_extra, "horas extra");
    if horas_extra > 0: #Solamente muestra este mensaje si trabajo horas extra
        print("Esas horas te dieron $", sueldo_extra + sueldo_extra_tp, "más");
    print("Tu sueldo final es de $", sueldo_total);

def e3():
    print("\nEjercicio 3");
    horas_extra();


#Funciones del ejercicio 4  
def cal_subsidio():
    sub = 0;
    num_hijos = 0;
    num_hijos_esc = 0;
    viuda = 0;
    #guarda el numero de hijos
    num_hijos = int(input("Ingresa el numero de hijos que tienes "));
    #si es un numero posible continua
    if num_hijos > 0 and num_hijos < 53 :
        #si tiene hasta dos hijos el subsidio es de 70
        if num_hijos <= 2 :
            sub = 70;
        # si tiene entre 3  5 hijos el subsidio es 90
        elif num_hijos >= 3 and num_hijos <= 5 :
            sub = 90;
        #si tiene mas de 5 el subsidio es de 120
        elif num_hijos > 5:
            sub = 120;
        #guarda el numero de hijos en edad escolar
        num_hijos_esc = int(input("¿cuantos de ellos tienen entre 6 y 18 años? "));
        #si ingresa un dato valido multiplica el numero de hijos en edad escolar por 10 y lo suma
        if num_hijos_esc <= num_hijos :
            sub += (num_hijos_esc * 10);
            #guarda 1 si es viuda
            viuda = int(input("Si eres viuda ingresa 1, si no ingresa 0   "));
            #suma 20 si es viuda
            if viuda == 1:
                sub += 20.00;
            # si no no suma nada
            elif viuda == 0:
                sub = sub;
            #si escribe otra cosa en viuda, le pide que ingrese un dato correcto
            else :
                print("Debes ingresar un dato correcto");
                sub = 0;
        #si no ingresa un numero valido de hijos en edad escolar le pide que lo haga
        elif num_hijos_esc < 0 or num_hijos_esc > num_hijos:
            print("Ingresa un numero valido");
            sub = 0;
    #Si es igual a 0 solo le pregunta si es viuda
    elif num_hijos == 0 :
        #guarda 1 si es viuda
        viuda = int(input("Si eres viuda ingresa 1, si no ingresa 0   "));
        #suma 20 si es viuda
        if viuda == 1:
            sub += 20.00;
        # si no no suma nada
        elif viuda == 0:
            sub = sub;
        #en otro caso pide un numero valido
        else :
            print("Debes ingresar un dato correcto");
    #Si el numero de hijos no es correcto
    else :
        print("Debes ingresar un dato correcto");
        #guarda 3 en viuda porque se salta ese paso
        viuda = 3;
        
    #imprime sus datos
    #si tiene un numero de hijos posible
    if num_hijos > 0 and num_hijos < 53 :
        print("Tienes ", num_hijos, "hijos");
        print("De los cuales ", num_hijos_esc , "estan en edad escolar");
    #si no es viuda
    if viuda == 0 :
        print("No eres viuda");
    #si es viuda
    elif viuda == 1 :
        print("Eres viuda");
    print("El subsidio es de $",sub, "mensuales");
    
def e4():
    print("\nEjercicio 4");
    cal_subsidio();


#Funciones del ejercicio 5  
def mayor_edad():
    #se piden las fechas
    dia_act = int(input("ingresa el dia actual con número "));
    mes_act = int(input("ingresa el mes actual con número "));
    anio_act = int(input("ingresa el año actual con número "));
    dia_nac = int(input("ingresa tu dia de nacimiento con número "));
    mes_nac = int(input("ingresa tu mes de nacimiento con número "));
    anio_nac = int(input("ingresa tu año de nacimiento con número "));
    #se calcula la diferencia de tiempo entre la fecha actual y la de nacimiento
    dif_anio = anio_act - anio_nac;
    dif_mes = mes_act - mes_nac;
    dif_dia = dia_act - dia_nac;
    #si ingresa las fechas existentes continua
    if dia_act <= 31 and dia_act > 0 and dia_nac <= 31 and dia_nac > 0 and mes_act <= 12 and mes_act > 0 and mes_nac <= 12 and mes_nac > 0 :
        # si la diferencia de años es menor a 18 no entra
        if dif_anio < 18 :
            print("No podras entrar al equipo de golf");
            return 0;
        # si la diferencia de años es igual a 18 evalua la de meses
        if dif_anio == 18 :
            #si la diferencia de meses es menor a 0 no entra
            if dif_mes < 0 :
                print("No podras entrar al equipo de golf");
                return 0;
            #si la diferencia de meses es igual a 0 evalua la de dias
            if dif_mes == 0 :
                #si la diferencia de dias es menor a 0 no entra
                if dif_dia < 0 :
                    print("No podras entrar al equipo de golf");
                    return 0;
                #si la diferencia de dias es igual a 0 no entra
                if dif_dia == 0 :
                    print("No podras entrar al equipo de golf");
                    return 0;
                #si la diferencia de dias es mayor a 0  entra
                if dif_dia > 0 :
                    print("Podras formar parte del equipo de golf");
                    return 1;
            #si la diferencia de meses es mayor a 0  entra
            if dif_mes > 0 :
                print("Podras formar parte del equipo de golf");
                return 1;
        # si la diferencia de años es mayor a 18  entra
        if dif_anio > 18 :
            print("Podras formar parte del equipo de golf");
            return 1;
    #si ingresa fechas inexistentes pide que ingrese reales
    if dia_act > 31 or dia_act < 0 or dia_nac > 31 or dia_nac < 0 or mes_act > 12 or mes_act < 0 or mes_nac > 12 or mes_nac < 0 :
        print("Debes ingresar una fecha correcta");
        
def evalua_prom():
    #si es mayor de edad continua
    if mayor_edad() == 1 :
        #ingresa los demas datos
        grado = int(input("Ingresa el grado escolar que cursas con numero "));
        grupo = str(input("Ingresa tu grupo "));
        promedio = float(input("Ingresa tu promedio hasta el ultimo semestre "));
        #si su promedio es menor de 60 no lo deja entrar
        if promedio < 60 and promedio > 0:
            print("Lo sentimos mucho pero no podrás formar parte por tu bajo promedio");
        #si su promedio es igual o mayor a 60 le pregunta su horario
        if promedio >= 60 and promedio < 101 :
            horario = str(input("¿En que horario prefieres tu entrenamiento? "));
            #imprime sus datos            
            print("Tu grupo es ", grupo);
            print("Tu grado es ", grado);
            print("Tu promedio es ", promedio);
            print("Y tu horario elegido es ", horario);
        #Si ingresa un promedio incorrecto
        if promedio < 0 or promedio > 100 :
            print("Debes ingresar datos correctos");

         
def e5():
    print("\nEjercicio 5");
    evalua_prom();
    

#Funciones del ejercicio 6    
def autos():
    #Pide la placa  y las millas recorridas
    placa = (int(input("Dame tu numero de auto: ")));
    millas = (float(input("¿Cuantas millas haz recorrido?: "))); 
    
    if millas > 80: #Si las millas son mayores a 80 desplegar el mensaje
        print("\n-Esta arriba del limite de velocidad-\n");
    else: #En otro caso muestra mensaje
        print("\n-No esta arriba del limite de velocidad-\n");
        
    kms = (float(input("¿Cuantos kilometros haz recorrido?: "))); #Pide los km recorridos
    
    if kms > 200 and kms <350: #Si los km pasan 200 pero tambien son menores a 350 desplegar el mensaje
        print("\n-Hace falta mantenimiento al auto-\n");
    else: #En otro caso muestra otro mensaje
        print("\n- No Hace falta mantenimiento al auto-\n");
        
    #Pide los km que recorre por litro
    km_litro = (int(input("¿Cuantos kilometros reccores por litro de gasolina? (Solo de 16 a 10): ")));
    if km_litro <= 16 and km_litro >= 14: #Si son menores o igual a 16 y mayores o igual a 14 despliega los mensajes
        print("Su auto consume poca gasolina");
        litros_recorrido = 100/km_litro; #Calcula los litros que consume, dividiendo los 100 km entre lo que gasta por litro
        print("En 100 kilometros su auto gasta", litros_recorrido, "litros de gasolina"); 
    elif km_litro <= 13 and km_litro >= 10: #Si son menores o igual a 13 y mayores o igual a 10 despliega el mensaje
        print("Consume algo de gasolina");
    else: #En otro caso mostrar mensaje default
        print("Ese consumo de gasolina no estaba en nuestras expectativas");
        
def e6():
    print("\nEjercicio 6");
    autos();


#Funciones del ejercicio 7  
def basquetbol():
    jugador = (int(input("Dame tu numero de jugador: ")));
    anotados = (int(input("¿Cuantos tiros anotaste?: ")));
    fallados = (int(input("¿Cuantos tiros fallaste?: "))); 
    
    if anotados > 0 and fallados > 0: #Si los anoto y fallo al menos un tiro
        tiros_total = anotados + fallados; #Suma los tiros para sacar el total
        print("\nHiciste", tiros_total, "tiros en total\n");#Imprime el total
    else: #En otro caso no saca el total 
        if fallados == 0: #Si los tiros fallados son 0 despliega el mensaje
            print("No fallaste ningun tiro");
        if anotados == 0: #Si los tiros anotados son 0 despliega el mensaje
            print("No anotaste ningun tiro");

    if anotados <= 0:
        print("Si no anotaste nada, no pudiste haber hecho puntos");
        puntos = 0;
    else:
        puntos = (int(input("¿Cuantos puntos anotaste?: ")));
    
    if puntos <= 6 and puntos >=3: #Si los puntos son menores o igual a 6 y mayores o igual a 3
        print("Anotó pocos puntos"); #Imprime el mensaje
        
    elif puntos <= 15 and puntos >=7:#Si los puntos son menores o igual a 15 y mayores o igual a 7
        puntos_tres = puntos/3; #Saca el promedio de triples que pudo hacer en base a los puntos que anoto
        print("Anotó puntos aceptables"); #Imprime el mensaje
        print("Tu promedio de triples que pudiste haber anotado fue de ", puntos_tres);

    elif puntos <= 22 and puntos >=16:#Si los puntos son menores o igual a 22 y mayores o igual a 16
        puntos_tres = puntos/3;#Saca el promedio de triples que pudo hacer en base a los puntos que anoto
        print("Felicidades por sus anotaciones");#Imprime el mensaje
        print("Tu promedio de triples que pudiste haber anotado fue de ", puntos_tres);

    else: #En otro caso muestra un mensaje default
        print("Los puntos anotados no estaban en nuestras expectativas"); 
    
def e7():
    print("\nEjercicio 7");
    basquetbol();


e1();
e2();
e3();
e4();
e5();
e6();
e7();

print("\npractica 07");
print("padilla valdez gustavo");
print("becerra gonzalez diego ivan");
