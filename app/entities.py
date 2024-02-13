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

class Cupo():
    def __init__(self, letra):
        self.letra = letra

class Empleado():
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class Pago():
    def __init__(
            self,
            hora_i,
            fecha_i,
            hora_f,
            fecha_f,
            valor,
            carro,
            cupo,
            empleado
            ):
        self.hora_inicio = hora_i
        self.fecha_inicio = fecha_i
        self.hora_fin = hora_f
        self.fecha_fin = fecha_f
        self.valor = valor
        self.carro = carro
        self.cupo = cupo
        self.empleado = empleado