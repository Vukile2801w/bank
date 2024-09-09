import sys
import os
import unittest as uni



# Dodaj 'bank' folder u sys.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Bank')))

import tools

class TestExample(uni.TestCase):

    
    def test_Id_generator(self):
        tool = tools.UniqueIDGenerator(set([]))

        generated_ids = set()
        duplicate_found = False
        
        for i in range(10 ** 6):
            
            new_id = tool.generate_id()
            if new_id in generated_ids:
                duplicate_found = True
            else:
                generated_ids.add(new_id)
        
        self.assertFalse(duplicate_found, "Došlo je do duplikata ID-ova")
        return "test"

if __name__ == "__main__":
    uni.main()