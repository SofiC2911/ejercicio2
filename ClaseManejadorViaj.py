# -*- coding: utf-8 -*-
import csv
from ClaseViajero import claseVia

class ManejadorViaj:
    
    __listaViaj = []
    
    def __init__(self):    #inicializa las variables
        self.__listaViaj = []
        
    def __str__(self):      #muestra informacion de la lista
        s = ""
        for ObjViaj in self.__listaViaj:
            s += str(ObjViaj) + '\n'
        return s
    
    def CargarList(self):
        arch = open('registroViajeros.csv')
        reader = csv.reader(arch,delimiter=';')
        
        b = True
        for i in reader:
            if b:
                b = not b
            else:
                numV = int(i[0])
                dni = i[1]
                nom = i[2]
                ape = i[3]
                millasA = int(i[4])
                unViajero = claseVia(numV,dni,nom,ape,millasA)
                self.__listaViaj.append(unViajero)
    
        arch.close()

    def BuscarIndice(self, numV):
        if type(numV) == int: 
            indice = -1
            for i, ObjViaj in (enumerate(self.__listaViaj)):
                if ObjViaj.getIdViaj() == numV:
                    indice = i
            return indice
        else:
            print('Parametro de tipo incorrecto')
    
    def BuscarViajero(self,indice):
        if type(indice) == int:
            viajero = self.__listaViaj[indice]
            return viajero
        else:
            print('Parametro de tipo incorrecto')
    
    def agregar(self,v):
        self.__listaViaj.append(v)
        