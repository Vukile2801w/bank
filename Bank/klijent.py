class Klijent:
    def __init__(self, password: str, name: str, id: str, balance: float = 0) -> None:
        self.password = password.encode()
        self.name = name.replace(" ", "_")
        self.id = id
        self.balance = balance

    def podigni(self, password: str, kolicina: float) -> None:
        if password.encode() == self.password:
            if self.balance < kolicina:
                print("Nemate dovoljno novca na računu")
                if input(f"Možete da podignete: {self.balance} (Y/N)  ").capitalize() == "Y":
                    self.balance -= self.balance
                else:
                    return
            else:
                self.balance -= kolicina
            print(f"Ostalo vam je: {self.balance}")
        else:
            print("Šifra koju ste uneli je neodgovarajuća")

    def uplati(self, kolicina: float):
        self.balance += kolicina

    def uplati_na_racun(self, kolicina: float, ciljani_racun, password: str):
        if password.encode() == self.password:
            if self.balance < kolicina:
                print("Nemate dovoljno novca na računu")
                if input(f"Možete da podignete: {self.balance} (Y/N)  ").capitalize() == "Y":
                    ciljani_racun.uplati(self.balance)
                    self.balance -= self.balance
                else:
                    return
            else:
                self.balance -= kolicina
                ciljani_racun.uplati(kolicina)
            print(f"Ostalo vam je: {self.balance}")
            print(f"Prebacili ste {kolicina} na {ciljani_racun.id}")
        else:
            print("Šifra koju ste uneli je neodgovarajuća")
    
    def ukloni_racun(self):
        # Ovde ne bi trebalo da koristimo `del self`, već samo iz liste uklanjanja
        pass
