class CuentaBancaria:
    def __init__(self,tasa_interes=0.05,balance=0):
        self.tasa_interes=tasa_interes
        self.balance=balance

        
        
#depósito(self, amount): aumenta el balance de la cuenta en el monto dado
    def deposito(self,monto):
        self.balance += monto
        return(self)
    

# retiro(self, amount): disminuye el balance de la cuenta en el monto dado si hay fondos suficientes; 
# si no hay suficiente dinero, imprime el mensaje: "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
    def retiro(self,monto):
        if (self.balance - monto <=5):
            print(f'Fondos insuficientes:cobrando tarifa $5')            
            self.balance=self.balance - monto -5
        else:
            self.balance -= monto
        return(self)


# mostrar_info_cuenta(self)imprime en la consola: por ejemplo, "Balance: $100"
    def mostrar_info_cuenta(self):
        print(f'El balance es  {self.balance}')


# generar_interés(self): aumenta el balance de la cuenta por el balance actual * la tasa de interés (siempre que el balance sea positivo)
    def generar_interes(self):
        if self.balance >0:
            interes_ganado=self.balance * self.tasa_interes
            print(f'intereses generados {interes_ganado}')
            self.balance= self.balance + interes_ganado
        else:
            print("No hay saldo suficiente")
        return(self)


class Usuario:
    def __init__(self,name):
        self.name=name
        self.cuenta=CuentaBancaria()
    

    def retiro(self,monto):     #metodo actualizado
        self.cuenta.retiro(monto)
        return self
    

    def generar_interes(self):
        self.cuenta.generar_interes()
        return self
    

    def deposito(self,monto):
        self.cuenta.deposito(monto)
        return self


    def mostrar_info_cuenta(self):
        self.cuenta.mostrar_info_cuenta()
        print(f'Mostrando cuenta de {self.name}')
        return(self)
    


sol=Usuario("Sol")
carlota=Usuario("Carlota")
pepito= Usuario("Pepito")

sol.deposito(1000).retiro(100).generar_interes().mostrar_info_cuenta()

carlota.deposito(8000).retiro(900).generar_interes().mostrar_info_cuenta()

pepito.deposito(8999).retiro(799).generar_interes().mostrar_info_cuenta()


