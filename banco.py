#hacer una clase que se llame cuenta bancatia 
#atributos: a numero de cuenta y yb saldo --> los que van en el init
#metodos : retirar y depositar
import random
from .persona import Persona #importo la clase persona
class CuentaBancaria:
    #defino atributos en este bloque
    def __init__(self,saldo,persona):
        #tiene dos atributos
        self.saldo=saldo
        self.cuenta=random.randint(1000,100000) #numero aleatorio
        self.persona=persona #asocio una persona a la cuenta bancaria

    #metodos retirarm consultar y consignar
    def retirar(self,monto):
        if monto>self.saldo:
            print('fondos insuficientes') #para que no den negativos
        else:
            self.saldo=self.saldo-monto
            print('retiro exitoso')
    
    def ConsultarSaldo(self):
        print('cuenta: ', self.cuenta)
        print('saldo: ', self.saldo)
        print('-------------------------')
    
    def Consignar(self,monto):
        if monto<10000:
            self.saldo=self.saldo + monto
        else:
            comision=monto*4/1000
            self.saldo=self.saldo + monto-comision

#funciones extras para la interfaz
#como esta funcion no esta dentro de la clase no se le pone el parametro self          
def buscarCuentas(mensaje,listaDeCuentas): #entrego el mensaje y la lista 
        numerodecuenta=int(input(mensaje))
        #buscar la cuenta del usuario y cuando se encuentre imprime saldo
        #ALGORITMO DE BUSQUEDA
        for cuenta1 in listaDeCuentas: #recorre la lista de cuentas
            if cuenta1.cuenta==numerodecuenta: #si la cuenta ingredada por el usuario esta el la lista la retorno
                return [True,cuenta1] #retorna v y retorna la cuenta encontrada
            else:
                print('Esta cuenta no existe')
                return False
    
def buscarPersonas(cedula,ListaPersonas):
        for persona in ListaPersonas:
            if persona.documento==cedula:
                return persona
            else:
                return False 



listaDeCuentas=[]
ListaPersonas=[]

while True:
    #para modificar metodos
    operacion=float(input('ingrese 1 si quiere consultar saldo, 2 si quiere retirar y 3 si quiere consignar y 4: para crear una nueva cuenta:'))
    if operacion==1:
        #busco con la funcion buscar cuentas la cuenta bancaria y si esta la retorno 
        busqueda=buscarCuentas('ingrese el numero de cuenta que quiere consultar: ',listaDeCuentas)
        #consulto el saldo asociado  a esa cuenta
        if busqueda[0]==True: #si la busqueda en la posicipm 0 es verdader
            cuenta=busqueda[1] #me retorna la cuenta en esta posicion
            cuenta.ConsultarSaldo() #consultar
        else:
            print('La cuenta no se encuentra registrada')
        
    elif operacion==2:
        busqueda=buscarCuentas('ingrese el numero de cuenta que quiere retirar: ',listaDeCuentas)
        #retornar verdadero si la encontro y falso si no 
        if busqueda[0]==True: #si la busqueda en la posicipm 0 es verdader
            cuenta=busqueda[1] #me retorna la cuenta en esta posicion
            r=float(input('Ingrese el monto que desea retirar: '))
            cuenta.retirar(r)  #me retira el monto pedido
        else: 
            print('La cuenta no se encuentra registrada')

    elif operacion== 3: # en matlaa es sin los dos puntos
        busqueda=buscarCuentas('ingrese el numero de cuenta que quiere consignar: ',listaDeCuentas)
        if busqueda[0]==True: #si la busqueda en la posicipm 0 es verdader
            cuenta=busqueda[1] #me retorna la cuenta en esta posicion
            r=float(input('Ingrese el monto que desea consignar: '))
            cuenta.Consignar(r)  #me consignar el monto pedido
            print('consignacion exitosa')
        else:
            print('La cuenta no se encuentra registrada')

    elif operacion==4:
        saldototal=float(input('Bienvenido al banco .Para crear una cuenta bancaria , ingrese el salgo inicial '))
        cedula=int(input('ingrese el numero de la cedula: '))
        persona_encontrada=buscarPersonas(cedula,ListaPersonas)
        if persona_encontrada==False:
            nombre=input('ingrese el nombre: ')
            edad=int(input('ingese la edad : '))
            telefono=int(input('ingrese el numero telefonico: '))
            nuevapersona=Persona(nombre,edad,telefono,cedula) #creo el objeto
            ListaPersonas.append(nuevapersona) #agrego a la lista personas
            numerocuenta=CuentaBancaria(saldototal,nuevapersona) #creo la cuenta banacaria asociada a la persona
            print('el numero de la cuenta es: ', numerocuenta.cuenta)
            listaDeCuentas.append(numerocuenta)
        else:  #si encontro el usuario  
            numerocuenta=CuentaBancaria(saldototal,persona_encontrada) #creo el numero de cuenta y lo asocio a los datods de la persona encontrada
            print('el numero de la cuenta es: ', numerocuenta.cuenta)
            listaDeCuentas.append(numerocuenta)
    else:
        print('opcion no valida.')
        break
        