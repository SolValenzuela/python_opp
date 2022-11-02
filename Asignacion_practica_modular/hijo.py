import padre

class Hijo:
    def __init__(self,email):
        self.email= email
        

user=padre.Usuario("Carlota")
print(user.name)
email=Hijo ("hijo@gamil.com")
print( email.email)

#print(locals())
