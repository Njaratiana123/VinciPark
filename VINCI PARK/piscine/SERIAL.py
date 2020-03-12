#!/usr/bin/env python
#-*-coding: utf-8-*-

import serial
ser = serial.Serial('COM4', baudrate=115200, timeout=1)
while 1:

    arduinoData = str(ser.readline())
    arduinoData = arduinoData.split(" ")
    if len(arduinoData) == 4:
        etat = arduinoData[1]
        print("etat : {}".format(etat))
        capteur = arduinoData[3]
        capteur = capteur.split("\\r\\n'")
        capteur = capteur[0]
        print('capteur : {}'.format(capteur))
        print('=============================')
    #print(arduinoData)



