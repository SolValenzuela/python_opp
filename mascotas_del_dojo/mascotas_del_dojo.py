from ninja import Ninja
from mascotas import Mascota

name=Mascota('Lola','gata','galleta')
print(name)

# Crea una instancia de un Ninja y asígnale una instancia de mascota al atributo de mascota.
ninja1=Ninja('Ninja','1','galleta','pellet',name)
print(ninja1)


# Haz que el ninja alimente, pasee y bañe a su mascota.
ninja1.alimentar().caminar().bañar()


name.dormir().jugar().dormir()
print(name)





