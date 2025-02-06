class Vehiculo: 
    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
    
    def acelerar(self, incremento):
        self.velocidad += incremento
    
    def frenar(self, decremento):
        self.velocidad += decremento
   
    def get_velocidad(self):
        return self.velocidad 
    
    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {} ,Velocidad: {}".format(self.marca ,self.modelo ,self.color ,self.velocidad)
    
abeo = Vehiculo("Chevrolet","Abeo","Plateado")
print (abeo.show_attr())