import typing

class Ingredient:
    def __init__(self):
        self.name:Str = input("Ingrediente: ")
        self.unidad:Str = input("Introduce las unidades en las que se mide 'pza','rebanada':")


class Recipe:
    def __init__(self, name:Str, ingredients:List(Str), quantities:List(Float)):
        self.name = name
        self.ingredients = ingredients
        self.quantities = quantities
        self.lista_Ingredientes = []
        for i in range(len(self.ingredients)):
            self.lista_Ingredientes.append(self.ingredients[i].name)

    def prepare_recipe(self):
        preparation = float(input("Que cantidad de receta deseas preparar?: "))
        print("Para preparar ", preparation, " tantos de ", self.title, " necesitas los siguientes ingredientes:")
        for i in range(len(self.ingredients)):
            print(self.ingredients[i].name + ": ", float(self.quantities[i]) * preparation, self.ingredients[i].unidad)
        print("Listo! La receta está preparada.")

def crearReceta():
    ingredientes, cantidades = [], []
    nombreReceta = input("¿Cual es el nombre de la receta?: ")
    num_Ingredientes = input("Cuántos ingredientes tiene la receta?: ")
    for i in range(int(num_Ingredientes)):
        ingrediente = Ingredient()
        ingredientes.append(ingrediente)
        cantidades.append(input("Cantidad: "))
    receta = Recipe(nombreReceta, ingredientes, cantidades)
    print(receta.lista_Ingredientes)
    print(receta.quantities)
    receta.prepare_recipe()

i=1
while i==1:
    crearReceta()
    i=int(input("¿Continuar con las recetas? 1. Si 2. No: "))
    print("Que disfrutes tu comida! Yummy!")

