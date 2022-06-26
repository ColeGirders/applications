from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import math
import PySimpleGUI as sg
import time
import pandas as pd
import subprocess
import webbrowser
import ctypes
from datetime import datetime
import os
import urllib.request
import keyboard
from decimal import Decimal



font1='Arial 14'

input1t=''
input2t=''
i12=1
coperator='none'
calculation=""

numbers=['.',0,1,2,3,4,5,6,7,8,9]
operators=['/','*','-','+']

layout=[[sg.Text("",key='input1',size=(20,1),background_color='white',text_color='black'),
        sg.Text("",key='operator',size=(1,1),text_color='black')],
        [sg.Text("",key='input2',size=(20,1),background_color='white',text_color='black')],
        [sg.Text("",key='output',size=(20,1),background_color='white',text_color='black')],
        [sg.Button("Clear",key='clear',font=font1,size=(5,2)),
         sg.Button("/",key='/',font=font1,size=(5,2)),
         sg.Button("*",key='*',font=font1,size=(5,2)),
         sg.Button("-",key='-',font=font1,size=(5,2))],
        [sg.Button("7",key='7',font=font1,size=(5,2)),
         sg.Button("8",key='8',font=font1,size=(5,2)),
         sg.Button("9",key='9',font=font1,size=(5,2)),
         sg.Button("+",key='+',font=font1,size=(5,2))],
        [sg.Button("4",key='4',font=font1,size=(5,2)),
         sg.Button("5",key='5',font=font1,size=(5,2)),
         sg.Button("6",key='6',font=font1,size=(5,2))],
        [sg.Button("1",key='1',font=font1,size=(5,2)),
         sg.Button("2",key='2',font=font1,size=(5,2)),
         sg.Button("3",key='3',font=font1,size=(5,2)),
         sg.Button("=",key='=',font=font1,size=(5,2))],
        [sg.Button("0",key='0',font=font1,size=(12,2)),
         sg.Button(".",key='.',font=font1,size=(5,2))],
        [sg.Text("")],
        [sg.Button("Exit")]]


#window=sg.Window("Calculator", layout, icon='nexus.ico', size=(320,420),finalize=True)
window=sg.Window("Calculator", layout, size=(320,420),finalize=True)


while True:
    event, values = window.read()
    print(event)

    if (event=='clear'):
        input1t=''
        input2t=''
        i12=1
        coperator='none'
        calculation=""
        window['input1'].update(input1t)
        window['input2'].update(input2t)
        window['operator'].update("")
        window['output'].update("")

    if (event=='='):
        if (input2t!=""):
            if (calculation!="" and calculation!='Missing second argument'):
                window['input1'].update(calculation)
                
                if (coperator=='+'):
                    calculation=Decimal(calculation)+Decimal(input2t)
                elif (coperator=='-'):
                    calculation=Decimal(calculation)-Decimal(input2t)
                elif (coperator=='*'):
                    calculation=Decimal(calculation)*Decimal(input2t)
                elif (coperator=='/'):
                    calculation=Decimal(calculation)/Decimal(input2t)
                elif (coperator=='none'):
                    calculation=Decimal(input1t)

                window['output'].update(calculation)
            else:
                if (coperator=='+'):
                    calculation=Decimal(input1t)+Decimal(input2t)
                elif (coperator=='-'):
                    calculation=Decimal(input1t)-Decimal(input2t)
                elif (coperator=='*'):
                    calculation=Decimal(input1t)*Decimal(input2t)
                elif (coperator=='/'):
                    calculation=Decimal(input1t)/Decimal(input2t)
                elif (coperator=='none'):
                    calculation=Decimal(input1t)
                
            
        elif (input2t==""):
            if (coperator=='none'):
                calculation=Decimal(input1t)
            else:
                calculation="Missing second argument"
         
                
        window['output'].update(calculation)

    if (event in str(operators)):
        window['operator'].update(event)
        i12=2
        coperator=event
        event=""
        if (input2t!=""):
            input1t=calculation
            input2t=""
            calculation=""
            window['input1'].update(input1t)
            window['input2'].update(input2t)
            window['output'].update("")

        
        
    if (i12==1):
        if (event in str(numbers)):
            input1t+=event
            window['input1'].update(input1t)
    
    if (i12==2):
        if (event in str(numbers)):
            input2t+=event
            window['input2'].update(input2t)
    
        
    if (event=="Exit" or event == sg.WIN_CLOSED):
        break


window.close()





