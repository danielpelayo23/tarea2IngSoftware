'''
Created on 17/1/2015

@author: Emmanuel De Aguiar 10-10179
         Daniel Pelayo 10-10539
'''
import unittest
from reservacion import reservar, Tarifa
from datetime import datetime


class TestReservar(unittest.TestCase):
    def testNotValidMinHour(self):
        tarifa = Tarifa(1,2)
        self.assertIsNone(reservar(datetime(2015,4,29,17,30),datetime(2015,4,29,17,44),tarifa), 'Pass')
    def testNotValidMaxHour(self):
        tarifa = Tarifa(1,2)
        self.assertIsNone(reservar(datetime(2015,6,2,2,0),datetime(2015,6,5,2,1),tarifa), 'Pass')
    def testDifferentYear(self):
        tarifa = Tarifa(1,2)
        self.assertEqual(reservar(datetime(2015,12,31,23,0),datetime(2016,1,1,0,0),tarifa),2,'Pass')
    def testDifferentTax1(self):
        tarifa = Tarifa(1,2)
        self.assertEqual(reservar(datetime(2015,12,2,17,0),datetime(2015,12,2,19,0),tarifa),3,'Pass')
    def testDifferentTax2(self):
        tarifa = Tarifa(1,2)
        self.assertEqual(reservar(datetime(2015,12,2,5,0),datetime(2015,12,2,7,0),tarifa),3,'Pass')
    def testMinCostMinReservation(self):
        tarifa = Tarifa(1,10)
        self.assertEqual(reservar(datetime(2015,12,2,7,0),datetime(2015,12,2,7,15),tarifa), 1, 'Pass')
    def testMaxCostMinReservation(self):
        tarifa = Tarifa(1,10)
        self.assertEqual(reservar(datetime(2015,12,2,18,0),datetime(2015,12,2,18,15),tarifa),10, 'Pass')
    def testMinCostMaxReservation(self):
        tarifa = Tarifa(1,10)
        self.assertEqual(reservar(datetime(2015,12,2,7,0),datetime(2015,12,5,7,0),tarifa), 396, 'Pass')
    def testMaxCostMaxReservation(self):
        tarifa = Tarifa(1,10)
        self.assertEqual(reservar(datetime(2015,12,2,7,30),datetime(2015,12,5,7,0),tarifa), 423, 'Pass')