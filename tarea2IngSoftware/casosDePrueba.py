'''
Created on 17/1/2015

@author: Emmanuel De Aguiar 10-10179
         Daniel Pelayo 10-10539
'''
import unittest
from reservacion import reservar, Tarifa
from datetime import datetime


class TestReservar(unittest.TestCase):
    
    def testSameHour(self):
        tarifa = Tarifa(1,2)
        self.assertIsNone(reservar(datetime(2015,4,29,17,30),datetime(2015,4,29,17,30),tarifa), 'Pass')
    def testMinHour(self):
        tarifa = Tarifa(1,2)
        self.assertEqual(reservar(datetime(2015,4,29,10,30),datetime(2015,4,29,10,45),tarifa),1, 'Pass')
    def testTypeDates(self):
        tarifa = Tarifa(1,2)
        self.assertRaises(TypeError,reservar,('fecha en string',['fecha','en','lista'],tarifa))
    def testTarifas(self):
        tarifa = Tarifa(-4,2)
        self.assertRaises(TypeError,reservar,(datetime(2015,4,29,17,30),datetime(2015,4,29,17,15),tarifa))
    def testDifferentMonth(self):
        tarifa = Tarifa(1,2)
        self.assertEqual(reservar(datetime(2015,4,30,23,0),datetime(2015,5,1,0,0),tarifa),2,'Pass')
    def testDifferentDay(self):
        tarifa = Tarifa(1,2)
        self.assertEqual(reservar(datetime(2015,3,20,23,0),datetime(2015,3,21,0,0),tarifa),2,'Pass')
    def testPastDate(self):
        tarifa = Tarifa(1,2)
        self.assertIsNone(reservar(datetime(2015,3,20,23,0),datetime(2015,3,19,0,0),tarifa),'Pass')
    def testCompleteHour(self):
        tarifa = Tarifa(1,2)
        self.assertEqual(reservar(datetime(2015,7,18,3,0),datetime(2015,7,18,4,15),tarifa),4,'Pass')
    def testNotExactHours(self):
        tarifa = Tarifa(1,2)    
        self.assertEqual(reservar(datetime(2015,7,18,3,47),datetime(2015,7,18,4,12),tarifa),2,'Pass')