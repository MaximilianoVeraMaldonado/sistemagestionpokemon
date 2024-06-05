import csv
import msvcrt
import os
#cinturon
equipo= []
#pokedex
Pokedex = ""
#Leer la información del csv
with open('actividad_15\pokemon_primera_generacion(1) (1).csv', newline='', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=",")
    Pokedex = list(data)

#Comenzar el sistema
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")

    print("""\033[33m
    Sistema de Pc de pokemon 
    ══════════════════════════════\033[0m
    1) Mostrar todos los Pokémon disponibles
    2) Buscar un Pokémon por nombre.
    3) Agregar un Pokémon al cinturón.
    4) Mostrar los Pokémon en el cinturón.
    5) Quitar un Pokémon en el cinturón
    6) Generar csv
    0) Salir""")
    opcion = int(input("Seleccione : "))

    if opcion==0:
        break
    elif opcion==1:
        print("<<<< POKEDEX DE TODOS LOS POKÉMON DISPONEBLES >>>>")#TITULO
        for i in range(1,len(Pokedex)):
            for j in range(len(Pokedex[i])):
                print(f" {Pokedex[0][j]} : {Pokedex[i][j]}")
            print("=========================================")
    elif opcion==2:
        print("<<<< BUSQUEDA DE UN POKÉMON POR NOMBRE >>>>")#TITULO
        pokemon=input("Ingrese el nombre del pokemon que buscar : ").capitalize()
        centinela = False
        for poke in Pokedex:
            if poke[1]==pokemon:
                print("Pokemón encontrado ")
                print("================================")
                print(f"Número: {poke[0]}\nNombre: {poke[1]}\nTipo: {poke[2]}\nAltura (m): {poke[3]}\nPeso (kg): {poke[4]}  ")
                print("================================")
                centinela=True
        if centinela==False:
            print("Pokemón no encontrado")
    elif opcion==3:
        print("<<<< AÑADIR UN POKÉMON AL CINTURÓN >>>>")#TITULO
        pokemon=input("Ingrese el nombre del pokemon : ").capitalize()
        if len(equipo)>=0 and len(equipo)<=5:
            if not pokemon in equipo :
                centinela = False
                for poke in Pokedex:
                    if poke[1]==pokemon:
                        print("Pokemón encontrado ")
                        print("================================")
                        print(f"Número: {poke[0]}\nNombre: {poke[1]}\nTipo: {poke[2]}\nAltura (m): {poke[3]}\nPeso (kg): {poke[4]}  ")
                        print("================================")
                        equipo.append(pokemon)
                        centinela=True
                        print("pokemon añadido ")
                if centinela==False:
                    print("Pokemón no encontrado")
            else:
                print("Pokemon Repetido/ no deben repertirce el pokemon")
        else:
            print("Cinturon lleno ")
    elif opcion==4:
        print("<<<< TÚ EQUIPO POKÉMON >>>>")#TITULO
        for i in range(len(equipo)):
            print(f"{i+1}) {equipo[i]}")
        if len(equipo)==0:
            print("No hay pokemones")
    elif opcion==5:
        print("<<<< QUITAR UN POKÉMON DEL EQUIPO >>>>")#TITULO
        for i in range(len(equipo)):
            print(f"{i+1}) {equipo[i]}")
        Nom= input("Nombre del pokemon que quieras eliminar :  ").capitalize()
        centinela = False
        for p in equipo:
            if p[1] == Nom:
                equipo.remove(p)
                print("Pokemon eliminado")
                centinela =True
                break
        if not centinela:
            print("Pokemon no encontrado")
    elif opcion==6:
        if len(equipo)>0:
            with open ('actividad_15\equipo\cinturón.csv','w',newline='',encoding='utf-8') as a:
                escritura = csv.writer(a,delimiter=',')
                escritura.writerows(equipo)
            print("Reporte generado ")
        else:
            print("No hay pokemones en el cinturon")
    else:
        print("Opccion no valida")