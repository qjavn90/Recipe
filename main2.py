import typing

class Ingredient:
    def __init__(self):
        self.name:Str = input("Ingrediente: ")
        self.unidad:Str = input("Introduce las unidades en las que se mide 'pza','rebanada':")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Ingrediente: {self.name}'

class Recipe:
    def __init__(self, name:str, ingredients:list, quantities:list):
        self.name = name
        self.ingredients = ingredients
        self.quantities = quantities

    def __str__(self):
        return f' Nombre de la receta: {self.name}.'

    def __repr__(self):
        return self.__str__()

    def prepare_recipe(self):
        preparation = float(input("Que cantidad de receta deseas preparar?: "))
        print("Para preparar ", preparation, " tantos de ", self.name, " necesitas los siguientes ingredientes:")
        for i in range(len(self.ingredients)):
            print(self.ingredients[i].name + ": ", float(self.quantities[i]) * preparation, self.ingredients[i].unidad)
        print("Listo! La receta está preparada.")

    def imprimeReceta(self):
        print("Receta:", self.name)
        for i in range(len(self.ingredients)):
            print("Ingrediente: ", self.ingredients[i], "Cantidad: ", self.quantities[i])
class RecipeBook:
    def __init__(self):
        self.name=input("Introduce el nombre del Recetario: ")
        self.author=input("Introduce el autor del Recetario:")

    def __str__(self):
        return f' Título del recetario: {self.name}. Autor del recetario: {self.author}'

    def crearReceta(self):
        ingredientes, cantidades = [], []
        nombreReceta = input("¿Cual es el nombre de la receta?: ")
        num_Ingredientes = input("Cuántos ingredientes tiene la receta?: ")
        for i in range(int(num_Ingredientes)):
            ingrediente = Ingredient()
            ingredientes.append(ingrediente)
            cantidades.append(input("Cantidad: "))
        receta = Recipe(nombreReceta, ingredientes, cantidades)
        print(receta.ingredients)
        print(receta.quantities)
        return receta

    def crearRecetario(self):
        self.listaRecetas=[]
        i=1
        while i==1:
            receta=self.crearReceta()
            self.listaRecetas.append(receta)
            i=int(input("¿Continuar con las recetas? 1. Si 2. No: "))
        return self.listaRecetas

########################################################################################
#PRUEBAS

###Crear una receta
ingredientes=["Huevos"]
cantidades=[2]
receta=Recipe("Huevos al Gusto",ingredientes,cantidades)
receta.imprimeReceta()

recetario=RecipeBook()
recetario.crearRecetario()
print(recetario)
print(recetario.listaRecetas)
print(recetario.listaRecetas[0].imprimeReceta())

