# -*- coding: utf-8 -*-
from ClaseManejadorViaj import ManejadorViaj

from ClaseMenu import Menu


if  __name__  ==  '__main__' :
    
    ListManejador = ManejadorViaj()
    
    ListManejador.CargarList()
    
    menu = Menu()
    
    print(ListManejador)

    numViajeroF = int(input('Ingrese numero de viajero frecuente: '))
    while numViajeroF>0:
        indice = ListManejador.BuscarIndice(numViajeroF)
        unViajero = ListManejador.BuscarViajero(indice)
        
        if indice == -1:
            print('el numero ingresado no corresponde a ningun viajero frecuente')
        else:
            salir = False
            while not salir:
                print("---------------- MENU --------------")
                print('1 - Consultar cantidad de millas \n2 - Acumular millas \n3 - Canjear millas \n4 - Salir')
                op = int(input('Ingrese opcion: '))
                menu.opcion(op,unViajero)
                salir = op == 4
    
        numViajeroF = int(input('Ingrese numero de viajero frecuente, ingreso finaliza con -1: '))