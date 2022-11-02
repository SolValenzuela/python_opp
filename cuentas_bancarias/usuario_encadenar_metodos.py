class Usuario:		#clase
    def __init__(self, name): #constructor
        self.name = name
        self.balance_cuenta = 0

    # método de depósito
    def hacer_deposito(self, monto):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += monto	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return(self) #al agregar return se puede encadenar metodos

    #método de retiro
    def hacer_retiro(self, monto):
        if (self.balance_cuenta- monto < 0):
            print("Saldo insuficiente,intente otro monto")
        else:  # toma un argumento que es el monto del depósito
            self.balance_cuenta -= monto    # la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return(self) #al agregar return se puede encadenar metodos
        
    #metodo que muesta el balance
    def mostrar_balance(self):
        print(f"El balance de la cuenta de {self.name} es {self.balance_cuenta}")
        return(self) #al agregar return se puede encadenar metodos

    #metodo de transferencia
    def transferir_dinero(self, otro_usuario, monto):
        if (self.balance_cuenta- monto < 0):
            print("Saldo insuficiente,intente otro monto")
        else:
            otro_usuario.hacer_deposito(monto)  
            self.hacer_retiro(monto)
            print(f'{self.name} ha realizado una transferencia a otro usuario ') 
        return(self) #al agregar return se puede encadenar metodos


#el primer usuario hace 3 depositos y 1 giro,luego muestra balance
Carlota=Usuario("Carlota")
Homero=Usuario("Homero")
Marge=Usuario("Marge")
Carlota.hacer_deposito(100)
Carlota.hacer_deposito(300)
Carlota.hacer_deposito(300)
Carlota.hacer_retiro(200)
Carlota.transferir_dinero(Marge,200)
Carlota.mostrar_balance()
Carlota.hacer_deposito(1000).hacer_retiro(500).mostrar_balance()



#segundo usuario hace 2 depositos y 2 giros y se muestra balance
Homero.hacer_deposito(500)
Homero.hacer_deposito(500)
Homero.hacer_retiro(200)
Homero.hacer_retiro(200)
Homero.mostrar_balance()
Homero.hacer_deposito(500).hacer_retiro(400).mostrar_balance()


#tercer usuario hace 1 deposito y 3 giros y se muestra balance
Marge.hacer_deposito(1000)
Marge.hacer_retiro(100)
Marge.hacer_retiro(200)
Marge.hacer_retiro(100)
Marge.mostrar_balance()
Marge.hacer_deposito(400).hacer_retiro(300).mostrar_balance()