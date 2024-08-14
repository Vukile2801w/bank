import random
import getpass

class UniqueIDGenerator:
    def __init__(self, existing_ids = set()):
        self.existing_ids = existing_ids

    def generate_id(self):
        while True:
            new_id = f"{random.randint(1, 999999):06d}"  # Generiše nasumičan broj i formatira kao šestocifreni string
            if new_id not in self.existing_ids:
                self.existing_ids.add(new_id)
                return new_id
            
    def get_ids(self):
        return self.existing_ids
    
    def replace_ids(self, ids):
        self.existing_ids = ids


def unesi_lozinku(msg):
    return getpass.getpass(msg)