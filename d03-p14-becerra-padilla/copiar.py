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