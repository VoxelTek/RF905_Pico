'''
Created on 2013-6-20

@author: hackeen
'''
#import spi

import machine
import utime
#from time import sleep
#import RPi.GPIO as GPIO

class RF905:
    #CSN = 24
    #DR  = 7
    #AM  = 15
    #CD  = 13
    #PWR = 11
    #TRX_CE = 12
    #TXEN = 8

    def __init__(self,csn,dr,am,cd,pwr,trx_ce,txen):
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setwarnings(False)
        ###CSN_PIN = csn
        ###DR_PIN  = dr
        ###AM_PIN  = am
        ###CD_PIN  = cd
        ###PWR_PIN = pwr
        ###TRX_CE_PIN = trx_ce
        ###TXEN_PIN = txen

        #GPIO.setup(CSN,GPIO.OUT)
        #GPIO.output(CSN,GPIO.HIGH)
        CSN = machine.Pin(csn, machine.Pin.OUT)
        CSN.value(1)
        #GPIO.setup(DR,GPIO.IN)
        DR = machine.Pin(dr, machine.Pin.IN)
        #GPIO.setup(AM,GPIO.IN)
        AM = machine.Pin(am, machine.Pin.IN)
        #GPIO.setup(CD,GPIO.IN)
        CD = machine.Pin(cd, machine.Pin.IN)
        #GPIO.setup(PWR,GPIO.OUT)
        #GPIO.output(PWR,GPIO.HIGH)
        PWR = machine.Pin(pwr, machine.Pin.OUT)
        PWR.value(1)
        #GPIO.setup(TRX_CE,GPIO.OUT)
        #GPIO.output(TRX_CE,GPIO.LOW)
        TRX_CE = machine.Pin(trx_ce, machine.Pin.OUT)
        TRX_CE.value(0)
        #GPIO.setup(TXEN,GPIO.OUT)
        #GPIO.output(TXEN,GPIO.LOW)
        TXEN = machine.Pin(txen, machine.Pin.OUT)
        TXEN.value(0)
        
    def openSPI(self):
        #spi.openSPI(speed=106000)
        spi = machine.SPI(0, 106000)
        
    def writeconfig(self,address1,address2,address3,address4):
        #self.openSPI()
        #GPIO.output(self.CSN,GPIO.LOW)
        CSN.value(0)
        #spi.transfer((0x00,))
        spi.write((0x00,))
        #spi.transfer((0x4C,))
        spi.write((0x4C,))
        #spi.transfer((0x0C,))
        spi.write((0x0C,))
        #spi.transfer((0x44,))
        spi.write((0x44,))
        #spi.transfer((0x20,))
        spi.write((0x20,))
        #spi.transfer((0x20,))
        spi.write((0x20,))
        #spi.transfer((address1,))
        spi.write((address1,))
        #spi.transfer((address2,))
        spi.write((address2,))
        #spi.transfer((address3,))
        spi.write((address3,))
        #spi.transfer((address4,))
        spi.write((address4,))
        #spi.transfer((0x58,))
        spi.write((0x58,))
        #GPIO.output(self.CSN,GPIO.HIGH)
        CSN.value(1)
        #spi.closeSPI()
        
    def sendstr(self,content,address1,address2,address3,address4): 
        #self.openSPI()
        ##SetTx
        #GPIO.output(self.TRX_CE,GPIO.LOW)
        TRX_CE.value(0)
        #GPIO.output(self.TXEN,GPIO.HIGH)
        TXEN.value(1)
        
        utime.sleep(0.01)
        #GPIO.output(self.CSN,GPIO.LOW)
        CSN.value(0)
        #spi.transfer((0x20,))
        spi.write((0x20,))
        for i in range(32):
            a = 32
            if i < len(content):
                a = ord(content[i])           
            #spi.transfer((a,))
            spi.write((a,))
        #GPIO.output(self.CSN,GPIO.HIGH)
        CSN.value(1)
        #sleep(0.01)
        utime.sleep(0.01)
        #GPIO.output(self.CSN,GPIO.LOW)
        CSN.value(0)
        #spi.transfer((0x22,))
        spi.write((0x22,))
        #spi.transfer((address1,))
        spi.write((address1,))
        #spi.transfer((address2,))
        spi.write((address2,))
        #spi.transfer((address3,))
        spi.write((address3,))
        #spi.transfer((address4,))
        spi.write((address4,))
        #GPIO.output(self.CSN,GPIO.HIGH)
        CSN.value(1)
     
        #GPIO.output(self.TRX_CE,GPIO.HIGH)
        TRX_CE.value(1)
        utime.sleep(0.01)
        #GPIO.output(self.TRX_CE,GPIO.LOW)
        TRX_CE.value(0)
        #spi.closeSPI()
        
    def listen(self,callback):
        #self.openSPI()
        ##SetRx
        #GPIO.output(self.TXEN,GPIO.LOW)
        TXEN.value(0)
        #GPIO.output(self.TRX_CE,GPIO.HIGH)
        TRX_CE.value(1)
             
        while 1==1:    
            #while GPIO.input(self.DR) == GPIO.LOW:
            while DR.value() == 0:
                a=10
        
            #GPIO.output(self.TRX_CE,GPIO.LOW)
            TRX_CE.value(0)
            #GPIO.output(self.CSN,GPIO.LOW)
            CSN.value(0)
            #spi.transfer((0x24,))
            spi.write((0x24,))
            data = ""
            for x in range(32):
                #data = data+chr(spi.transfer((0x00,))[0])
                data = data+chr(spi.transfer((0x00,))[0])
            ##print("2:"+data)
            #callback(data)
            #GPIO.output(self.CSN,GPIO.HIGH)
            CSN.value(1)
            #GPIO.output(self.TRX_CE,GPIO.HIGH)
            TRX_CE.value(1)

            utime.sleep(0.01)
            
        
        #spi.closeSPI()

        
