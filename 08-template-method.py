# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:49:15 2015

@author: dankow01
"""

class CaffeineBeverage():
    def __init__(self):
        pass
    
    # Template method
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiment()
    
    def boilWater(self):
        print('Boiling water')
        
    def pourInCup(self):
        print('Pouring in cup')
    
    def brew(self):
        pass
    
    def addCondiment(self):
        pass


class Coffee(CaffeineBeverage):
    def brew(self):
        print('Putting grind in coffee pot')
        
    def addCondiment(self):
        print('Adding milk and sugar')


class Tea(CaffeineBeverage):
    def brew(self):
        print('Putting tea leaves in pot')
        
    def addCondiment(self):
        print('Adding lemon and honey')

