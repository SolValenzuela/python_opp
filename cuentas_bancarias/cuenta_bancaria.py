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
        print(f'Balance:{self.balance}')


# generar_interés(self): aumenta el balance de la cuenta por el balance actual * la tasa de interés (siempre que el balance sea positivo)
    def generar_interes(self):
        if self.balance >0:
            interes_ganado=self.balance * self.tasa_interes
            print(f'intereses generados {interes_ganado}')
            self.balance= self.balance + interes_ganado
        else:
            print("No hay saldo suficiente")
        return(self)


cuenta1=CuentaBancaria()
cuenta1.deposito(1000).retiro(200).generar_interes().mostrar_info_cuenta()

cuenta2=CuentaBancaria()
cuenta2.deposito(3000).retiro(1000).retiro(1050).retiro(950).mostrar_info_cuenta()

