# -*- coding: utf-8 -*-
class claseVia:
    __numViajero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millaAcum = 0
    
    def __init__(self,numViajero,dni,nom,apellido,milla):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apellido
        self.__millaAcum = milla
    
    def cantidadTotaldeMillas(self):
        print('estoy dentro de cantMilla')
        return self.__millaAcum
    
    def acumularMillas(self,cantM):
        if type(cantM) == int:
            print('millas antes de acumular: ',self.__millaAcum)
            self.__millaAcum +=cantM
            print('millas despues de acumular: ',self.__millaAcum)
        else:
            print('error de tipo de cantidad de millas')
    
    def canjearMillas(self,cantCanj):
        if type(cantCanj) == int:
            if cantCanj <= self.__millaAcum:
                print('millas antes de restar: ',self.__millaAcum)
                self.__millaAcum -= cantCanj
                print('millas despues de restar: ',self.__millaAcum)
                print('Sus millas fueron canjeadas con exito')
            else:
                print('Sus millas no son suficientes para el canje') 
            
    def __str__(self):
        return ('num viajero: {} dni: {} nombre: {} apellido: {} millas: {}'.format(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millaAcum))
        
            
    def getIdViaj(self):
        return self.__numViajero
    
    