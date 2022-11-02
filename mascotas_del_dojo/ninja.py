from mascotas import Mascota

class Ninja:
# implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
    def __init__(self,nombre, apellido, premios, comida_mascota, mascota):
        self.nombre=nombre
        self.apellido=apellido
        self.premios=premios
        self.comida_gato=comida_mascota
        self.mascota=mascota
        

# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        print(f'{self.nombre} saca a su mascota a caminar')
        self.mascota.jugar()
        return self

# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        print(f'{self.nombre} alimenta a su mascota')
        self.mascota.jugar()
        return self

# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bañar(self):
        print(f'{self.nombre} la baña')
        self.mascota.ruido()
        return self