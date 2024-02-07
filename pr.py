from string import ascii_uppercase
from random import choice,randint
import names

_ = 1
for _ in range(30):
    random_placa = result_str = ''.join(choice(ascii_uppercase) for i in range(3))
    tipos = ["Camion", "furgoneta", "Deportivo", "Clasico", "Vehiculo"]
    print(f'cliente{_} = Cliente("{names.get_full_name()}", "{randint(11111111, 999999999)}", "{randint(3141111111, 3149999999)}", lisra_carros)')

# for _ in range(300):
#     print(f"cliente{randint(1,2)}.addCar(carritto{_})")