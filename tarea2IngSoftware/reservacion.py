'''
Created on 13/1/2015

@author: Emmanuel De Aguiar 10-10179
         Daniel Pelayo 10-10539
'''
from datetime import datetime
from math import ceil


class Tarifa(object):
    
    def __init__(self,diurna,nocturna):
        self.diurna = diurna
        self.nocturna = nocturna
        pass
    
    def validarTarifa(self):
        if self.diurna > 0 and self.nocturna > 0:
            return True
        else:
            print('Alguna tasa de los turnos es invalida. Recuerde ingresar valores positivos')
            return False    


'''Esta clase permetiria un manejo mas ideal y realista en cuanto a manejar una reservacion como un objeto.
    Sin embargo la tarea enunciaba que hicieramos una funcion y eso fue lo que se hizo.'''        
class Reservacion(object):
    
    def __init__(self,fechaInicial,fechaFinal,tarifa):
        self.fechaInicial = fechaInicial
        self.fechaFinal = fechaFinal
        self.tiempoHospedaje = self.fechaFinal - self.fechaInicial
        self.tarifa = tarifa
        self.status = 'Rechazada'
        if self._validarFechas2() and self.tarifa.validarTarifa():
            self.status = 'Aprobada'
            self._factura()
        else:            
            del(self.fechaInicial)
            del self.fechaFinal
            del self.tiempoHospedaje
            del self.tarifa
            del self.status
            print('Su reservacion no fue creada')
   
    def _validarFechas2(self):
        
        
        tiempoHospedajeMin = (self.tiempoHospedaje.days*24 + (self.tiempoHospedaje.seconds)/3600)*60
        
        if (tiempoHospedajeMin < 15) or (tiempoHospedajeMin > 4320):
            print('Estas fuera del intervalo de reserva. Recuerde que solo puede hospedarse un minimo de 15 minutos y un maximo de 72 horas.')
            return False
        else:
            #print ('Estadia en hotel: %s' %tiempoHospedaje)
            return True
                
    def _factura(self):
        '''Primero se validan las fechas ingresadas:
            -el maximo tiempo de la reservacion es de 72 horas
            -el tiempo minimo de reservacion es de 15 min
           Luego se valida el costo de los turnos diurno y nocturno:
            -verificar que el monto sea positivo
        '''    
        if self.status == 'Aprobada':
        
            '''Una vez validado los datos que se han ingresado procedemos a calcular el costo de la reservacion'''
            horas_a_pagar = self.fechaFinal - self.fechaInicial                            #Duracion de reservacion formato timestamp
            horas_a_pagar = horas_a_pagar.days*24 + (horas_a_pagar.seconds)/3600 #Duracion de Reservacion en horas
            horas_a_pagar = ceil(horas_a_pagar)                                  #Aplicamos funcion Techo a las horas que se cobraran
            
            print()
            
            print('Duracion de su reserva: %s' %self.tiempoHospedaje)
            print('Pagara un total de %s horas:' % horas_a_pagar)
            print('Tasa por Hora turno Diurno:      %s Bs.' %self.tarifa.diurna)
            print('Tasa por Hora turno Nocturno:    %s Bs.' %self.tarifa.nocturna)
            
            '''Para el manejo del cobro de horas se usaran intervalos de hora y su respectivo limite inferior y superior
                -horaI: Limite inferior del intervalo de la hora a cobrar
                -horaS: Limite superior del intervalo de la hora a cobrar
                -minu: Determinara si la hora cruza la frontera entre la tasa del turno diurno y nocturno
                -cobro: Llevara la cuenta del costo de la reservacion'''
            horaI = self.fechaInicial.hour
            minu = self.fechaInicial.minute       
            cobro = 0
            
            '''Inicio Ciclo que calcula el cobro'''
            while horas_a_pagar >  0:
                
                '''Aumento limite superior de la hora'''
                horaS = horaI +1
                if horaS==23:
                    horaS=0
                else:
                    horaS = horaI + 1
                    
                
                if minu > 0:
                    if ((horaI in(18,19,20,21,22,23,0,1,2,3,4,5))or (horaS in(18,19,20,21,22,23,0,1,2,3,4,5))):
                        cobro = cobro + self.tarifa.nocturna   
                    elif (horaI in(6,7,8,9,10,11,12,13,14,15,16,17))and (horaS in(6,7,8,9,10,11,12,13,14,15,16,17)):
                        cobro = cobro + self.tarifa.diurna
                else:
                    if ((horaI ==17)and (horaS ==18)):
                        cobro = cobro + self.tarifa.diurna
                    elif (horaI in(6,7,8,9,10,11,12,13,14,15,16,17))and (horaS in(6,7,8,9,10,11,12,13,14,15,16,17)):
                        cobro = cobro + self.tarifa.diurna
                    elif (horaI in(18,19,20,21,22,23,0,1,2,3,4,5))and (horaS in(18,19,20,21,22,23,0,1,2,3,4,5)):
                        cobro = cobro + self.tarifa.nocturna
                    elif(horaI == 5 and horaS == 6):
                        cobro = cobro + self.tarifa.nocturna
                    
                '''Aumento limite inferior de la hora'''        
                if horaI == 23:
                    horaI = 0
                else:
                    horaI = horaS
                    
                    
                '''Cuenta de Horas que se cobraran'''   
                horas_a_pagar = horas_a_pagar -1
            print('Total a pagar:                  %s Bs.' %cobro)
            return cobro
            '''Fin Ciclo que calcula el cobro'''
        
        else:
            print('No puede consultar su factura. No ha creado una reservacion')


'''Funcion que dado:
    -Una fecha y hora en que comienza una reservacion
    -Una fecha y hora en que termina una reservacion
    -Un objeto tarifa que maneja diferentes tasas
   Calcula y devuelve el monto a pagar por la reservacion'''
def reservar(fechaInicial,fechaFinal,tarifa):
    
    tiempoHospedaje = fechaFinal - fechaInicial #Duracion de reservacion formato timestamp
    print()
    print()
          
    if validarFechas2(fechaInicial,fechaFinal,tiempoHospedaje) and tarifa.validarTarifa():
        
        '''Una vez validado los datos que se han ingresado procedemos a calcular el costo de la reservacion'''
                                    
        horas_a_pagar = tiempoHospedaje.days*24 + (tiempoHospedaje.seconds)/3600 #Duracion de Reservacion en horas
        horas_a_pagar = ceil(horas_a_pagar)                                  #Aplicamos funcion Techo a las horas que se cobraran
            
        print()
            
        print('Duracion de su reserva: %s' %tiempoHospedaje)
        print('Pagara un total de %s horas:' % horas_a_pagar)
        print('Tasa por Hora turno Diurno:      %s Bs.' %tarifa.diurna)
        print('Tasa por Hora turno Nocturno:    %s Bs.' %tarifa.nocturna)
            
        '''Para el manejo del cobro de horas se usaran intervalos de hora y su respectivo limite inferior y superior
                -horaI: Limite inferior del intervalo de la hora a cobrar
                -horaS: Limite superior del intervalo de la hora a cobrar
                -minu: Determinara si la hora cruza la frontera entre la tasa del turno diurno y nocturno
                -cobro: Llevara la cuenta del costo de la reservacion'''
        horaI = fechaInicial.hour
        minu = fechaInicial.minute       
        cobro = 0
        
        if tarifa.diurna > tarifa.nocturna:
            tarifaAcobrar = tarifa.diurna
        elif tarifa.diurna < tarifa.nocturna:
            tarifaAcobrar = tarifa.nocturna
        else:
            tarifaAcobrar = tarifa.diurna
            
        totalDiurnas = 0
        totalNocturnas = 0
        totalMasCaro = 0
            
        '''Inicio Ciclo que calcula el cobro'''
        while horas_a_pagar >  0:
                
            '''Aumento limite superior de la hora'''
            horaS = horaI +1
            if horaS==24:
                horaS=0
            else:
                horaS = horaI + 1
                    
                
            if minu > 0:
                if (horaI == 5) and (horaS == 6):
                    cobro = cobro + tarifaAcobrar
                    totalMasCaro += 1
                elif (horaI == 17) and (horaS == 18):
                    cobro = cobro + tarifaAcobrar 
                    totalMasCaro +=1
                elif (horaI in(6,7,8,9,10,11,12,13,14,15,16,17))and (horaS in(6,7,8,9,10,11,12,13,14,15,16,17)):
                    cobro = cobro + tarifa.diurna
                    totalDiurnas+=1
                elif (horaI in(18,19,20,21,22,23,0,1,2,3,4,5))and (horaS in(18,19,20,21,22,23,0,1,2,3,4,5)):
                    cobro = cobro + tarifa.nocturna
                    totalNocturnas+=1
                else:
                    pass
            else:
                if ((horaI ==17)and (horaS ==18)):
                    cobro = cobro + tarifa.diurna
                    totalMasCaro +=1
                elif(horaI == 5 and horaS == 6):
                    cobro = cobro + tarifa.nocturna
                    totalMasCaro += 1
                elif (horaI in(6,7,8,9,10,11,12,13,14,15,16,17))and (horaS in(6,7,8,9,10,11,12,13,14,15,16,17)):
                    cobro = cobro +tarifa.diurna
                    totalDiurnas +=1
                elif (horaI in(18,19,20,21,22,23,0,1,2,3,4,5))and (horaS in(18,19,20,21,22,23,0,1,2,3,4,5)):
                    cobro = cobro + tarifa.nocturna
                    totalNocturnas +=1
                
                    
            '''Aumento limite inferior de la hora'''        
            if horaI == 23:
                horaI = 0
            else:
                horaI = horaS
                    
                    
            '''Cuenta de Horas que se cobraran'''   
            horas_a_pagar = horas_a_pagar -1
        print('Total a pagar:                  %s Bs.' %cobro)
        print('Total Horas nocturnas: %s, Total Horas Diurnas: %s, Total cruce de turnos: %s' %(totalNocturnas,totalDiurnas,totalMasCaro))
        return cobro
        '''Fin Ciclo que calcula el cobro'''
        
    else:
        print('No puede consultar su factura. No ha creado una reservacion')
        return None

'''Funcion que dado:
    -Fecha y hora inicial
    -Fecha y hora Final
    -tiempo total de la reservacion(fecha inicial - fecha final)
   Determina si la reservacion es valida'''  
def validarFechas2(fechaInicial,fechaFinal,tiempoHospedaje):
        
    
    tiempoHospedajeMin = (tiempoHospedaje.days*24 + (tiempoHospedaje.seconds)/3600)*60
        
    if (tiempoHospedajeMin < 15) or (tiempoHospedajeMin > 4320):
        print('Estas fuera del intervalo de reserva. Recuerde que solo puede hospedarse un minimo de 15 minutos y un maximo de 72 horas.')
        return False
    else:
        return True
      
"""fi=datetime(2015,4,29,17,30)
ff=datetime(2015,4,30,17,45)"""

horainicial = "2015 12 29 18:00"
horafinal = "2016 1 1 18:00"

fi = datetime.strptime(horainicial, "%Y %m %d %H:%M")
ff = datetime.strptime(horafinal, "%Y %m %d %H:%M")


miTarifa = Tarifa(2,1)
reservar(fi, ff, miTarifa)