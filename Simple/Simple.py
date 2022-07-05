import random


def Simple():
    
    diccionario = {}
    for i in range(1,11):   
        edad = random.randint (0,101)    
        diccionario[i] = edad 
    return diccionario

print(Simple())

