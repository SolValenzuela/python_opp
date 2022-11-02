class Mascota:
# implementa __init__( name , tipo , golosinas ):
    def __init__(self,name,tipo,golosina):
        self.name=name
        self.tipo=tipo
        self.golosina=golosina
        self.energia=0
        self.salud=0
        
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia=self.energia + 25
        print(f'La mascota {self.name} está durmiendo')
        return self

# comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energia=self.energia + 5
        self.salud=self.salud + 10
        print(f'La mascota {self.name} está comiendo')
        return self

# jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud=self.salud +5
        print(f'La mascota {self.name} está jugando')
        return self

# ruido() - imprime el sonido que produce la mascota
    def ruido(self):
        print(f'La mascota {self.name} dice prrrrr')
    
    def __repr__(self):
        return (f'\n********************************\n{self.name} es su {self.tipo}, su golosina favorita es {self.golosina},\nsu nivel de salud es {self.salud} y su energia está en  {self.energia} \n *****************')