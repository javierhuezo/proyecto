# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 19:53:17 2022

@author: ASUS
"""

nombres=[]
apellidos=[]


for x in range(3):
   nom= input("Ingrese el  nombre: ")
   nombres.append(nom)
   
   ape1= input("Ingrese el  primer apellido: ")   
   ape2=input("Ingrese el segundo apellido: ")
   apellidos.append([ape1,ape2])
   print("****************************************")
   
for x in range(3):
    print("Su nombre completo es: ", nombres[x],apellidos[x][0],apellidos[x] [1])