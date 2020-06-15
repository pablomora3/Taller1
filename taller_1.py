import os
import sys
import math
opcionMenu = 0
cantidadingresos = 2
lista_cantidad_potasio = []
lista_cantidad_argon = []
K = 0
A = 0
indice = 0
lista = ""

class Menu:
        
    def menu():
        os.system('clear')
        print ("Bienvenido al sistema datasión potasio-argon")
        print ("\t1 - Ingresar Datos")
        print ("\t2 - Realizar Calculo")
        print ("\t3 - Actualizar Datos")
        print ("\t4 - Reiniciar")
        print ("\t0 - Salir")
        while True:
            try:
                opcionMenu = int(input("Ingrese la opcion deseada --> "))
                if opcionMenu==1:
                    Listas.agrega_listas()
                elif opcionMenu==2:
                    Calculo.formula()
                elif opcionMenu==3:
                    Modificar.actualiza()
                elif opcionMenu==4:
                    lista_cantidad_argon.clear()
                    lista_cantidad_potasio.clear()
                    Menu.menu()
                elif opcionMenu==0:
                    print("")
                    input("Programa terminado\npulsa una tecla para continuar")
                    os.system('clear')
                    sys.exit()
                elif opcionMenu>4:
                    print ("El valor de la cantidad debe ser numerico y dentro de las opciones dadas")
                elif opcionMenu<0:
                    print ("El valor de la cantidad debe ser numerico y dentro de las opciones dadas")
            except ValueError:
                print ("El valor de la cantidad debe ser numerico y dentro de las opciones dadas")

class Listas:
    def agrega_listas():
        os.system('clear')
        while True:
            try:
                cantidadingresos=int(input("Ingrese una cantidad de muestras a evaluar: "))
                i = 1
                while i <= cantidadingresos:
                    try:
                        potasio=float(input("Ingrese una cantidad de potasio: "))
                        lista_cantidad_potasio.append(potasio)
                        while True:
                            try:
                                argon=float(input("Ingrese una cantidad de Argón: "))
                                lista_cantidad_argon.append(argon)
                                break
                            except ValueError:
                                print ("El valor de la cantidad debe ser numerico")
                        i = i + 1
                    except ValueError:
                        print ("El valor de la cantidad debe ser numerico")
                print("")
                input("Ha concluido el ingreso de las cantidades, retornando al menu...\npulsa una tecla para continuar")
                Menu.menu()
            except ValueError:
                print ("El valor de la cantidad debe ser numerico")
     
class Calculo:
        
    def formula():
        os.system('clear')
        if len(lista_cantidad_potasio) != 0:
            print("--- Datos de las muestras ---")
            conteo = 0
            cenomayor = 0
            mesomayor = 0
            palemayor = 0
            prepalemayor = 0
            muestramayorc = 0
            muestramayorm = 0
            muestramayorp = 0
            muestramayorpp = 0
            ceno = 0
            meso = 0
            pale = 0
            prepale = 0
            for potasio, argon in zip(lista_cantidad_potasio, lista_cantidad_argon):
                conteo = conteo + 1
                K = potasio
                A = argon
                masa = 0
                era = ""
                edad = (1.248*(10**9))/(math.log(2))*(math.log((K+(A/0.109))/K))
                calcmasa = (K + A)
                if edad < 65500000:
                    era = "cenozoica"
                    ceno = ceno + calcmasa
                    masa = masa + calcmasa
                    if ceno < masa:
                        muestramayorc = conteo
                        cenomayor = masa
                    else:
                        cenomayor = cenomayor
                elif edad < 251000000:
                    era = "mesozoica" 
                    meso = meso + calcmasa
                    masa = masa + calcmasa
                    if meso < masa:
                        muestramayorm = conteo
                        mesomayor = masa
                    else:
                        mesomayor = mesomayor
                elif edad < 542000000:
                    era = "paleozoica" 
                    pale = pale + calcmasa   
                    masa = masa + calcmasa
                    if pale < masa:
                        muestramayorp = conteo
                        palemayor = masa
                    else:
                        palemayor = palemayor
                else:
                    era = "pre-paleozoica"
                    prepale = prepale + calcmasa
                    masa = masa + calcmasa
                    if prepalemayor < masa:
                        muestramayorpp = conteo
                        prepalemayor = masa
                    else:
                        prepalemayor = prepalemayor   
                print("Muestra #" + str(conteo) + ", " 
                + "Cantidad K:" + str(K) + ", " 
                + "Cantidad A:" + str(A) + ", "
                + "Masa:" + str(K + A) + ", "
                + "Edad:" + str(edad) + ", "
                + "Era: " + era)
            print("\n--- Masa por eras ---")
            print("Cenozoica: " + str(ceno) + "mg, " + "La mayor: muestra #" + str(muestramayorc) + " con: " + str(cenomayor) + "mg\n" +
                "Mesozoica: " + str(meso) + "mg, " + "La mayor: muestra #" + str(muestramayorm) + " con: " + str(mesomayor) + "mg\n" +
                "Paleozoica: " + str(pale) + "mg, " + "La mayor: muestra #" + str(muestramayorp) + " con: " + str(palemayor) + "mg\n" +
                "Pre-paleozoica: " + str(prepale) + "mg, " + "La mayor: muestra #" + str(muestramayorpp) + " con: " + str(prepalemayor) + "mg\n")
            print("")
            input("Ha concluido el ingreso de las cantidades, retornando al menu...\npulsa una tecla para continuar")
            Menu.menu()
        else:
            print("")
            input("Aun no hay datos ingresados, retornando al menu...\npulsa una tecla para continuar")
            Menu.menu()

class Modificar:
    
     def actualiza():
        os.system('clear')
        if len(lista_cantidad_potasio) == 0:
            print("")
            input("Aun no existen datos para modificar, presione una tecla para continuar...")
            Menu.menu()
        else:
            print ("Indique el elemento a modificar")
            print ("\t1 - Potasio")
            print ("\t2 - Argon")
            print ("\t0 - Volver al menu")
            while True:
                try:
                    opcionMenu = int(input("Ingrese la opcion deseada --> "))
                    if opcionMenu==1:
                        while True:
                            try:
                                indice = int(input("Ingrese la muestra a modificar --> ")) - 1
                                if indice < len(lista_cantidad_potasio):
                                    while True:
                                        try:
                                            cambio = float(input("Ingrese el nuevo valor --> "))
                                            lista_cantidad_potasio[indice] = cambio
                                            print("")
                                            input("Retornando al menu...\npulsa una tecla para continuar")
                                            Menu.menu()
                                        except ValueError:
                                            print("\nEl valor debe ser numerico\n")
                                if indice>(len(lista_cantidad_potasio)-1):
                                    print("\nLa muestra no existe, la cantidad de muestras es: " + str(len(lista_cantidad_potasio)) + "\n")
                            except ValueError:
                                print("\nLa muestra no existe, la cantidad de muestras es: " + str(len(lista_cantidad_potasio
                                )) + "\n")
                    if opcionMenu==2:
                        while True:
                            try:
                                indice = int(input("Ingrese la muestra a modificar --> ")) - 1
                                if indice < len(lista_cantidad_argon):
                                    while True:
                                        try:
                                            cambio = float(input("Ingrese el nuevo valor --> "))
                                            lista_cantidad_argon[indice] = cambio
                                            print("")
                                            input("Retornando al menu...\npulsa una tecla para continuar")
                                            Menu.menu()
                                        except ValueError:
                                            print("\nEl valor debe ser numerico\n")
                                if indice>(len(lista_cantidad_argon)-1):
                                    print("\nLa muestra no existe, la cantidad de muestras es: " + str(len(lista_cantidad_argon)) + "\n")
                            except ValueError:
                                print("\nLa muestra no existe, la cantidad de muestras es: " + str(len(lista_cantidad_argon)) + "\n")
                    if opcionMenu>2:
                        print("\nEsta no es una opcion valida, ingresela nuevamente\n")
                except ValueError:
                    print("\nEsta no es una opcion valida, ingresela nuevamente\n")

Menu.menu()