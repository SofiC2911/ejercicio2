# -*- coding: utf-8 -*-
from ClaseViajero import claseVia
#from ClaseManejadorViaj import ManejadorViaj

class Menu: 
    #__switcher=None
    def __init__(self):
        self.__switcher = {1:self.opcion1,
                           2:self.opcion2,
                           3:self.opcion3,
                           4:self.salir
                           }
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self,op,obV):
        if (type(obV) == claseVia) and (type(op) == int):
            func=self.__switcher.get(op, lambda: print("Opción no válida"))
            func(obV)
        else:
            print('Parametros de tipo incorrecto')
        
    def salir(self,obV):
        print('Salir')
        
    def opcion1(self,obV):
        if type(obV) == claseVia:
            cant = obV.cantidadTotaldeMillas()
            print('las cantidad de millas recorridas es de: ',cant)
        else:
            print('error en opcion 1')
        
    def opcion2(self, obV):
        if type(obV) == claseVia:
            cantMi = int(input('Ingrese cantidad de millas a acumular: '))
            obV.acumularMillas(cantMi)
    
    def opcion3(self, obV):
        if type(obV) == claseVia:
            cantCan = int(input('Ingrese cantidad de millas a canjear: '))
            obV.canjearMillas(cantCan)