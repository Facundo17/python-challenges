import random

with open("names.txt", "r") as names:
    
    lines = names.readlines() # esto carga toda la lista en memoria
    
    listNames = list(lines) # lo convierto en una lista
    
    name = random.choice(listNames) # con la función random, selecciono un valor aleatorio dentro de una sequencia (list, tupple o string)
    
    # nota: tener en cuenta que los nombres se están devolviendo con "\n" al final
    print(f"Randomly selected name: {name}")