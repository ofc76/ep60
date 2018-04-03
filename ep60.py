#!/usr/bin/python3
# -*- coding: utf-8 -*-

import serial, time 

DEVICE_PORT = '/dev/ttyEP60'
DEVICE_SPEED = 57600

ESC = 0x1b
BOLD = 0x47
CUT = 0x69
LF = 0x0a      # print end feed
CR = 0x0d      # print, N.B. This command is ignored.
STATUS = 0x76
BEEP = 0x07

HEAD0 = 'Название организации'
HEAD1 = ''
HEAD2 = '      адрес'
FOOTER0 = '------------------------------------'
FOOTER1 = '          чек не фискальный  '
FOOTER2 = '            Вдалої поїздки  '

class Ep60:
        
    bold = False
    state = 0

    def __init__(self):
        ser = serial.Serial()
        ser.baudrate = DEVICE_SPEED
        ser.port = DEVICE_PORT 
        ser.timeout = 0.1
        ser.close()
        ser.open()   
        self.printer = ser

    def utf_to_866bytes(self, txt):
        with open('/tmp/prn.txt', 'w', encoding='cp866') as f:
            f.write(txt.replace('і','i').replace('І','I'))
        with open('/tmp/prn.txt', 'rb') as f:
            arr = f.read()
        return arr

    def print_bold(self, txt):
        arr = self.utf_to_866bytes(txt)
        str_prn = bytearray()
        str_prn.append(ESC)
        str_prn.append(BOLD)
        str_prn.append(1)
        str_prn.extend(arr)
        str_prn.append(ESC)
        str_prn.append(BOLD)
        str_prn.append(0)
        self.printer.write(str_prn)


    def print_txt(self, txt):
        arr = self.utf_to_866bytes(txt)
        str_prn = bytearray()
        str_prn.extend(arr)
        self.printer.write(str_prn)


    def cut(self):
        str_prn = bytearray()
        str_prn.append(ESC)
        str_prn.append(CUT)
        self.printer.write(str_prn)
   
    def LF(self):
        str_prn = bytearray()
        str_prn.append(LF)
        self.printer.write(str_prn)


    def status(self):
        str_prn = bytearray()
        str_prn.append(ESC)
        str_prn.append(CUT)
        self.printer.write(str_prn)
        time.sleep(0.5)
        state = self.printer.read(1) 
        return state


    def head(self):
        if not HEAD0 == '':
            str_prn = bytearray()
            arr = self.utf_to_866bytes(HEAD0)
            str_prn.extend(arr)
            self.printer.write(str_prn)
            self.LF()
        if not HEAD1 == '':
            str_prn = bytearray()
            arr = self.utf_to_866bytes(HEAD1)
            str_prn.extend(arr)
            self.printer.write(str_prn)
            self.LF()
        if not HEAD2 == '':
            str_prn = bytearray()
            arr = self.utf_to_866bytes(HEAD2)
            str_prn.extend(arr)
            self.printer.write(str_prn)
            self.LF()

    def footer(self):
        if not FOOTER0 == '':
            str_prn = bytearray()
            arr = self.utf_to_866bytes(FOOTER0)
            str_prn.extend(arr)
            self.printer.write(str_prn)
            self.LF()
        if not FOOTER1 == '':
            str_prn = bytearray()
            arr = self.utf_to_866bytes(FOOTER1)
            str_prn.extend(arr)
            self.printer.write(str_prn)
            self.LF()
        if not FOOTER2 == '':
            str_prn = bytearray()
            arr = self.utf_to_866bytes(FOOTER2)
            str_prn.extend(arr)
            self.printer.write(str_prn)
            self.LF()
        self.cut()
        
'''     
    
ser.write(my_bytes_2)
time.sleep(0.5)
bytes = ser.read(32)  
print (bytes)      
    
ser.write(my_bytes_3)
time.sleep(0.5)
bytes = ser.read(2)  
print (bytes)      
    
ser.write(my_bytes_4)
time.sleep(0.5)
bytes = ser.read(1)  
print (bytes)    
'''
    






