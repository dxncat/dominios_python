class Carro():
    #crear el metodo construcctor
    def __init__(self, placa, tipo_vehiculo):
        self.placa = placa
        self.tipo_vehiculo = tipo_vehiculo

class Cliente():
    def __init__(self, nombre, documento, celular, lista_carros):
        self.nombre = nombre
        self.documento = documento
        self.celular = celular
        self.lista_carros = lista_carros

    def addCar(self, car):
        self.lista_carros.append(car)
    
    def listCar(self):
        for x in self.lista_carros:
            print("carro con placas: " + x.placa)