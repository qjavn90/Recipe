import copy
class Ingredient:
    def __init__(self, name:str='', unidad:str=''):
        self.name:str = name
        self.unidad:str = unidad

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Ingrediente: {self.name}'

    def crearIngrediente(self):
        self.name = input("Ingrediente: ")
        self.unidad=input("Introduce las unidades en las que se mide 'pza','rebanada':")
        return self
class Recipe:

    def __init__(self, name='', ingredients=None, quantities=None):
        self.name = name
        if quantities is None:
            self.quantities = []
        else:
            self.ingredients = ingredients
        if ingredients is None:
            self.ingredients = []
        else:
            self.quantities=quantities

    def __str__(self):
        return f' Nombre de la receta: {self.name}.'

    def __repr__(self):
        return self.__str__()

    def crearReceta(self):
        self.name = input("¿Cual es el nombre de la receta?: ")
        num_Ingredientes = input("Cuántos ingredientes tiene la receta?: ")
        self.ingredients=[]
        ingrediente = Ingredient()
        for i in range(int(num_Ingredientes)):
            ingrediente=ingrediente.crearIngrediente()
            self.ingredients.append(copy.copy(ingrediente))
            self.quantities.append(input("Cantidad: "))
        return self

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
    def __init__(self, name='', author='', listaRecetas=None):
        self.name=name
        self.author=author
        if listaRecetas is None:
            self.listaRecetas = []
        else:
            self.listaRecetas=listaRecetas
    def __str__(self):
        return f' Título del recetario: {self.name}. Autor del recetario: {self.author}'

    def crearRecetario(self):
        self.name = input("Introduce el nombre del Recetario: ")
        self.author = input("Introduce el autor del Recetario:")
        receta = Recipe()
        i = 1
        while i==1:
            receta.crearReceta()
            self.listaRecetas.append(copy.copy(receta))
            i=int(input("¿Continuar con las recetas? 1. Si 2. No: "))
        return self

    def imprimeRecetario(self):
        print(self)
        for i in range(len(self.listaRecetas)):
            self.listaRecetas[i].imprimeReceta()

########################################################################################
#PRUEBAS
###Crear un ingrediente
###Podemos crear un ingrediente cuyos argumentos estén vacios

#ingrediente=Ingredient()
#print(ingrediente)

###Podemos crear un ingrediente con los argumentos que queramos
#ingrediente=Ingredient('Huevos','pza')
#print(ingrediente)
#print(ingrediente.name)
#print(ingrediente.unidad)

###Podemos modificar las propiedades del ingrediente, usando la funcion 'crearIngrediente'
#ingrediente=Ingredient()
#ingrediente.crearIngrediente()
#print(ingrediente)
#print(ingrediente.name)
#print(ingrediente.unidad)

###Crear una receta
#Podemos crear una receta vacía
#receta=Recipe()
#print(receta)

#Podemos crear una receta con los argumentos
#nombreReceta='Huevos al gusto'
#ingredientes=['Huevos']
#cantidades=[2]
#receta=Recipe(nombreReceta,ingredientes,cantidades)
#print(receta.ingredients)
#receta.imprimeReceta()

#huevo=Ingredient('Huevos','pza')
#ingredientes=[huevo]
#receta=Recipe(nombreReceta,ingredientes,cantidades)
#print(receta.ingredients)
#receta.imprimeReceta()

#Podemos crear una receta utilizando, la función 'crearReceta()'
#receta=Recipe()
#receta.crearReceta()
#receta.imprimeReceta()
#print(receta.ingredients)

###Crear un recetario
#recetario=RecipeBook()
#recetario.crearRecetario()
#recetario.imprimeRecetario()
#print(recetario.listaRecetas)
#print(recetario.listaRecetas[0])