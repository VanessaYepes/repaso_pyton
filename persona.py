#defio el nombre de la clase 
class Persona():

    #CONTRUCTOR DE UNA CLASE
    def __init__(self,nombre,edad, telefono,documento):  #init es el contractor de la clase
        #atributos de la clase
        self.nombre= nombre #siempre pongo el self.
        self.edad= edad
        self.telefono= telefono
        self.documento=documento

persona1=Persona('vanessa',22,20044004) #creo la persona 
print(persona1.nombre)





