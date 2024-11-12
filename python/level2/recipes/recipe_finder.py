import json

ingredients = input("Enter a list of ingredients, separated by commas: ")
recipesIndexes = []

# convertir a array, eliminar espacios en blanco
ingredients = ingredients.split(",")
ingredients = [ x.strip() for x in ingredients]

# leer el archivo de recetas
with open("./recipes.json", "r") as recipes:
    data = json.load(recipes)

# comparar las recetas con los ingredientes
for x in range(len(data)):
    ingInRecipe = data[x]["ingredients"]
    countIn = 0
    
    for y in ingInRecipe:
        if y in ingredients:
            countIn += 1
        
        # tengo todos los ingredientes que necesito
        if countIn == len(ingInRecipe):
            # agrego el índice de la receta
            recipesIndexes.append(x)
            break

# imprimir mensaje
if len(recipesIndexes) > 0:
    print("Here are some recipes you can make:")
    print("")
    for z in recipesIndexes:
        print(f"Recipe: {data[z]["name"]}")
        print(f"Ingredients: {", ".join(data[z]["ingredients"])}")
        print(f"Instructions: {data[z]["instructions"]}")
        print("")
else:
    print("There are no enough ingredients for a recipe.")
    