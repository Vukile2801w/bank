import bank
import klijent
from tools import UniqueIDGenerator, unesi_lozinku 
import os
import random

file_path = 'data.txt'

id_gen = UniqueIDGenerator()

if os.path.exists(file_path):
    banka = bank.Bank()
    banka.load_data(file_path)
else:
    password = unesi_lozinku("Unesite novu sifru ")
    id:str = input("Unesite id (unesite _ za nasumicno)\nId mora biti samo broj duzine 6 num  ")
    while True:
        if id == "_":
            id = id_gen.generate_id()
            break
        elif len(id) == 6 and id.isdigit():
            id = input(id)
            break

        id = input("Molimo unesite odgovarajuci id ")

    banka = bank.Bank(password, id)
imena = [
    "Petar Petrovic", "Marko Markovic", "Ana Anic","Petar Petrovic", "Marko Markovic", "Ana Anic","Petar Petrovic", "Marko Markovic", "Ana Anic","Petar Petrovic", "Marko Markovic", "Ana Anic",
    "Petar Petrovic", "Marko Markovic", "Ana Anic","Petar Petrovic", "Marko Markovic", "Ana Anic","Petar Petrovic", "Marko Markovic", "Ana Anic","Petar Petrovic", "Marko Markovic", "Ana Anic"
    ]
for i in range(15):
    _klijent = klijent.Klijent(f"{i*4}{i*2}{i//2}", f"{imena[1]}{i}", id_gen.generate_id(), random.randrange(0, 10000))
    banka.novi_klijent(_klijent)

banka.save_date(file_path)
