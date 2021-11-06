import random
class Producto():
    def __init__(self,nombre,precio):
        #tiene dos atributos
        self.nombre=nombre
        self.precio=precio
        self.referencia= 'REF'+ str(random.randint(100,10000))
        self.inventario=(0,100)
