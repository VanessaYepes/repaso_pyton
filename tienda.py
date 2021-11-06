#clase que se llame tienda
#atributos : nombre , apgina web , direccion , lista de productos
from .producto import Producto

class tienda:
    #defino atributos en este bloque
    def __init__(self,nombre,paginaweb,direccion):
        #tiene dos atributos
        self.nombre=nombre
        self.paginaweb=paginaweb
        self.direccion=direccion
        self.listaProductos=[] #creo la lista

#inicializar la tienda  
nombre=input('ingrese el nombre de la tienda:  ')
paginaweb=input('ingese la pagina web: ')
direccion=input('ingrese la direccion de la tienda: ')
tiendacreada=tienda(nombre,paginaweb,direccion)