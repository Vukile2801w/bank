import klijent
from tools import UniqueIDGenerator, unesi_lozinku

class Bank:
    def __init__(self, master_password:str= "", bank_id:int= -1):
        
        self.id_generator = UniqueIDGenerator()

        self.password = master_password.encode()
        self.id = bank_id

        self.klijenti = []

    def save_date(self, file_path):
        with open(file_path, "a") as data:
            for i in self.klijenti:
                password:str = i.password
                name:str = i.name
                id:int = i.id
                balance:float = i.balance

                data.write(f"{name.title()} {id} {password} {balance}\n")
            
            data.write(f"{self.id_generator.get_ids()}\n")
            data.write(f"{self.password} {self.id}")

    def load_data(self, file_path):
        with open(file_path, "r") as data:
            for i in data.readlines():
                if i == data.readlines()[-2]:
                    self.id_generator.replace_ids(eval(i))
                    continue
                if i == data.readlines()[-1]:
                    bank_data = i.split(" ")
                    password = bank_data[0]
                    id = bank_data[1]

                    self.password = password
                    self.id = id

                klijent_data = i.split(" ")
                name = klijent_data[0]
                id = int(klijent_data[1])
                password = klijent_data[2]
                balance = float(klijent_data[3])

                klijent = klijent.Klijent(password, name, id, balance)

                self.klijenti.append(klijent)



    def pronadji_klijenta(self, nacin_pretrage:str, id=None, name=None):
        if nacin_pretrage == "id":
            if id == None:
                return
            
            for i in self.klijenti:
                if i.id == id:
                    return i
                
        elif nacin_pretrage == "name":
            if name == None:
                return
            
            for i in self.klijenti:
                if i.name == name:
                    return i
        
            

    def novi_klijent(self, klijent):
        self.klijenti.append(klijent)

    def ukloni_klijenta(self, klijent, user_password:str, master_password:str = None):

        if master_password.encode() == self.password:
            self.klijenti.remove(klijent)
            klijent.ukloni_racun()

        
        elif user_password.encode() == klijent.password:
            self.klijenti.remove(klijent)
            klijent.ukloni_racun()
        
    
    def pristup_klijentu(self, klijent, akcija):
        if akcija == "podigni":
            password = unesi_lozinku("Unesite korisnicku sifru").encode()
            kolicina = float(input("Unesite kolicinu koju zelite da podignete"))

            klijent.podigni(password, kolicina)
        
        elif akcija == "uplati":
            kolicina = float(input("Unesite kolicinu koju zelite da uplatite"))

            klijent.uplati(kolicina)
        
        elif akcija == "uplati_na_racun":
            password = unesi_lozinku("Unesite korisnicku sifru").encode()
            kolicina = float(input("Unesite kolicinu koju zelite da uplatite"))
            id = input("Unesite id racuna na koji hocete da uplatite")

            ciljani_klijent = self.pronadji_klijenta("id", id)
        
