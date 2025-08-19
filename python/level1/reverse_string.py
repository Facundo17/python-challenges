"""
Create as script that can reverse a string in Python
"""
text = "wPython is fun!"

# la forma más fácil. usando string slicing
print(text[::-1])


# mas largo, recorrer el array hasta la mitad
# ir intercambiando el valor de la derecha con el de su opuesto a la izquierda
import math
current = 0
last = len(text) - 1
middle = math.floor(len(text) / 2)

textL = list(text) # convierto el string en una lista

for x in textL:
    if current == middle:
        print("".join(textL)) # junto la lista en un nuevo string
        break
    
    right = textL[current]
    left = textL[last]
    
    textL[current] = left
    textL[last] = right
    
    current += 1
    last -= 1
    